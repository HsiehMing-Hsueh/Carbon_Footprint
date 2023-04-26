import tkinter as tk
from tkinter import ttk
from tkinter import Button ,Frame
from datasoerce import CarbonFootPrint
from PIL import Image, ImageTk
import csv

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #建立topFrame
        topFrame = ttk.Labelframe(self)
        topFrame.pack()
        #----------------建立按鈕----------------------------
        self.option_add('*font',('verdana', 12, 'bold'))
        self.title("碳排放的窗口")
        
        Button(topFrame, text='石油').pack(side=tk.RIGHT)
        Button(topFrame, text='煤炭').pack(side=tk.RIGHT)
        Button(topFrame, text='天然氣').pack(side=tk.RIGHT)
            
        # --------------建立combobox--------------------------
        comboBoxFrame = ttk.LabelFrame(self,text="Combo Box")
        comboBoxFrame.pack(side=tk.LEFT,fill=tk.Y)

        csv_filename = 'a.csv'
        with open(csv_filename) as f:
            reader = csv.reader(f)
            lst = list(tuple(line) for line in reader)
            lst.insert(0,'請選擇一個國家')
        comboBoxValues  = (lst)   

        comboBox = ttk.Combobox(comboBoxFrame,state= "readonly")
        comboBox.pack()
        comboBox['values'] = comboBoxValues        
        comboBox.current(0)
        comboBox.pack(side=tk.LEFT)

        # ----------------建立logo--------------------
        logoImage = Image.open('./Images/co2logo.png')
        resizeImage = logoImage.resize((89,82), Image.LANCZOS)
        self.logoTkimage = ImageTk.PhotoImage(resizeImage)
        logoLabel = ttk.Label(topFrame, image=self.logoTkimage)
        logoLabel.pack(pady=(0,50),side=tk.LEFT)
        #建立medianFrame
        medianFrame =ttk.Labelframe(self)
        medianFrame.pack(side=tk.LEFT)
        #建立bottomFrame
        bottomFrame = ttk.Labelframe(self)
        bottomFrame.pack(side=tk.LEFT)
        #建立treeViewFrame
        treeViewFrame = ttk.Labelframe(self)
        treeViewFrame.pack(side=tk.RIGHT)
        #建立treeview
        columns = ('#1', '#2', '#3')
        tree = ttk.Treeview(treeViewFrame, columns=columns, show='headings')
        tree.heading('#1', text='country')
        tree.column("#1", minwidth=0, width=75)
        tree.heading('#2', text='population')
        tree.column("#2", minwidth=0, width=100)
        tree.heading('#3', text='co2')
        tree.column("#3", minwidth=0, width=30)
        tree.pack(side=tk.LEFT)
        #----------幫treeview加scrollbar----------------------------------
        scrollbar = ttk.Scrollbar(treeViewFrame, command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.config(yscrollcommand=scrollbar.set)
#主程式
def main():
    
    try:
        api_list = CarbonFootPrint.download_api()
        print(type(api_list))
        
        
    except Exception as err:
        print(str(err))
        return
    
    
    window = Window()
    window.title("碳足跡CarbonFootPrint")
    window.mainloop()
#啟動點
if __name__ == "__main__":
    main()