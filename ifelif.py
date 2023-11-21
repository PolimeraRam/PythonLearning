while True:
    userText = input("Always Type add, show or exit.").strip()
    with open("files/todo.txt", "r") as file:
        li = file.readlines()

        if "add" in userText:
            y = userText[4:]
            li.append(y + "\n")
            file = open("files/todo.txt", "w")
            file.writelines(li)
            file.close()
        elif "show" in userText:
            print(li)
            for i, j in enumerate(li):
                print(i + 1, ":", j.strip("\n"))
            # print(f"New Format string: {i+1}={j}")

        # print(list(enumerate(li)))
        elif "edit" in userText:
            i = int(userText[5:])
            v = input("Enter Element Text: ")
            li[i - 1] = v + "\n"
            print(li)
            file = open("files/todo.txt", "w")
            file.writelines(li)
            file.close()

        elif "exit" in userText:
            break
        else:
            print("Command not valid.")

print("Bye")
