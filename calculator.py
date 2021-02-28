from tkinter import *
import math

root = Tk()
root.title("Calculator")

entry = Entry(root, width=24)
entry.grid(row=0, column=0, columnspan=4)

# global variables for future use
count = 1
second_number_was = 0
sec_number = 0
f_num = 0
isNumWithMinus = False
IsThereCarka = False
# -----

def onClick(number):
  current_num = entry.get()
  entry.delete(0, END)
  entry.insert(0, str(current_num) + str(number))

def Negate():
  current_num = entry.get()
  global operator
  global isNumWithMinus
  operator = "+/-"

  if current_num[0] == "-":
    isNumWithMinus = True
  else:
    isNumWithMinus = False

  if operator == "+/-" and not(isNumWithMinus):
    numWithMinus = "-" + str(current_num)
    print(numWithMinus)
    entry.delete(0, END)
    entry.insert(0, numWithMinus)
    
  if operator == "+/-" and isNumWithMinus:
    entry.delete(0, END)
    numWithoutMinus = ""
    for char in current_num:
      if char == "-":
        continue
      numWithoutMinus += char 

    entry.insert(0, float(numWithoutMinus))
    print("neguju minus")

def Percent():
  global IsThereCarka
  current_num = entry.get()
  entry.delete(0, END)
  percentNum = "{:.6f}".format(float(current_num) / 100)
  entry.insert(0, percentNum)
  IsThereCarka = True

def Divide():
  first_num = entry.get()
  global f_num
  global operator
  operator = "/"
  f_num = float(first_num)
  entry.delete(0, END)

def Multiply():
  first_num = entry.get()
  global f_num
  global operator
  operator = "*"
  f_num = float(first_num)
  entry.delete(0, END)

def Subtract():
  first_num = entry.get()
  global f_num
  global operator
  operator = "-"
  f_num = float(first_num)
  entry.delete(0, END)

def Add():
  first_num = entry.get()
  global f_num
  global operator
  operator = "+"
  f_num = float(first_num)
  entry.delete(0, END)

def Carka():
  global IsThereCarka
  current_num = entry.get()
  IsNotDecimal = not IsThereCarka
  if IsNotDecimal:
    numWithCarka = current_num + "."
    IsThereCarka = True
    entry.delete(0, END)
    entry.insert(0, numWithCarka)

def Clear():
  global f_num
  global sec_number
  global count
  global operator

  f_num = ""
  sec_number = ""
  operator = "None"
  count = 1
  entry.delete(0, END)

def Equal():
  global f_num
  global second_number_was
  global count
  global operator
  global sec_number
  global IsThereCarka

  IsThereCarka = False

  sec_number = entry.get()

  if count == 1:
    second_number_was = sec_number

  entry.delete(0, END)

# Operator +
  if operator == "+":
    answer = "{:.2f}".format(f_num + float(second_number_was) * count)
    if answer.endswith("00"):
      answer = "{:.0f}".format(f_num + float(second_number_was) * count)
    entry.insert(0, answer)
    count += 1
    print("scitam")

# Operator -
  if operator == "-":
    answer = "{:.2f}".format(f_num - float(second_number_was) * count)
    entry.insert(0, answer)
    count += 1
    print("odcitam")

# Operator *
  if operator == "*":
    answer = "{:.2f}".format(f_num * pow(float(second_number_was), count))
    entry.insert(0, answer)
    count += 1
    print("nasobim")

# Operator /
  if operator == "/":
    answer = "{:.2f}".format(f_num / pow(float(second_number_was), count))
    entry.insert(0, answer)
    count += 1
    print("delim")

  if operator == "None":
    f_num = ""
    sec_number = ""
    entry.insert(0, "")


button0 = Button(root, text="0", width=8, height=2, command=lambda: onClick(0))
button1 = Button(root, text="1", width=2, height=2, command=lambda: onClick(1))
button2 = Button(root, text="2", width=2, height=2, command=lambda: onClick(2))
button3 = Button(root, text="3", width=2, height=2, command=lambda: onClick(3))
button4 = Button(root, text="4", width=2, height=2, command=lambda: onClick(4))
button5 = Button(root, text="5", width=2, height=2, command=lambda: onClick(5))
button6 = Button(root, text="6", width=2, height=2, command=lambda: onClick(6))
button7 = Button(root, text="7", width=2, height=2, command=lambda: onClick(7))
button8 = Button(root, text="8", width=2, height=2, command=lambda: onClick(8))
button9 = Button(root, text="9", width=2, height=2, command=lambda: onClick(9))

buttonClear = Button(root, text="C", width=2, height=2, command=Clear)
buttonNegate = Button(root, text="+/-", width=2, height=2, command=Negate)
buttonPercent = Button(root, text="%", width=2, height=2, command=Percent)
buttonDivide = Button(root, text="÷", width=2, height=2, command=Divide)
buttonMultiply = Button(root, text="×", width=2, height=2, command=Multiply)
buttonSubtract = Button(root, text="-", width=2, height=2, command=Subtract)
buttonAdd = Button(root, text="+", width=2, height=2, command=Add)
buttonCarka = Button(root, text=",", width=2, height=2, command=Carka)
buttonEqual = Button(root, text="=", width=2, height=2, command=Equal)

button0.grid(row=5, column=0, columnspan=2)
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

buttonClear.grid(row=1, column=0)
buttonNegate.grid(row=1, column=1)
buttonPercent.grid(row=1, column=2)
buttonDivide.grid(row=1, column=3)
buttonMultiply.grid(row=2, column=3)
buttonSubtract.grid(row=3, column=3)
buttonAdd.grid(row=4, column=3)
buttonCarka.grid(row=5, column=2)
buttonEqual.grid(row=5, column=3)

root.mainloop()
