contents = ["Content 1", "Content "
                         "shkjdsj "
                         " 2"]
filenames = ["filename1.txt", "filename2.txt","filename3.txt"]

str = "Thulasi Rami " \
      "Reddy"

# print(list(zip(filenames, contents )))

for c, f in zip(contents, filenames):
    file = open(f"files\{f}", "w")
    file.write(c)
    file.close()

