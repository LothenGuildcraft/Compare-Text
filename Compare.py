from tkinter import *
from tkinter import filedialog
import re

root = Tk()
root.title("Compare text")
root.geometry('1420x500')

frame = Frame(root)

# Can create multiLine comments
input1 = Text(root, width=100, height=35)
input2 = Text(root, width=100, height=35)

def clickCompare():
    arrayInput1 = []
    arrayInput2 = []
    for line in input1.get('1.0', END).splitlines():
        arrayInput1.append(line)
    for line in input2.get('1.0', END).splitlines():
        arrayInput2.append(line)
    for element in range(len(arrayInput1)):
        num = element + 1.0
        if element >= len(arrayInput2):
            maxInput1 = float(str(element + 1) + '.' + str(len(arrayInput1[element])))
            input1.tag_add("Error", num, maxInput1)
        elif arrayInput1[element] != arrayInput2[element]:
            maxInput1 = float(str(element + 1) + '.' + str(len(arrayInput1[element])))
            maxInput2 = float(str(element + 1) + '.' + str(len(arrayInput2[element])))
            input1.tag_add("Error", num, maxInput1)
            input2.tag_add("Error", num, maxInput2)
        elif (element + 1 == len(arrayInput1)) and (element + 1 < len(arrayInput2)):
            for x in range(element + 1, len(arrayInput2)):
                num = x + 1.0
                maxInput2 = float(str(x + 1) + '.' + str(len(arrayInput2[x])))
                input2.tag_add("Error", num, maxInput2)

        input1.tag_config("Error", background="red")
        input2.tag_config("Error", background="red")

def cleantl():
    input2.delete("1.0", END)
    #Start of modified version of Yury's code
    sremoved = re.sub(r"\s+", " ", input1.get("1.0", END))
    finaltext = sremoved.replace('[', '\n').replace(']', '').replace('AM', 'AM -').replace('PM', 'PM -').replace('Edited', '').replace('(1 liked)', '').replace('(2 liked)', '').replace('(3 liked)', '').replace('(4 liked)', '').replace('(5 liked)', '').replace('(6 liked)', '').replace('(7 liked)', '').replace('(8 liked)', '').replace('(9 liked)', '')
    #End of modified version of Yury's code
    input2.insert(INSERT, finaltext)

def uploadLeft():
    file_path = filedialog.askopenfilename()
    input1.delete("1.0", END)
    input1.insert(INSERT, open(file_path, "r").read())

def uploadRight():
    file_path = filedialog.askopenfilename()
    input2.delete("1.0", END)
    input2.insert(INSERT, open(file_path, "r").read())

compareText = Button(frame, text="Compare", command=clickCompare)
uploadFileLeft = Button(frame, text="Upload to Left Side", command=uploadLeft)
uploadFileRight = Button(frame, text="Upload to Right Side", command=uploadRight)
teamsCleanup = Button(frame, text="Cleanup Teams Chat", command=cleantl)

input1.grid(row=0, column=0)
input2.grid(row=0, column=1)
frame.grid(row=1, column=0)
uploadFileLeft.grid(row=0, column=0)
uploadFileRight.grid(row=0, column=1)
compareText.grid(row=0, column=2)
teamsCleanup.grid(row=0, column=3)

root.mainloop()
