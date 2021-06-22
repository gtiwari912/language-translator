#Lib
from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator  #pip install googletrans==3.1.0a0
from tkinter import messagebox

#Frame of tkinter
root = tk.Tk()
root.title('Langauge Translator')
root.geometry('800x360')
root.maxsize(800,360)
root.config(bg='light blue')

#Icon 
root.iconbitmap(r'icon.png')

#Bg Image
img = PhotoImage(file="background.png")
label = Label(image=img)
label.place(x=0, y=0)


#Translate Function
def translate():
        lang_1 = t1.get("1.0","end-1c")
        cl = choose_langauge.get()

        if lang_1 == '':
                messagebox.showerror('Language Translator','please fill the box')
        else:
                t2.delete(1.0,'end')
                translator = Translator()
                output = translator.translate(lang_1, dest=cl)
                t2.insert('end',output.text)


#Clear Function
def clear():
        t1.delete(1.0,'end')
        t2.delete(1.0,'end')
        

#Class of Lang
lan = ['Auto Detect','English', 'Marathi', 'Hindi', 'Afrikaans', 'Albanian', 'Arabic', 'Azerbaijani', 'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian',
        'Catalan', 'Cebuano', 'Chichewa', 'Chinese', 'Corsican', 'Croatian', 'Czech', 'Danish', 'Dutch', 'Esperanto', 'Estonian', 'Filipino', 'Finnish',
        'French', 'Frisian', 'Galician', 'German', 'Greek,Haitian', 'Creole', 'Hausa', 'Hawaiian', 'Hmong', 'Hungarian', 'Icelandic', 'Igbo', 'Indonesian',
        'Irish', 'Italian', 'Japanese', 'Javanese', 'Kazakh', 'Korean', 'Kurdish', 'Kyrgyz', 'Latin', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Macedonian',
        'Malagasy', 'Malay', 'Maltese', 'Maori', 'Mongolian', 'Nepali', 'Norwegian', 'Pashto', 'Persian', 'Pilipino', 'Polish', 'Portuguese', 'Punjabi', 'Romanian',
        'Russian', 'Serbian', 'Sinhalese', 'Slovenian', 'Somali', 'Spanish', 'Swahili', 'Swedish', 'Tagalog', 'Taiwanese', 'Tamil', 'Telugu', 'Thai', 'Tibetan',
        'Tigrinya','Turkish', 'Twi', 'Ukrainian', 'Urdu', 'Vietnamese', 'Yiddish', 'Yoruba', 'Zulu']


#All Labels
Label(root, text="Translator", font=( "times new roman", 25,'bold','underline'),background='lightskyblue1').place(x=320,y=20)

Label(root, text="Select Language:", font=( "times new roman", 17,'bold'),background='lightskyblue1').place(x=50,y=70)
Label(root, text="Select Language:", font=( "times new roman", 17,'bold'),background='lightskyblue1').place(x=420,y=70)

Label(root, text="Enter Input text:-", font=( "times new roman", 17,'bold'),background='lightskyblue1').place(x=50,y=115)
Label(root, text="Enter Output text:-", font=( "times new roman", 17,'bold'),background='lightskyblue1').place(x=420,y=115)


#All Combobox
auto_detect = ttk.Combobox(root, width = 11, state='readonly',font=('times new roman',16,'bold'),value=lan) 
auto_detect.place(x=231,y=71)
auto_detect.current(0) 

choose_langauge = ttk.Combobox(root, width = 11, state='readonly',font=('times new roman',16,'bold'),value=lan) 
choose_langauge.place(x=601,y=71)
choose_langauge.current(2) 


#All TextBox
t1 = Text(root,font=('times new roman',14,'bold'),width=30,height=6,borderwidth=4,relief=RIDGE)
t1.place(x=70,y=155)

t2 = Text(root,font=('times new roman',14,'bold'),width=30,height=6,borderwidth=4,relief=RIDGE)
t2.place(x=445,y=155)


#Buttons
clear = Button(root,text="Clear",relief=RIDGE,borderwidth=3,font=('times new roman',17,'bold'),cursor="hand2",command=clear)
clear.place(x=170,y=305)

transl = Button(root,text="Translate",relief=RIDGE,borderwidth=3,font=('times new roman',17,'bold'),cursor="hand2",command=translate)
transl.place(x=540,y=305)


root.mainloop()
