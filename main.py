import tkinter as tk
import manipulate
import format
from tkinter import ttk


#create GUI window
initWindow = tk.Tk()
initWindow.geometry('700x1000')

#Add explanatory labels, format the GUI
hello = tk.Label(text='Welcome to the FEA data manipulation program', height='4', justify='left', fg='red', bg='white', underline='2').pack()
inform = tk.Label(text='Use this program to properly format your txt file/s, then read, add to, and manipulate the coordinate data', justify='left').pack()
ttk.Separator(master=initWindow).pack(pady='5')

#First section, options for formatting of the txt file
pyformat = tk.Label(text='Format', height='2', fg='red', relief='raised', width='300', pady='10').pack()
ttk.Separator(master=initWindow).pack(pady='5')
#create label and add button to trigger the adding of delimiters
delimlabel=tk.Label(text='Add delimeters?')
delimbutton = tk.Button(text='Run add delimiters', width=17, height=3, bg='white', fg='black', command=format.delim).pack()
#create labels and button to trigger prepending function
elemLabel = tk.Label(text='Add element labels to new blank txt file?').pack()
elemlabelnote = tk.Label(text='Note: choose the orginal file first, then a blank file when prompted').pack()
elem = tk.Button(text='Run add element labels', width=17, height=3, bg='white', fg='black', command=format.addElem).pack()

#Next section - for the manipulation/alteration of the data
ttk.Separator(master=initWindow).pack(pady='5')
pyarray = tk.Label(text='Manipulate', height='2', fg='red', relief='raised', width='300', pady='10').pack()
ttk.Separator(master=initWindow).pack(pady='5')
arrLabel2 = tk.Label(text='Add extra columns to txt file?').pack()
arrLabel4 = tk.Label(text='What is the name of the new coordinate/column?').pack()
#Text box for user input, naming the new column. The name is passed as an argumemt to the addCol function in the manipulate module
col_name = tk.Entry()
col_name.pack()

arrButton2 = tk.Button(text='Add a colummn', width=17, height=3, fg='black', command=lambda: manipulate.addCol(col_name)).pack()
#label and button for triggering addArr function in manipulate module

arrLabel3 = tk.Label(text='How many columns are there in the txt file?').pack()
of_cols = tk.Entry(initWindow)
of_cols.pack()

arrLabel1 = tk.Label(text='Split file into coordinate arrays?').pack()
arrButton1 = tk.Button(text='Run create arrays', width=17, height=3, fg='black', command=lambda: manipulate.addArr(of_cols)).pack()

#loop GUI window until user exits
initWindow.mainloop()
