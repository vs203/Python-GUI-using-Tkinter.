from tkinter import *
from tkinter.font import Font
from tkinter import ttk

from Trading_GUI.Scrape import list,list_1
if __name__ == '__main__':
    root = Tk()
    root.geometry('1050x500')
    root.title('Trade_Easy')
    photo = PhotoImage(file = r'E:\PYCHARM PROJECTS\Tkinter\Trading_GUI\dol.png')
    Label(image = photo , bg  ='black').place(x=10,y=80)
    photo_1 = PhotoImage(file = r'E:\PYCHARM PROJECTS\Tkinter\Trading_GUI\pound.png')
    Label(image = photo_1 ,bg = 'black').place(x=10,y=330)
    photo_2 = PhotoImage(file = r'E:\PYCHARM PROJECTS\Tkinter\Trading_GUI\eurosss.png')
    Label(image = photo_2 ,bg = 'black').place(x=820,y=80)
    photo_3 = PhotoImage(file = r'E:\PYCHARM PROJECTS\Tkinter\Trading_GUI\bundle.png')
    Label(image = photo_3 ,bg = 'black').place(x=820,y=350)

    dict = {}
    font_1 = Font(family="Comic Sans MS", size=20, weight="bold",  # slant = "italic" )
                  )
    Label(root, text = "Select a currency to get its value in INR" ,  font = font_1  , bg = 'black' , fg = 'white' ).place(x = 230 , y = 140  , )
    for currency in list:
        for value in list_1:
            dict[currency] = value
            list_1.remove(value)
            break

    def select(event):
        my_label = Label(root, text ="Current Exchange Rate for:\n" + my_combo.get()    +":\n" + dict[my_combo.get()] , pady = 10 , bg = 'black' , fg = 'white' , font = font_1).place(x = 330 , y =290)


    root.configure(background="black")
    root.wm_iconbitmap("dollars.ico")
    font = Font(family="Comic Sans MS", size = 30 , weight = "bold" , #slant = "italic" )
                )

    Label(root,text="Trade Easy" , font = font ,bg = "red" , fg= "black" , pady=10).pack(fill = X )


    #Combo-box

    my_combo = ttk.Combobox(root , value = list , width = 50 , justify = CENTER , exportselection=0 )
    my_combo.current(0)
    my_combo.bind("<<ComboboxSelected>>" ,select)
    my_combo.place(x = 350, y =250)





root.mainloop()