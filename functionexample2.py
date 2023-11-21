# from functions import get_list_from_file, write_list_to_file
import functions

while True:
    userText = input("Always Type add, show or exit.").strip()
    li = functions.get_list_from_file()

    if "add" in userText:
        y = userText[4:]
        li.append(y + "\n")
        functions.write_list_to_file(li)

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
        functions.write_list_to_file(li)

    elif "exit" in userText:
        break
    else:
        print("Command not valid.")

print("Bye")
