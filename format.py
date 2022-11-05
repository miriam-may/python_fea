import dearpygui.dearpygui as dpg


dpg.create_context()
f1type=(('Text files', '*.txt'), ('All files', '*.*'))
ftype = (('Text files', '*.txt'), ('All files', '*.*'))

file_one = ""
file_two = ""

def clearError():
    dpg.delete_item("error", children_only=False)

def clear():
    dpg.delete_item("success", children_only=False)

def clear_child():
    dpg.delete_item("success_child", children_only=False)

def clearError_child():
    dpg.delete_item("error_child", children_only=False)

#function to add delimiters
def delim(): 
    def callback(sender, app_data):
        print(sender)
        print(app_data)
        with open(app_data['file_path_name'], 'r') as magma_file:
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

        with open(app_data['file_path_name'], 'w') as magma_file:
            #rewrite the entire file with the stored, altered text in variable elms
            magma_file.write(elms)
        #close the writeable file
        magma_file.close()
        with dpg.window(label="Result", tag="success_child"):
            dpg.add_text("Delimeter adding complete")
            dpg.add_button(label="Clear", callback=clear_child)

        

    #ask user to open a file, assign file to variable
    #RESIDUAL_STRESS_TXT = fd.askopenfilename(title='open original file', initialdir='/', filetypes=f1type)
    with dpg.file_dialog(directory_selector=False, show=False, callback=callback, id="file_dialog_id"):
        dpg.add_file_extension(".txt")
        dpg.add_file_extension("", color=(150, 255, 150, 255))
    
    with dpg.window(label="File opener", tag="success", width=400, height=300):
        dpg.add_button(label="Select files", callback=lambda: dpg.show_item("file_dialog_id"))
        dpg.add_button(label="Clear window", callback=clear)
        
   
    
            
    
    
#function to add the prefix elem n where n is the node number
def addElem():

    def callback(sender, file_data):

        print(file_data)
        #create counting variables
        counter = 0
        linecount = 1

        with open(file_data['file_path_name'], 'r') as f:
            #get all lines in a list
            checks=f.readlines()
            #get just first line with no trailing whitespace or newline
            checks1=checks[0].rstrip('\n')

        f.close()

        with open(file_data['file_path_name'], 'w') as f2:
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
                    with dpg.window(label="Result", tag="success_child", pos=[100, 50]):
                        dpg.add_text("Appending complete")
                        dpg.add_button(label="Clear", callback=clear_child)

                    
    
               
                else: 
                    with dpg.window(label="Error", tag="error_child"):
                        dpg.add_text("Don\'t forget to format the original file correctly. The first line should read '    1    5'", parent="aw")
                        dpg.add_button(label="Clear", callback=clearError_child)


               
        f2.close()       
                 
        

    with dpg.file_dialog(directory_selector=False, show=False, file_count=1, callback=callback, id="file_dialog_id"):
        dpg.add_file_extension(".txt")
        dpg.add_file_extension("", color=(150, 255, 150, 255))
    
    with dpg.window(label="File opener", tag="success", width=400, height=300):
        dpg.add_button(label="Select files", callback=lambda: dpg.show_item("file_dialog_id"))
        dpg.add_button(label="Clear window", callback=clear)







