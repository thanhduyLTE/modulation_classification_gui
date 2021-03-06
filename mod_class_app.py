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

rel_start_left = 0.1
rel_start_right = 0.55
rel_width = 0.35
rel_height = 0.20
font_size = 15
delta_y = 0.3
left_start_y = 0
labels_list = []
class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sample and prediction")
        master.config(bg=bg)
        canvas = tk.Canvas(master, height=HEIGHT, width=WIDTH, bg=bg)
        canvas.pack()


        frame_top = tk.Frame(master, bg=bg, bd=5)
        frame_top.place(relx=0.5, rely=0.05, relwidth=0.75, relheight=0.15, anchor='n')

        self.frame_middle = frame_middle = tk.Frame(master, bg=bg, bd=5)
        frame_middle.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.65, anchor='n')

        frame_bottom = tk.Frame(master, bg=bg, bd=5)
        frame_bottom.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.15, anchor='n')


        header = tk.Label(frame_top, text='PHẦN MỀM\nNHẬN DẠNG LOẠI ĐIỀU CHẾ TÍN HIỆU', bg=bg,foreground ='red', font=('Arial',18,'bold')) .place(relx=0.5, anchor='n')
        footer = tk.Label(frame_bottom, text='Viện Điện tử \nPhòng Nghiên cứu thiết bị huấn luyện và ĐTYS',  bg=bg,foreground ='blue',font=('Arial',18,'bold')).place(relx=0.5, anchor='n')


        

        

        loaidieuche = tk.Label(frame_middle, text='Loại điều chế:', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        loaidieuche.place(relx= rel_start_left, rely=left_start_y,relwidth=rel_width,relheight= rel_height)

        dochinhxac = tk.Label(frame_middle, text='Độ chính xác:', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        dochinhxac.place(relx= rel_start_left, rely=left_start_y + delta_y*1,relwidth=rel_width,relheight= rel_height)

        tgnhandang = tk.Label(frame_middle, text='Thời gian nhận dạng:', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        tgnhandang.place(relx= rel_start_left, rely=left_start_y + delta_y*2,relwidth=rel_width,relheight= rel_height)

        onoff = tk.Button(frame_middle, text='On/Off', bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size), anchor= 'w')
        onoff.place(relx= rel_start_left, rely=left_start_y + delta_y*2.7,relwidth=rel_width,relheight= rel_height)
        self.stream_predict()
    def stream_predict(self):
        if labels_list:
            for label in labels_list:
                label.destroy()
        mod_pred = tk.StringVar()
        time_pred = tk.StringVar()
        acc_pred = tk.StringVar()
        mods = ['BPSK','QPSK', 'QAM']
        mod_type = mods[np.argmax(np.random.rand(1,3)[0])]
        total_time = np.random.rand()/10000
        acc = 90+ np.random.rand()*10
        # print(acc)
        mod_pred.set(mod_type)
        time_pred.set('%.3fms'%(total_time*1000))
        acc_pred.set('%.3f'%acc)
        result_dieuche = tk.Label(self.frame_middle, textvariable=mod_pred,bg='white',foreground ='#d17219',relief="groove",borderwidth = 3,font=('Arial',font_size ,'bold'))
        result_dieuche.place(relx= rel_start_right, rely=left_start_y,relwidth=rel_width,relheight= rel_height)

        result_acc = tk.Label(self.frame_middle, textvariable=acc_pred, bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        result_acc.place(relx= rel_start_right, rely=left_start_y + delta_y*1,relwidth=rel_width,relheight= rel_height)

        result_time = tk.Label(self.frame_middle, textvariable=time_pred, bg='white',foreground ='black',relief="groove",borderwidth = 3,font=('Arial',font_size))
        result_time.place(relx= rel_start_right, rely=left_start_y + delta_y*2,relwidth=rel_width,relheight= rel_height)

        labels_list.extend([result_dieuche, result_acc, result_time])
        self.master.after(1000, self.stream_predict)

root = tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
