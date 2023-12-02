if __name__ == '__main__':
    print("Enter the number of opertions you want to perform")
    N = int(input())
    number_list = []
    print("Print out all those number of commands along with their item")
    print("Commands are insert, remove, append, sort, reverse and print")
    for i in range(N):
        commands = input().split()
        if commands[0] == "insert":
            number_list.insert(int(commands[1]), int(commands[2]))
        elif commands[0] == "print":
            print(number_list)
        elif commands[0] == "remove":
            number_list.remove(int(commands[1]))
        elif commands[0] == "append":
            number_list.append(int(commands[1]))
        elif commands[0] == "sort":
            number_list.sort()
        elif commands[0] == "pop":
            number_list.pop()
        elif commands[0] == "reverse":
            number_list.reverse()
        