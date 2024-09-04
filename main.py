import tkinter as tk
from app.desctop_view import main_window

def main(): 
    root = tk.Tk()
    app = main_window(root)
    root.mainloop()

if __name__ == '__main__':
    main()