import matplotlib.pyplot as plt


def ReadFromFile():
    print("=" * 50)
    file = open('Новая форма.txt', encoding="utf8")
    a = file.readlines()
    file.close()
    return a


def ReadQuestionsIndexes():
    questionsCount = len(fileRead[2].split("\",\""))
    return sorted([int(i) for i in set(input(f"  Enter question indexes from 1 to {questionsCount - 1} >>> ").split())
                   if 0 < int(i) < questionsCount])


def IsNotTrash(answer):
    trash = open("Маты.txt", encoding="utf8").readline().split(",")
    if answer.lower() in ["нет", "да", "no", "yes"]:
        return True
    if answer == "" or answer.isupper() or len(set(answer)) < 4:
        return False

    for i in trash:
        if i in answer.lower():
            return False

    return True


def SaveAnswersInMassiv():
    n1 = (fileRead[0] + fileRead[1])[1:-2].rstrip().split('\",\"')
    questionsWithAnswers = [[] for i in range(len(n1))]

    for ind in questionIndexes:
        questionsWithAnswers[ind].append(n1[ind])

    for i in range(2, len(fileRead)):
        x = fileRead[i][1:-2].rstrip().split('\",\"')
        for ind in questionIndexes:
            if IsNotTrash(x[ind].rstrip()):
                questionsWithAnswers[ind].append(x[ind])
    return [i for i in questionsWithAnswers if i != []]


def CreateGraph(mass, i):
    t = mass
    labels = sorted(set(t))
    sizes = [round(t.count(i) * 100 / len(t)) for i in set(t)]
    # explode = (0, 0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.savefig(fr"C:\Users\Pavel\Desktop\ОПД 1 семестр\Graphs\graph{i}.png", dpi=200)


def WriteGraph():
    for i in range(len(answers)):
        t = answers[i][1:]
        if len(set(t)) <= 4:
            CreateGraph(t, i + 1)


def OutputAnswers(question, answers, f):
    f.write(question + '\n')
    for i in range(len(answers)):
        f.write(f"      {i + 1}) {answers[i]}\n")
    f.write("\n")


def WriteToFile():
    numberOfRespondents = len(fileRead) - 2
    fileName = rf'{input("  Enter the file name >>> ")}.txt'
    if (fileName != ".txt"):
        try:
            file = open(fr"C:\Users\Pavel\Desktop\ОПД 1 семестр\Опросы\{fileName}", 'w', encoding="utf8")
            file.write(f"Количество опрошенных {numberOfRespondents}\n\n")
            i = 0
            for indexAns in answers:
                OutputAnswers(f"{questionIndexes[i]}. {indexAns[0]}", indexAns[1:], file)
                i += 1
            file.close()
            print(f'{"=" * 20} Success! {"=" * 20}')
        except FileNotFoundError:
            print(f'\n{" " * 20} Error! {" " * 20}')


# Считываем и сохраняем данные
fileRead = ReadFromFile()
questionIndexes = ReadQuestionsIndexes()
answers = SaveAnswersInMassiv()

# Выводим данные
WriteGraph()
WriteToFile()
