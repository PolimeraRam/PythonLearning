date = input("Enter Date: ")
mood = input("How do you rate mood out of 1 to 10: ")
thoughts = input("Describe your thoughts:\n")
with open(f"journal\{date}.txt","w") as f:
    f.write(mood + (2 * "\n"))
    f.write(thoughts)
    
s = "ramramramra"
x = s.strip("ra")
print(x)


