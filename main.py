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
    except Exception as err:
        print(str(err))
        return
    for item in aqi_list:
        print(item)
    window = Window()
    window.title("碳足跡CarbonFootPrint")
    window.mainloop()
#啟動點
if __name__ == "__main__":
    main()