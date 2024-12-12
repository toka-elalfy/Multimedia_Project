import tkinter as tk
from tkinter import messagebox  
from gtts import gTTS
from playsound import playsound
import os

def text_to_speech():
    text = text_entry.get()
    if text.strip():  
        tts = gTTS(text, lang="ar") 
        file_path = "output.mp3"
        tts.save(file_path)  
        playsound(file_path) 
        os.remove(file_path)  
    else:
        messagebox.showwarning("تحذير", "الرجاء إدخال النص!")  

def clear_text():
    text_entry.delete(0, tk.END) 

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Text to Speech")
root.geometry("400x500")  
root.configure(bg="#FBF8EF")  

title_label = tk.Label(root, text="Text to Speech", font=("Arial", 20, "bold"), bg="#FBF8EF", fg="black")
title_label.pack(pady=20)

text_label = tk.Label(root, text="Enter your text:", font=("Arial", 14), bg="#FBF8EF", fg="black")
text_label.pack(pady=10)
text_entry = tk.Entry(root, width=40, font=("Arial", 12))
text_entry.pack(pady=10)

button_style = {"font": ("Arial", 14), "width": 15, "height": 2, "fg": "black"}  # Without bg

play_button = tk.Button(root, text="Play", command=text_to_speech, **button_style, bg="#E5E1DA")
play_button.pack(pady=10)

set_button = tk.Button(root, text="Set", command=clear_text, **button_style, bg="#B3C8CF")
set_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_program, **button_style, bg="#89A8B2")
exit_button.pack(pady=10)

root.mainloop()