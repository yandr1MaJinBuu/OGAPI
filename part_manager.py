from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if attacker_text.get() == '' or defender_text.get() == '' or server_text.get() == '' or combat_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(attacker_text.get(), defender_text.get(),
              server_text.get(), combat_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (attacker_text.get(), defender_text.get(),
                            server_text.get(), combat_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        attacker_entry.delete(0, END)
        attacerdefenderservercombat_entry.insert(END, selected_item[1])
        defenderservercombat_entry.delete(0, END)
        defenderservercombat_entry.insert(END, selected_item[2])
        servercombat_entry.delete(0, END)
        servercombat_entry.insert(END, selected_item[3])
        combat_entry.delete(0, END)
        combat_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], attacker_text.get(), defender_text.get(),
              server_text.get(), combat_text.get())
    populate_list()


def clear_text():
    attacker_entry.delete(0, END)
    defender_entry.delete(0, END)
    server_entry.delete(0, END)
    combat_entry.delete(0, END)


# Create window object
app = Tk()

# Part
attacker_text = StringVar()
attacker_label = Label(app, text='Attacker', font=('bold', 14), pady=20)
attacker_label.grid(row=0, column=0, sticky=W)
attacker_entry = Entry(app, textvariable=attacker_text)
attacker_entry.grid(row=0, column=1)
# Customer
defender_text = StringVar()
defender_label = Label(app, text='Defender', font=('bold', 14))
defender_label.grid(row=0, column=2, sticky=W)
defender_entry = Entry(app, textvariable=defender_text)
defender_entry.grid(row=0, column=3)
# Retailer
server_text = StringVar()
server_label = Label(app, text='Server', font=('bold', 14))
server_label.grid(row=1, column=0, sticky=W)
server_entry = Entry(app, textvariable=server_text)
server_entry.grid(row=1, column=1)
# Price
combat_text = StringVar()
combat_label = Label(app, text='Combat API', font=('bold', 14))
combat_label.grid(row=1, column=2, sticky=W)
combat_entry = Entry(app, textvariable=combat_text)
combat_entry.grid(row=1, column=3)
# Parts List (Listbox)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add CR', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Remove', width=12, command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Update', width=12, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=3)

app.title('OGame CR-API Saver')
app.geometry('480x350')

# Populate data
populate_list()

# Start program
app.mainloop()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''
