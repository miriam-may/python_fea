import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox

f1type=(('Text files', '*.txt'), ('All files', '*.*'))
ftype = (('Text files', '*.txt'), ('All files', '*.*'))

#function to add delimiters
def delim(): 

    #ask user to open a file, assign file to variable
    RESIDUAL_STRESS_TXT = fd.askopenfilename(title='open original file', initialdir='/', filetypes=f1type)

    #open a read-only file
    with open(RESIDUAL_STRESS_TXT, 'r') as magma_file:
        #read the selected file and apply it to variable elms
        elms = magma_file.read()
        #replace the applicable parts of variable elms with the delimiters
        elms = elms.replace('e+002', 'e+002, ')
        elms = elms.replace('e+003', 'e+003, ')
        elms = elms.replace('e+004', 'e+004, ')
        elms = elms.replace('e+005', 'e+005, ')
        elms = elms.replace('e+006', 'e+006, ')
        elms = elms.replace('e+007', 'e+007, ')
        elms = elms.replace('e+008', 'e+008, ')
        elms = elms.replace('e+009', 'e+009, ')
    #close the read-only file    
    magma_file.close()

    #open the same file as a writable
    with open(RESIDUAL_STRESS_TXT, 'w') as magma_file:
        #rewrite the entire file with the stored, altered text in variable elms
        magma_file.write(elms)
    #close the writeable file
    magma_file.close()

    #indicate to the user that the task is complete        
    p=tk.Label(text='Delimeter adding complete').pack()
            
    
    
#function to add the prefix elem n where n is the node number
def addElem():
    #create counting variables
    counter = 0
    linecount = 1

    #ask user to open the original file, assign file to variable
    RESIDUAL_STRESS_TXT = fd.askopenfilename(title='open original file', initialdir='/', filetypes=f1type)
 
    #ask user to open a second, blank file to write to
    RES_STRESS = fd.askopenfilename(title='open blank file', initialdir='/', filetypes=ftype)

    #open first file as readable
    with open(RESIDUAL_STRESS_TXT, 'r') as f:
            #open second file as writeable
        with open(RES_STRESS, 'w') as f2:
            #get all lines in a list
            checks=f.readlines()
            #get just first line with no trailing whitespace or newline
            checks1=checks[0].rstrip('\n')
            #check to see if the start of the file is formatted correctly
            if checks1.endswith('5'):
                #iterate through the lines in the file
                for line in checks:
                    counter+=1
                    
                    #skip every second (non-node) line
                    if counter % 2 == 0:
                        #write the correct prepend with an incrementing number
                        f2.write('Elem ' + str(linecount) + ' ' + line)
                        #incrememt the number
                        linecount += 1
                        
                    else:
                        #write the (non-node) line without prepend
                        f2.write(line)
                
                #tell user the task is complete    
                p = tk.Label(text="Appending complete").pack()
            else: 
                #If not, error message
                messagebox.showwarning('Incorrect Formatting', 'Don\'t forget to format the original file correctly. The first line should read "    1    5"')
                
        f2.close()
    f.close()







