from tkinter import messagebox
from requests import get
from json import loads
from tkinter import *

table = []
okno = Tk()

def showweather():
    for x in range(0,len(table)):
        if table[x][0] == lista.get(lista.curselection()):
            messagebox.showinfo(title="Temperatura",message=table[x][1]+" stopni Celsujsza")
            


url = 'https://danepubliczne.imgw.pl/api/data/synop'
response = get(url)


for row in loads(response.text):
    table.append([row['stacja'],row['temperatura']])
    
okno.title("WeathPY")
okno.geometry("300x300")

lista = Listbox(okno)

for x in range(0,len(table)):
    lista.insert(x,table[x][0])
lista.pack()

przycisk = Button(okno,text="Sprawdź pogodę",command=showweather)
przycisk.pack()

okno.mainloop()








