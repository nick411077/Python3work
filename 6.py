import csv

# 開啟 CSV 檔案
with open('student.csv', newline='',encoding='utf-8') as csvfile:
  # 讀取 CSV 檔案內容
    rows = csv.reader(csvfile)
  # 以迴圈輸出每一列
    i = False
    for row in rows:
        if i:
            sum=0
            average=0
            print(row[0]+":總和:",end="")
            for i in range(2,8):
                sum+=int(row[i])
            average=sum/6
            print(str(sum)+"平均:"+str(round(average,2)))
        else:
            i=True