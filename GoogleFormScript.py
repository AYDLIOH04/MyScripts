import shutil


def SaveAnswersInMassiv():
    n1 = (a[0] + a[1])[1:-2].rstrip().split('\",\"')
    questionsWithAnswers = [[] for i in range(len(n1))]

    for ind in questionIndexes:
        questionsWithAnswers[ind].append(n1[ind])

    for i in range(2, len(a)):
        x = a[i][1:-2].rstrip().split('\",\"')
        for ind in questionIndexes:
            if (x[ind].rstrip() != ""):
                questionsWithAnswers[ind].append(x[ind])
    return [i for i in questionsWithAnswers if i != []]


def OutputAnswers(question, answers, f):
    f.write(question + '\n')
    for i in range(len(answers)):
        f.write(f"      {i + 1}) {answers[i]}\n")
    f.write("\n")


def WriteToFile():
    try:
        file = open(fileName, 'w', encoding="utf8")
        file.write(f"Количество опрошенных {numberOfRespondents}\n\n")
        i = 0
        for indexAns in answers:
            OutputAnswers(f"{questionIndexes[i]}. {indexAns[0]}", indexAns[1:], file)
            i += 1
        file.close()

        shutil.copy(fr'C:\Users\Pavel\Desktop\ОПД 1 семестр\Scripts\{fileName}',
                    r"C:\Users\Pavel\Desktop\ОПД 1 семестр")

        print(f'{"="*20} Success! {"="*20}')
    except FileNotFoundError:
        print(f'\n{" "*20} Error! {" "*20}')


print("=" * 50)
file = open('Новая форма.txt', encoding="utf8")
a = file.readlines()
file.close()

questionsCount = len(a[2].split("\",\""))
questionIndexes = [int(i) for i in set(input(f"  Enter question indexes from 1 to {questionsCount - 1} >>> ").split()) if 0 < int(i) < questionsCount]
questionIndexes.sort()

answers = SaveAnswersInMassiv()
numberOfRespondents = len(a) - 2
fileName = rf'{input("  Enter the file name >>> ")}.txt'

WriteToFile()


