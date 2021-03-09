from tkinter import *
import pandas
import random
Background_color = '#B1DDC6'
index = 0
new_data = 0
# ---------- Card Change --------- #


def next_step():
    global index
    global new_data
    canvas.itemconfig(card_image, image=front_img)
    new_data = random.choice(french_list)
    # print(new_data)
    index = french_list.index(new_data)
    canvas.itemconfig(Title, text='French')
    canvas.itemconfig(body, text=new_data)
    window.after(3000, cycle)


def remove():
    # print(english_list)
    # print(index)
    french_list.remove(new_data)
    english_list.remove(english_list[index])
    # print('Word removed')
    # print(english_list)


def cycle():
    canvas.itemconfig(Title, text='English')
    canvas.itemconfig(body, text=english_list[index])
    canvas.itemconfig(card_image, image=back_img)


window = Tk()
window.config(width=1000, height=800)
file = pandas.read_csv('./data/french_words.csv')
french_list = file['French'].to_list()
english_list = file['English'].to_list()


canvas = Canvas(width=1200, height=800, bg=Background_color)
back_img = PhotoImage(file='./images/card_back.png')
front_img = PhotoImage(file='./images/card_front.png')
card_image = canvas.create_image(600, 320, image=front_img)
title = 'Title'
Title = canvas.create_text(600, 200, text=title, font=('serif', 20, 'italic'))
body = canvas.create_text(600, 280, text='Word', font=('Arial', 45, 'bold'))
canvas.grid(row=0, column=0, columnspan=8, rowspan=3)
right_image = PhotoImage(file='./images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=next_step)
right_button.grid(row=2, column=5)
wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=remove)
wrong_button.grid(row=2, column=2)
window.mainloop()
