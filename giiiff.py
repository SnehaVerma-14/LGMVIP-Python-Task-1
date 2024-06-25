# Importing the required libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from moviepy.video.io.VideoFileClip import VideoFileClip


# Creating root window
root = tk.Tk()


#setting title
root.title("ProjectGurukul - GIF Creator")


#setting window size
root.geometry("600x400")
root.resizable(width=False, height=False)
root.configure(background="#D7BDE2")

# function to select input file
def input_file():
    global input_file_name
    input_file_name = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("PDF files", ".mp4"), ("all files", ".*")))
    input_label.configure(text="Input File : " + input_file_name.split("/")[-1])

# function to select output file
def output_file():
    global output_file_name
    output_file_name = filedialog.asksaveasfilename(initialdir = "/", title = "Select file", filetypes = (("GIF files", ".gif"), ("all files", ".*")))
    output_label.configure(text="Save As : " + output_file_name.split("/")[-1])

# function to create gif
def create_gif():


    # getting start and end time
    start_time = int(start_range.get())
    end_time = int(stop_range.get())


   # checking for errors
    if start_time > end_time:
        messagebox.showerror("Error", "Start time is greater than end time")
        return
    if end_time < 0 or start_time < 0:
        messagebox.showerror("Error", "Start and end time should be positive")
        return
    if input_file_name == None or output_file_name == None:
        messagebox.showerror("Error", "Input file and output file not selected")
        return
  
    # creating gif
    clip = VideoFileClip(input_file_name)
    subclip = clip.subclip(start_time, end_time)
    subclip.write_gif(output_file_name, verbose=False)


    # showing success message
    messagebox.showinfo("Success", "GIF created successfully")

# Creating GUI
title_label=tk.Label(root)
title_label.configure(background="#095aaa",foreground="#ABEBC6",font="Arial 18 bold",justify="center",text="ProjectGurukul - GIF Creator")
title_label.place(x=0,y=0,width=600,height=45)


input_label=tk.Label(root)
input_label.configure(background="#D7BDE2",foreground="#333333",font="Arial 14",justify="center",text="Input File : ")
input_label.place(x=20,y=70,width=328,height=40)


input_button=tk.Button(root)
input_button.configure(font="Arial 14",justify="center",text="Choose File",command=input_file)
input_button.place(x=380,y=70,width=160,height=40)


range_label=tk.Label(root)
range_label.configure(background="#D7BDE2",foreground="#333333",font="Arial 16 bold",justify="center",text="Enter Start and End Time (in seconds)")
range_label.place(x=150,y=130,width=300,height=41)


start_range=tk.Entry(root)
start_range.configure(font="Arial 30",justify="center", background="#1E1E1E", foreground="white")
start_range.place(x=200,y=170,width=80,height=60)


stop_range=tk.Entry(root)
stop_range.configure(font="Arial 30",justify="center", background="#1E1E1E", foreground="white")
stop_range.place(x=320,y=170,width=80,height=60)


range_label2=tk.Label(root)
range_label2.configure(background="#D7BDE2",foreground="#333333",font="Arial 30",justify="center",text="−")
range_label2.place(x=280,y=170,width=40,height=60)


output_label=tk.Label(root)
output_label.configure(background="#D7BDE2",foreground="#333333",font="Arial 14",justify="center",text="Save As : ")
output_label.place(x=20,y=260,width=328,height=38)


output_button=tk.Button(root)
output_button.configure(font="Arial 14",justify="center",text="Choose Path", command=output_file)
output_button.place(x=380,y=260,width=160,height=40)


create_button=tk.Button(root)
create_button.configure(font="Arial 20 bold",justify="center",text="Create GIF", command=create_gif)
create_button.place(x=200,y=330,width=205,height=52)

# Running the root window
root.mainloop()