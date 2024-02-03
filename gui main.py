# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''

root=tk.Tk()

root.title("Lane And Speed Breaker Detection")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

# bg = Image.open(r"E:/carrier_choice_prediction/y9.jpg")
# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
# bg_img = ImageTk.PhotoImage(bg)
# bg_lbl = tk.Label(root,image=bg_img)
# bg_lbl.place(x=0,y=93)
# #, relwidth=1, relheight=1)

video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("road1.mp4", video_label,loop = 1, size = (w, h))
player.play()

w = tk.Label(root, text="Lane And Speed Breaker Detection",width=90,background="#800517",foreground="white",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=0)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#800517")


from tkinter import messagebox as ms


def lan_CURVE_DETECTION ():
    from subprocess import call
    call(["python","laneDetectRansac.py"])

def speed ():
    from subprocess import call
    call(["python","GUI_Master_New.py"])



wlcm=tk.Label(root,text="...... WELCOME TO LANE AND SPEED BREAKER DETECTION SYSTEM ......",width=90, height=1, background="black",foreground="white",font=("Times new roman",19,"bold"))
wlcm.place(x=0,y=600)




d2=tk.Button(root,text="Lane Detection",command=lan_CURVE_DETECTION,width=25,height=2,bd=0,background="#808069",foreground="white",font=("times new roman",17,"bold"))
d2.place(x=30,y=150)
d3=tk.Button(root,text="Speed Breaker Detection",command=speed,width=25,height=2,bd=0,background="#808069",foreground="white",font=("times new roman",17,"bold"))
d3.place(x=30,y=250)


# d3=tk.Button(root,text="REGISTER",command=Register,width=20,height=2,bd=0,background="#800517",foreground="white",font=("times new roman",17,"bold"))
# d3.place(x=100,y=0)



root.mainloop()
