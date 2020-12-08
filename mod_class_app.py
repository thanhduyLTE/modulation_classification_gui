# -*- coding: utf-8 -*-
import numpy as np
# from Tkinter import *
import tkinter as tk

stream_length = np.random.randint(256, 4096)
stream = np.random.rand(stream_length,2,128)
list_sample = []
sample = 5000
HEIGHT = 600
WIDTH = 800
bg = '#33FFF3'
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        master.config(bg=bg)
        canvas = tk.Canvas(master, height=HEIGHT, width=WIDTH, bg=bg)
        canvas.pack()
	       
        # background_image = tk.PhotoImage(file='background.png')
        # background_label = tk.Label(master, image=background_image)
        # background_label.place(relwidth=1, relheight=1)

        frame_top = tk.Frame(master, bg=bg, bd=5)
        frame_top.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.1, anchor='n')

        frame_middle = tk.Frame(master, bg='blue', bd=5)
        frame_middle.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.65, anchor='n')

        frame_bottom = tk.Frame(master, bg=bg, bd=5)
        frame_bottom.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')


        header = tk.Label(frame_top, text='PHẦN MỀM\nNHẬN DẠNG LOẠI ĐIỀU CHẾ TÍN HIỆU', bg=bg,foreground ='red', font=('Arial',18,'bold')) .place(relx=0.5, anchor='n')
        footer = tk.Label(frame_bottom, text='Viện Điện tử \nPhòng Nghiên cứu thiết bị huấn luyện và ĐTYS',  bg=bg,foreground ='blue',font=('Arial',18,'bold')).place(relx=0.5, anchor='n')


        rel_start_left = 0.05
        rel_start_right = 0.45
        rel_width = 0.35
        rel_height = 0.20
        font_size = 15
        loaidieuche = tk.Label(frame_middle, text='Loại điều chế:', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        loaidieuche.place(relx= rel_start_left, rely=0.1,relwidth=rel_width,relheight= rel_height)

        dochinhxac = tk.Label(frame_middle, text='Độ chính xác:', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        dochinhxac.place(relx= rel_start_left, rely=0.3,relwidth=rel_width,relheight= rel_height)

        tgnhandang = tk.Label(frame_middle, text='Thời gian nhận dạng:', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        tgnhandang.place(relx= rel_start_left, rely=0.5,relwidth=rel_width,relheight= rel_height)

        result_dieuche = tk.Label(frame_middle, text='QPSK', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        result_dieuche.place(relx= rel_start_right, rely=0.1,relwidth=rel_width,relheight= rel_height)

        result_acc = tk.Label(frame_middle, text='99%', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        result_acc.place(relx= rel_start_right, rely=0.3,relwidth=rel_width,relheight= rel_height)

        result_time = tk.Label(frame_middle, text='0.002s', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        result_time.place(relx= rel_start_right, rely=0.5,relwidth=rel_width,relheight= rel_height)

        onoff = tk.Label(frame_middle, text='On/Off', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size), anchor= 'w')
        onoff.place(relx= rel_start_left, rely=0.7,relwidth=rel_width,relheight= rel_height)
        # self.greet_button = tk.Button(master, text="Greet", command=self.greet)
        # self.greet_button.pack()

        # self.close_button = tk.Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def greet(self):
        print("Greetings!")

root = tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
