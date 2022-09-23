import sys
import tkinter as tk
from tkinter import ttk
from datetime import date
from pyrecord import *
from pycategory import *

categories = Categories()
records = Records()

def balance(money):
    global bala_str
    records.set_balance(int(money))
    bala_str.set("Now you have " + str(records.balance) + " dollars.")

def delete():
    global record_box
    records.delete(record_box.index(record_box.curselection()))
    record_box.delete(record_box.curselection())
    bala_str.set("Now you have " + str(records.balance) + " dollars.")

def add(date, category, description, amount):
    category = category.replace(' ', '')
    category = category.replace('-','')
    records.add(date + ' ' + category + ' ' + description + ' ' + amount, categories)
    global record_box
    global bala_str
    record_box.delete(0, tk.END)
    for i , r in enumerate(records.records):
        record_box.insert(i, f'{r.date:<11}{r.category:<30}{r.description:<21}{r.amount}')
    bala_str.set("Now you have " + str(records.balance) + " dollars.")

def find(category):
    target_categories = categories.find_subcategories(category, categories._categories)
    L = records.find(target_categories)
    global record_box
    record_box.delete(0, tk.END)
    for i , r in enumerate(L[1]):
        record_box.insert(i, f'{r.date:<11}{r.category:<30}{r.description:<21}{r.amount}')
    global bala_str
    bala_str.set("Total amount above is " + str(L[0]) + " dollars.")

def reset():
    global record_box
    record_box.delete(0, tk.END)
    for i , r in enumerate(records.records):
        record_box.insert(i,  f'{r.date:<11}{r.category:<30}{r.description:<21}{r.amount}')
    global bala_str
    bala_str.set("Now you have " + str(records.balance) + " dollars.")
    

root = tk.Tk()
f = tk.Frame(root)
f.grid(row = 0, column = 0)
root.title('PyMoney')

find_label = tk.Label(f, text = 'Find category')
find_label.grid(row = 0, column = 0)
find_str = tk.StringVar()
find_entry = tk.Entry(f, textvariable = find_str)
find_entry.grid(row = 0, column = 1)
find_btn = tk.Button(f, text = 'Find', command = lambda: find(find_str.get()))
find_btn.grid(row = 0, column = 2)
rst_btn = tk.Button(f, text = 'Reset', command = lambda: reset())
rst_btn.grid(row = 0, column = 3)

init_label = tk.Label(f, text = 'Initial money')
init_label.grid(row = 1, column = 4)
init_str = tk.StringVar()
init_entry = tk.Entry(f, textvariable = init_str)
init_entry.grid(row = 1, column = 5)
init_entry.insert(0, 0)
upda_btn = tk.Button(f, text = 'Update', command = lambda: balance(init_str.get()))
upda_btn.grid(row = 2, column = 5, sticky='E')

spac_label = tk.Label(f, text = '')
spac_label.grid(row = 3, column = 4)

date_label = tk.Label(f, text = 'Date')
date_label.grid(row = 4, column = 4)
date_str = tk.StringVar()
date_entry = tk.Entry(f, textvariable = date_str)
date_entry.grid(row = 4, column = 5)
date_entry.insert(0, str(date.today()))

cate_label = tk.Label(f, text = 'Category')
cate_label.grid(row = 5, column = 4)
cate_str = tk.StringVar()
cate_combo = ttk.Combobox(f, values = ['- expense',
                                       '  - food',
                                       '    - meal',
                                       '    - snack', 
                                       '    - drink',
                                       ' - transportation', 
                                       '    - bus', 
                                       '    - railway',
                                       '- income', 
                                       '  - salary', 
                                       '  - bonus'], width = 18)
cate_combo.grid(row = 5, column = 5)

desc_label = tk.Label(f, text = 'Description')
desc_label.grid(row = 6, column = 4)
desc_str = tk.StringVar()
desc_entry = tk.Entry(f, textvariable = desc_str)
desc_entry.grid(row = 6, column = 5)

amou_label = tk.Label(f, text = 'Amount')
amou_label.grid(row = 7, column = 4)
amou_str = tk.StringVar()
amou_entry = tk.Entry(f, textvariable = amou_str)
amou_entry.grid(row = 7, column = 5)
add_btn = tk.Button(f, text = 'Add a record', command = lambda: add(date_str.get(), cate_combo.get(), desc_str.get(), amou_str.get()))
add_btn.grid(row = 8, column = 5, sticky='E')

record_box = tk.Listbox(f, width = 47)
record_box.grid(row = 1, column = 0, rowspan = 8, columnspan = 4)
for i , r in enumerate(records.records):
    record_box.insert(i,  f'{r.date:<11}{r.category:<30}{r.description:<21}{r.amount}')

bala_str = tk.StringVar()
bala_str.set('Now you have ' + str(records.balance) + ' dollars.')
bala_label = tk.Label(f, textvariable = bala_str)
bala_label.grid(row = 9, column = 0, columnspan = 3, sticky='W')
dele_btn = tk.Button(f, text = 'Delete', command = lambda: delete())
dele_btn.grid(row = 9, column = 3)

f.mainloop()

records.save()
 
'''while True:
    command = input('\nWhat do you want to do (add / view / delete / view categories / find / exit)? ')
    if command == 'add':
        record = input('Add an expense or income record with category, description, and amount (separate by spaces):\n')
        records.add(record, categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? ")
        records.delete(delete_record)
    elif command == 'view categories':
        categories.view(categories._categories, 0)
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category, categories._categories)
        records.find(target_categories, category)
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')'''


