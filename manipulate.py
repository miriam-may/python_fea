from tkinter import filedialog as fd1
import copy
import decimal
import dearpygui.dearpygui as dpg

ftype=(('Text files', '*.txt'), ('All files', '*.*'))

#create Coordinate class

class Coordinate():
    def __init__(self, coordinate_name: str, values: list): 
        self.coordinate_name = coordinate_name
        self.values = values

    def __repr__(self):
        if self.coordinate_name is None:
            self.coordinate_name = "Unnamed_coordinate"
        else:
            self.coordinate_name =f"{self.coordinate_name}"
        return(f"Coordinate name={self.coordinate_name}, ",f"values = {self.values}, ")

    def formatNumbers(self):
        temp_list = []
        for node in self.values:
            temp_node = decimal.Decimal(node)
            temp_list.append(temp_node)
        self.values.clear()
        for node in temp_list:
            self.values.append(node)
        print(self.values[0])


#create list variables for known coordinates, and placeholder variables for unknown coordinate
#instances of the Coordinate class

colxx = []
colyy = []
colzz = []
colxy = []
colyz = []
colxz = []

list_filler = []

#create instances of coordinate class
coordxx = Coordinate('xx', colxx)
coordyy = Coordinate('yy', colyy)
coordzz = Coordinate('zz', colzz)
coordxy = Coordinate('xy', colxy)
coordyz = Coordinate('yz', colyz)
coordxz = Coordinate('xz', colxz)

#create more empty instances, to be used as needed
seven_coord = Coordinate('xxx', copy.deepcopy(list_filler))
eight_coord = Coordinate('yyy', copy.deepcopy(list_filler))
nine_coord = Coordinate('zzz', copy.deepcopy(list_filler))
ten_coord = Coordinate('xxy', copy.deepcopy(list_filler))
eleven_coord = Coordinate('yyz', copy.deepcopy(list_filler))

counter = 0

def clearError():
    dpg.delete_item("error", children_only=False)

def clear():
    dpg.delete_item("success", children_only=False)

def addCol(col_name):

    RESIDUAL_STRESS_TXT = fd1.askopenfilename(title='open original file', initialdir='/', filetypes=ftype)
    NEW_COLUMN_TXT = fd1.askopenfilename(title='open txt file with new column', initialdir='/', filetypes=ftype)
    next_col_name = col_name.get()
    current_col = Coordinate('', [])
    global counter
    counter += 1
    if counter == 1:
        current_col = seven_coord
    elif counter == 2:
        current_col = eight_coord
    elif counter == 3:
        cuurent_col = nine_coord
    elif counter == 4:
        current_col = ten_coord
    elif counter == 5:
        current_col = eleven_coord
    else:
        #return False
        with dpg.window(label="Error", tag="error"):
            dpg.add_text("There are no empty column variables available. Please exit the program and inform support.")
            dpg.add_button(label="Clear", callback=clearError)
       

    #name the column with the user input from main module
    current_col.coordinate_name=next_col_name    

    #split the txt file into individual lines (as arraylists)
    with open(RESIDUAL_STRESS_TXT, 'r') as orig:
            fin = orig.read().splitlines()
    orig.close()

    #reopen the txt file, and open the txt file with the new columns
    #turn the new column into the text file into an array
    #then write the data of the new column onto the end of every node 
    #line until there are no lines in the new column left
    with open(RESIDUAL_STRESS_TXT, 'w') as newOriginal:
        with open(NEW_COLUMN_TXT, 'r') as newCol:
            i=0
            newCol_lines = newCol.readlines()
            for line in fin:
                if i < len(newCol_lines):
                    if line.__contains__('e+00'):
                        newOriginal.write(line + str(newCol_lines[i]).rstrip('\n') + ',' '\n')
                        i+=1
                    else:
                        newOriginal.write(line + '\n')
                else:
                    newOriginal.write(line + '\n')
            current_col.values=newCol_lines
        newCol.close()
    newOriginal.close()

    #This is for the benefit of the programmer, to check everything has worked correctly
    print(seven_coord.values[0])
    print(next_col_name)

    #inform the use that the program has run successfully
    with dpg.window(label="Result", tag="success"):
        dpg.add_text("Column added")
        dpg.add_button(label="Clear", callback=clear)
    
    
    

