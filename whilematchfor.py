
while True:
    userText = input("Always Type add, show or exit.").strip()
    file = open("files/todo.txt", "r")
    li = file.readlines()
    file.close()

    match userText:
        case "add":
            y = input("Enter any value: ")
            li.append(y + "\n")
            file = open("files/todo.txt", "w")
            file.writelines(li)
            file.close()
        case "show":
            print(li)
            for i, j in enumerate(li):
                print(i+1, ":",  j)
               # print(f"New Format string: {i+1}={j}")

           # print(list(enumerate(li)))
        case "edit":
            i = int(input("Enter number to edit element"))
            v = input("Enter Element Text: ")
            li[i-1] = v
            print(li)
            file = open("files/todo.txt", "w")
            file.writelines(li)
            file.close()

        case "exit":
            break
        case whatever:
            print("Enter only specified values")

print("Bye")
