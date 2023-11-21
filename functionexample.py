def get_list_from_file():
     with open("files/todo.txt", "r") as file_local:
        li_local = file_local.readlines()
     return li_local



def write_list_to_file(li_local):
    with open("files/todo.txt", "w") as file_local:
        file_local.writelines(li_local)
    # assert isinstance(li_local, list)
    return li_local


while True:
    userText = input("Always Type add, show or exit.").strip()
    li = get_list_from_file()

    if "add" in userText:
        y = userText[4:]
        li.append(y + "\n")
        write_list_to_file(li)

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
        write_list_to_file(li)

    elif "exit" in userText:
        break
    else:
        print("Command not valid.")

print("Bye")
