x = int(input("要幾層："))
for i in range(x):         # 總共有4層
    for j in range(x - i - 1):  # 在第一個*號出現前，先印出空白
        print(" ", end="")
    for k in range(i + 1):       # 印出該層所需要的*字數量
        print("* ", end = "")
    print()                # 換行
