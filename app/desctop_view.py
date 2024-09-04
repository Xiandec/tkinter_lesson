import tkinter as tk
from math import cos, sin

class main_window:
    def __init__(self, master) -> None:
        self.master = master
        self.w = 600
        self.h = 600
        self.angle = 0
        self.r = 220
        self.speed = 0.01
        self.direction = -1
        self.master.geometry(f'{self.w}x{self.h + 50}+{self.master.winfo_screenwidth() // 2 - self.w // 2}+{self.master.winfo_screenheight() // 2 - self.h // 2}')
        self.buttons_frame = tk.Frame(self.master)

        self.c = tk.Canvas(self.master, width=self.w, height=self.h)
        self.c.pack()

        self.change_dir_btn = tk.Button(self.buttons_frame, text = 'Change direction', width = 10, command = self.change_direction)
        self.change_dir_btn.pack(side=tk.LEFT)

        self.slider = tk.Scale(self.buttons_frame, from_=1, to=10, orient=tk.HORIZONTAL)
        self.slider.pack(side=tk.RIGHT)

        self.buttons_frame.pack()

        self.c.create_oval(100, 100, self.w - 100, self.h - 100, fill='white', outline='black')
        x = self.r * cos(self.angle) + self.w // 2
        y = self.r * sin(self.angle) + self.h // 2
        self.circle = self.c.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red', outline='black')
        self.update_position()

    def update_position(self) -> None:
        x = self.r * cos(self.angle) + self.w // 2
        y = self.r * sin(self.angle) + self.h // 2
        self.c.moveto(self.circle, x - 10, y - 10)
        self.speed = self.slider.get() / 100
        self.angle += self.speed * self.direction
        self.master.after(10, self.update_position)
        return 

    def change_direction(self) -> None:
        self.direction *= -1
        return 
