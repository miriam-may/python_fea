# Data Manipulation Program for Finite Element Analysis 
## Version 1.0

This program is being created at the request of a relative who is a mechanical engineer in the field of finite element analysis. <br>
We have an initial .txt file with output from a piece of engineering software, showing nodes at different coordinates and the data on shear stresses at each coordinate.
It is desirable to be able to add new coordinate columns containing more data on each node - for example, the coolrate - which would be contained in a separate .txt file.
<br>
The program as it currently stands assumes a starting txt file with 6 columns (xx, yy, zz, xy, yz, xz) with scope to add an extra 5 columns.
<br><br>

## Features
*****
The initial task of the program is to format the .txt file. It needed to add comma delimiters between each coordinate, and add Elem *n* to the beginning of each node line, where *n* is an ascending number in increments of 1, starting at 1.
<br><br>
The output file only has nodes on every second line. The other lines contain 2 numbers that are used elsewhere in the engineering software's program. It was considered desirable to keep these lines.
<br><br>
The decision had to be made whether to make a massive 2 dimensional array to hold the nodes and coordinates in rows and columns, or one dimensional arraylists of nodes (where the coordinate is referenced by the index), or one dimensional arraylists of coordinates (where the node is referenced by the index).<br>
Because of the increased complexity of two dimensional arrays, I decided to create one dimensional arraylists, and because of the sheer number of nodes (over 6,000) I decided to create one dimensional arraylists of coordinate columns, with the nodes referenced as indices.<br>
The program also needed the ability to add new columns, taken from .txt files, and add them as new arraylists. Because of the difficulty of having multiple .txt files in play, I decided it would be best to get the program to write any new columns in hard form to the original .txt file.<br>
The choice to use arraylists as the data structure to hold the coordinates is not a final one - I only chose it because it is an inbuilt data type in Python, it is easy to search, and is mutable (in case changes needed to be made to the data later on). If the data structure needs to be changed later, that will be done as the situation arises.
<br><br>

## Problems
<hr>
The biggest problem I have found so far was the fact that you don't know how many columns may be needed - you may start with at few as 3 at the beginning, then may add many more on later. Dynamically creating variables based on user input is never a good idea as you lose control over the program.
Although this is where a 2 dimensional array could have been handy (as it could have handled all user input in a single variable), I wanted to avoid having one monster-sized 2 dimensional array, as it would quickly become unmanagable.<br>
Considering that there will most likely be an upper limit of columns, I created a Class called Coordinate with attributes that could be changed by user input - the name and data attributes. That way, I could declare all possible class instances before runtime and maintain control, but the user had all the functionality they need.<br>
To handle the uncertainty of how many columns there would be, I just created variables that would change depending on how many columns were in play, with the user telling the program via a textbox how many columns were being used.
<br><br>
Another problem is that the engineer in question is having difficulty deciding what else he needs the program to do. This means there is little progress to make whilst there is no direction on what the program is supposed to do. At the moment, it just formats txt files and reads data into arraylists.
<br><br>
Another problem involves the fact that the the first arraylist, xx, will always have an extra "elem <i>n</i>" preceding each piece of relevant data. I have had no communication from the engineer about whether this is desirable for identification purposes or whether it should be stripped from the arraylist upon creation.
<br><br> 


## Technology used
<hr>

The following technologies were used:
- The IDE used was [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3](https://www.python.org/) was the language used
- [Tkinter](https://docs.python.org/3/library/tkinter.html) was used to create the Graphical User Interface (GUI)