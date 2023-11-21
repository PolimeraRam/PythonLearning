def get_list_from_file():
     with open("files/todo.txt", "r") as file_local:
        li_local = file_local.readlines()
     return li_local



def write_list_to_file(li_local):
    with open("files/todo.txt", "w") as file_local:
        file_local.writelines(li_local)
    # assert isinstance(li_local, list)
    return li_local
