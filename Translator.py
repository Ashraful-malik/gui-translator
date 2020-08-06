from tkinter import *
from tkinter import ttk
import time
from tkinter import messagebox
from gtts import gTTS
from playsound import playsound
from translate import Translator


def translate():
    try:
        translator = Translator(from_lang=language.get(), to_lang=Translate_language.get())
        user_data = textbox1.get(0.1, END)
        translate_words = translator.translate(user_data)
        textbox2.insert(END, translate_words)
    except Exception:
        messagebox.showinfo("", "I think your Internet connection is poor.")


def speek():
    try:
        tts = gTTS(textbox2.get(0.1, END), lang='en')
        tts.save('text.mp3')
        playsound('text.mp3')
    except Exception:
        messagebox.showinfo("", 'please Check your Internet connection.')


window = Tk()
window.geometry("950x400")
window.title("Translator")
window.resizable(False, False)


# this combobox for choose language for translate
language = StringVar()
choose_language = ttk.Combobox(window, width=20, textvariable=language, font="arial 12 bold")
choose_language['values'] = ('ENGLISH', 'HINDI', 'URDU', 'CHINESE', 'SPANISH', 'ARABIC')
choose_language.current(0)

# This combobox of in which language you want to Translate words.
Translate_language = StringVar()
Translate_language = ttk.Combobox(window, width=20, textvariable=Translate_language, font="arial 12 bold")
Translate_language['values'] = ('ENGLISH', 'HINDI', 'CHINESE', 'SPANISH', 'ARABIC',
                                'JAVANESE', 'BENGALI', 'RUSSIAN', 'JAPANESE')
Translate_language.current(1)

# this text box for writing.
textbox1 = Text(window, width=40, height=10, font="arial 15 bold")

# this text box for show Result.
textbox2 = Text(window, width=40, height=10, font=" arial 15 bold")

# Button for translate languages.
translate_btn = Button(window, text="Translate", font="Saffron 15 italic ", width=30, command=translate,
                       fg="red", bg="orange", relief="flat")

# add mic button
mic = PhotoImage(file='microphone.png')
mic_button = Button(image=mic, command=speek)

# adding time in window
add_time = Label(window, font='arial 20', bg='skyblue')


def real_time():
    add_time.config(text=time.strftime('%r'))
    add_time.after(1, real_time)


real_time()

window.config(bg='skyblue')

# pack

add_time.grid(row=0, column=1)
Translate_language.grid(row=1, column=2)
choose_language.grid(row=1, column=1)
translate_btn.grid(row=3, column=0, columnspan=3, pady=8)
textbox1.grid(row=2, column=1)
textbox2.grid(row=2, column=2)
mic_button.grid(row=1, column=4)
window.mainloop()
