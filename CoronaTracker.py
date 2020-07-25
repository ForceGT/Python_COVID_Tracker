import requests as r
import json
from tkinter import *

data = r.get("https://api.covid19india.org/data.json")
jsonContent = json.loads(data.text)
def table(root, total_rows, total_columns):
    e1 = Label(root, text="State", width=23, bg="#000", fg="white", font=('Arial', '18'))
    e1.grid(row=0, column=0)
    e2 = Label(root, text="Confirmed", width=23, bg="#000", fg="white", font=('Arial', '18'))
    e2.grid(row=0, column=1)
    e3 = Label(root, text="Deaths", width=23, bg="#000", fg="white", font=('Arial', '18'))
    e3.grid(row=0, column=2)
    e4 = Label(root, text="LastUpdatedAt", width=23, bg="#000", fg="white", font=('Arial', '18'))
    e4.grid(row=0, column=3)
    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(root, width=30, bg='#f4f6f6', fg='#cd3f3e', font=('Roboto', '12'), justify="center")
            e.grid(row=i+1, column=j)
            e.insert(END, lst[i][j])


lst = list()
for i in range(int(38)):
    stateName = jsonContent["statewise"][i]["state"]
    confirmedNumber = jsonContent["statewise"][i]["confirmed"]
    deaths = jsonContent["statewise"][i]["deaths"]
    lastUpdatedAt = jsonContent["statewise"][i]["lastupdatedtime"]
    data = (stateName, confirmedNumber, deaths, lastUpdatedAt)
    lst.append(data)

total_rows = len(lst)
total_columns = len(lst[0])
root = Tk()
table(root, total_rows, total_columns)
root.mainloop()
