from tkinter import *
from tkinter import filedialog
import re

# Create the window set up information
root = Tk()
root.title("Compare text")
root.configure(width=1420, height=500)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Create the main viewable frame in the app
mainFrame = Frame(root)
mainFrame.grid(row=0, column=0, sticky='news')

# Create multiline text fields
textInputField1 = Text(mainFrame, bd=4)
textInputField2 = Text(mainFrame, bd=4)

# Create the frame for the button
buttonFrame = Frame(mainFrame)

def clickCompare():
    arrayInput1 = []
    arrayInput2 = []
    for line in textInputField1.get('1.0', END).splitlines():
        arrayInput1.append(line)
    for line in textInputField2.get('1.0', END).splitlines():
        arrayInput2.append(line)
    for element in range(len(arrayInput1)):
        num = element + 1.0
        if element >= len(arrayInput2):
            maxInput1 = float(str(element + 1) + '.' + str(len(arrayInput1[element])))
            textInputField1.tag_add("Error", num, maxInput1)
        if arrayInput1[element] != arrayInput2[element]:
            maxInput1 = float(str(element + 1) + '.' + str(len(arrayInput1[element])))
            maxInput2 = float(str(element + 1) + '.' + str(len(arrayInput2[element])))
            textInputField1.tag_add("Error", num, maxInput1)
            textInputField2.tag_add("Error", num, maxInput2)
        if (element + 1 == len(arrayInput1)) and (element + 1 < len(arrayInput2)):
            for x in range(element + 1, len(arrayInput2)):
                num = x + 1.0
                maxInput2 = float(str(x + 1) + '.' + str(len(arrayInput2[x])))
                textInputField2.tag_add("Error", num, maxInput2)

        textInputField1.tag_config("Error", background="red")
        textInputField2.tag_config("Error", background="red")

def cleantl():
    textInputField2.delete("1.0", END)
    sremoved = re.sub(r"\s+", " ", textInputField1.get("1.0", END))
    #Add more functionality to take out reactions from text
    finaltext = sremoved.replace('[', '\n').replace(']', '').replace('AM', 'AM -').replace('PM', 'PM -').replace('Edited', '').replace('(1 liked)', '').replace('(2 liked)', '').replace('(3 liked)', '').replace('(4 liked)', '').replace('(5 liked)', '').replace('(6 liked)', '').replace('(7 liked)', '').replace('(8 liked)', '').replace('(9 liked)', '')
    textInputField2.insert(INSERT, finaltext)

def uploadLeft():
    file_path = filedialog.askopenfilename()
    textInputField1.delete("1.0", END)
    textInputField1.insert(INSERT, open(file_path, "r").read())

def uploadRight():
    file_path = filedialog.askopenfilename()
    textInputField2.delete("1.0", END)
    textInputField2.insert(INSERT, open(file_path, "r").read())

compareText = Button(buttonFrame, text="Compare", command=clickCompare)
uploadFileLeft = Button(buttonFrame, text="Upload to Left Side", command=uploadLeft)
uploadFileRight = Button(buttonFrame, text="Upload to Right Side", command=uploadRight)
teamsCleanup = Button(buttonFrame, text="Cleanup Teams Chat", command=cleantl)

textInputField1.grid(row=0, column=0, sticky='news')
textInputField2.grid(row=0, column=1, sticky='news')
buttonFrame.grid(row=1, column=0)
uploadFileLeft.grid(row=0, column=0)
uploadFileRight.grid(row=0, column=1)
compareText.grid(row=0, column=2)
teamsCleanup.grid(row=0, column=3)

mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=1)
mainFrame.rowconfigure(0, weight=1)

root.mainloop()
