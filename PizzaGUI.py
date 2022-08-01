#Pizza Oerdering App
#Hannah Wagner
#7/31/2022
#The purpose of this program is for a user to order pizza.
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

pizza = Tk()
pizza.geometry("600x500")
pizza.title("My Pizza Ordering App")


# User Input of information

name_label = Label(pizza, text = "What is your name?")
name_label.grid(row = 0, column = 0)

name_entry = Entry(pizza, width = 30)
name_entry.grid(row = 0, column = 1)

address_label = Label(pizza, text = "What is your address?")
address_label.grid(row = 1, column = 0)

address_entry = Entry(pizza, width = 30)
address_entry.grid(row = 1, column = 1)

number_label = Label(pizza, text = "What is your phone number?")
number_label.grid(row = 2, column = 0)

number_entry = Entry(pizza, width = 30)
number_entry.grid(row = 2, column = 1)

#Pizza Menu
my_pizza_menu = ["cheese", "pepperoni", "mushroom", "pineapple", "meat lovers"]

pizza_menu = Listbox(pizza, selectmode = MULTIPLE, bg="white", fg="black")
pizza_menu.grid(row = 3, column = 1)

for item in my_pizza_menu:
    pizza_menu.insert(0, item)
#Adds users pizza selection
def add_pizza():
    result = ""
    for item in pizza_menu.curselection():
        result = result + str(pizza_menu.get(item)) + "\n"
        add_lbl.config(text = "Your Pizza: " + "\n" + result)

add_lbl = Label(pizza, text = "")
add_lbl.grid(row = 9, column = 1)


add_button = Button(pizza, text = "Add Pizza", command = add_pizza)
add_button.grid(row = 5, column = 1)


def check():
    text1 = name_entry.get()
    new_lbl = Label(pizza, text = "Name: " + text1)
    new_lbl.grid(row = 12, column = 1)

    text2 = address_entry.get()
    new_lbl2 = Label(pizza, text = "Address: " + text2)
    new_lbl2.grid(row = 13, column = 1)

    text3 = number_entry.get()
    new_lbl3 = Label(pizza, text = "Phone Number: " + text3 )
    new_lbl3.grid(row = 14, column = 1)

check_out_button = Button(pizza, text = "Check Out", command = check)
check_out_button.grid(row = 6, column = 1)

def delete():
   pizza_menu.delete(0,5)
#Confirms the users decision to exit the program
def exit():
    answer = messagebox.askyesno("", "Are you sure you want to exit?")
    if answer == 1:
        pizza.destroy()
    else:
        return




delete_button = Button(pizza, text = "Delete Pizza", command = delete)
delete_button.grid(row = 7, column = 1)

exit_button = Button(pizza, text = "Exit", command = exit)
exit_button.grid(row = 8, column = 1)




pizza.mainloop()