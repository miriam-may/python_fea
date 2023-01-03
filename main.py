import manipulate
import format
import dearpygui.dearpygui as dpg


def dearpg():
    dpg.create_context()
    dpg.create_viewport()
    dpg.setup_dearpygui()

    with dpg.window(label = "Tensor output data manipulation", tag="mw"):
        dpg.add_text("Format, manipulate and display data from tensor output files that have been saved as .txt files")
        dpg.add_text("Run formatting - add delimeters and number each Elem")
        dpg.add_button(label = "Add delimeters", callback = format.delimiters)
        
        dpg.add_button(label = "Number Elements", callback = format.addElem)      
           
        dpg.add_text("Add extra column to .txt file")
        col = dpg.add_input_text(label = "Enter name of new column")
        colname = dpg.get_value(col)
        dpg.add_button(label = "Add the column", callback = lambda:manipulate.addCol(colname))
        
        dpg.add_text("How many columns are there in the .txt file currently, including any recently added?")
        of_cols = dpg.add_input_int(label = "Number of columns")
        number_of_cols = dpg.get_value(of_cols)
        dpg.add_button(label = "Create coordinate arrays", callback = lambda:manipulate.addArray(number_of_cols))
        

        with dpg.plot(label = "Data plot", query = True, height = 500, width = 500):
            dpg.add_plot_legend()
            dpg.add_plot_axis(dpg.mvXAxis, label = "x")
            dpg.add_plot_axis(dpg.mvYAxis, label = "y", tag = "y_axis")


    dpg.show_style_editor()

    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


dearpg()
