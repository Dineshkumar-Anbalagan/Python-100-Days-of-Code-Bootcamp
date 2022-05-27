print("Welcome to the treasure map")
row1 = ["🔑", "🔑", "🔑"]
row2 = ["🔑", "🔑", "🔑"]
row3 = ["🔑", "🔑", "🔑"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
x, y = list(str(input("Where do you wanna put the treasure? ")))
if x and y:
    map[int(y)-1][int(x)-1] = "X"
    print(map)
else:
    print("Please enter two digit integers and try again")