import glob
li = glob.glob("files/*")

for filpath in li:
    with open(filpath,"r")  as file:
        print(file.read())


