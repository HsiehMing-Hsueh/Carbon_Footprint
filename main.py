import tkinter as tk
from tkinter import ttk
from datasoerce import CarbonFootPrint

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        

#主程式
def main():
    
    try:
        aqi_list = CarbonFootPrint.download_aqi()
        print(type(aqi_list))
        
        
    except Exception as err:
        print(str(err))
        return
    
    
    window = Window()
    window.title("碳足跡CarbonFootPrint改一次title")
    window.mainloop()
#啟動點
if __name__ == "__main__":
    main()