def addArray(of_cols):

    #create variable to indicate to program which values belong in which columns
    num_of_cols=of_cols.get()


    #ask user to open a file
    RESIDUAL_STRESS_TXT = fd1.askopenfilename(title='open original file', initialdir='/', filetypes=ftype)

    #open file as read and write
    with open(RESIDUAL_STRESS_TXT, 'r+') as array_adder:

        #read the fill to a variable
        adder=array_adder.read()

        #create an array of values separated by the commas found in the txt file
        elmarr = adder.split(',')
        
        #make sure that the user has entered a value in the text box
        if not num_of_cols:
            with dpg.window(label="Error", tag="error"):
                dpg.add_text("Please enter a value in the input box")
                dpg.add_button(label="Clear", callback=clearError)
           

        #make sure the user has enetered only a whole numercial value
        try:
            int(num_of_cols)
        except ValueError:
            with dpg.window(label="Error", tag="error"):
                dpg.add_text("Please enter only a whole number")
                dpg.add_button(label="Clear", callback=clearError)
            
        else: 
            x=int(num_of_cols)-(int(num_of_cols)-1)
            countxx=int(num_of_cols)
            countyy=int(num_of_cols)-x
            countzz=int(num_of_cols)-(x+1)
            countxy=int(num_of_cols)-(x+2)
            countyz=int(num_of_cols)-(x+3)
            countxz=int(num_of_cols)-(x+4)
            countseven=int(num_of_cols)-(x+5)
            counteight=int(num_of_cols)-(x+6)
            countnine=int(num_of_cols)-(x+7)
            countten=int(num_of_cols)-(x+8)
            counteleven=int(num_of_cols)-(x+9)
            #iterate through the array
            for item in elmarr:
                #take the first value, then every sixth one after that...
                if countxx % int(num_of_cols) == 0:
                    #... and append it to the xx coordinate object values list. Do the same for all other columns
                    coordxx.values.append(item.strip())
                if countyy % int(num_of_cols) == 0:
                    coordyy.values.append(item.strip())
                if countzz % int(num_of_cols) == 0:
                    coordzz.values.append(item.strip())
                if countxy % int(num_of_cols) == 0:
                    coordxy.values.append(item.strip())
                if countyz % int(num_of_cols) == 0:
                    coordyz.values.append(item.strip())
                if countxz % int(num_of_cols) == 0:
                    coordxz.values.append(item.strip())
                if int(num_of_cols) >= 7:
                    if countseven % int(num_of_cols) == 0:
                        seven_coord.values.append(item.strip())
                if int(num_of_cols) >= 8:
                    if counteight % int(num_of_cols) == 0:
                        eight_coord.values.append(item.strip())
                if int(num_of_cols) >= 9:
                    if countnine % int(num_of_cols) == 0:
                        nine_coord.values.append(item.strip())
                if int(num_of_cols) >= 10:
                    if countten % int(num_of_cols) == 0:
                        ten_coord.values.append(item.strip())
                if int(num_of_cols) >= 11:
                    if counteleven % int(num_of_cols) == 0:
                        eleven_coord.values.append(item.strip())
                countxx+=1
                countyy+=1
                countzz+=1
                countxy+=1
                countyz+=1
                countxz+=1
                countseven+=1
                counteight+=1
                countnine+=1
                countten+=1
                counteleven+=1
            
    #close the file        
    array_adder.close()

    #remove the extra string values from coordinate xx
    temp_coordxx = []
    line_number = 1

    for node in coordxx.values:
        if node.find('\n')!=-1:
            string_to_delete = "Elem " + str(line_number) 
            node = node[node.index('\n')+1:]
            node = node.lstrip(string_to_delete)
            line_number+=1
        temp_coordxx.append(node)

    coordxx.values.clear()

    for item in temp_coordxx:
        coordxx.values.append(item)
            
    #This is for the benefit of the programmer, to check everything has worked correctly
    print(coordxx.values[1])
    coordxx.formatNumbers()

    #tell the user the arrays have been created
    with dpg.window(label="Result", tag="success"):
        dpg.add_text("Arrays created.")
        dpg.add_button(label="Clear", callback=clear)
