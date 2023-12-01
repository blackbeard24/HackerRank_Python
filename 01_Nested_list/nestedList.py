if __name__ == '__main__':
    scoreList = []
    nameList = []
    listNameScore = []
    print("Enter how many recrods you are going enter.....")
    for i in range(int(input())):
        print("Enter the {} name and score".format(i+1))
        name = input()
        score = float(input())
        scoreList.append(score)
        listNameScore.append([name, score])
    
    lowestScore = list(set(scoreList))
    lowestScore.sort()
    for name, score in listNameScore:
        if score == lowestScore[1]:
            nameList.append(name)
    
    nameList.sort()
    print("The second lowest scored students")
    for name in nameList:
        print(name)
