# Modes of file opening
#  r  = to rad data
#  w  = write data
#  a  = append data to the file
#  r+ = to rad and write data of a file
#  W+ = to write  and read data into a file
#  a+ = to append and read data of a file
#  x  = to open the file exclusive creation mode

file=open("MyData1 ",'a')
file.write("how are you \n ")
file.write("What is your name \n")

file.close