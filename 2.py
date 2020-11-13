password = 1234
x = 0
while x < 3:
    if password == int(input("PASSWORD:")):
        print("done")
        break
    else:
        print("try again")
        x += 1
        if x == 3:
            print("error")
print("exit")
