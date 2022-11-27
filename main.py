from tkinter import *
from tkinter import filedialog

d = {}
with open("dictionary.txt") as file:
    for line in file:
        values = line.strip().split("-")  # The strip() method removes any leading
        # (spaces at the beginning) and trailing (spaces at the end) characters
        # (space is the default leading character to remove)
        if values:
            d[values[0]] = values[1:]


def click():
    text_input = textEntry.get()  # collects text from text entry
    output.delete(0.0, END)
    if text_input in d.keys():
        output.insert(END, str((d[text_input])))
    else:
        output.insert(END, "Sorry, can not find such a word, please try another one")


def close_window():
    window.destroy()
    exit()


window = Tk()
window.title("Python Glossary")
window.config(background="black")

photo_One = PhotoImage(file="Resource_Python.png")
photoImage = photo_One.subsample(2, 2)  # reduce image size
Label(window, image=photoImage, bg="black").grid(row=0, column=0, sticky=W)

textEntry = Entry(window, width=30, bg="white", fg="black", font=('arial', 16, 'bold'))
textEntry.grid(row=3, column=0, sticky=W)

Button(window, text="SUBMIT", width=14, command=click, font=('arial', 20, 'bold'), bg="DodgerBlue2", fg="black").grid(
    row=4, column=0, sticky=W)
Button(window, text="Exit", width=14, command=close_window, font=('arial', 20, 'bold'), bg="DodgerBlue2",
       fg="black").grid(row=7, column=0, sticky=W)

Label(window, text="Welcome to the Python glossary, Enter the word and get its fully meaning definition.", bg="black",
      fg="white",
      font="none 16 bold").grid(row=1, column=0, sticky=W)

Label(window, text="Enter the word you would like to definition for:", bg="black", fg="white",
      font="none 16 bold").grid(row=2, column=0)

output = Text(window, width=75, height=6, wrap=WORD, bg="white", fg="black", font=('arial', 16, 'bold'))
output.grid(row=5, column=0, columnspan=2, sticky=W)

if __name__ == "__main__":
    mainloop()

