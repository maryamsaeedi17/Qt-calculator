import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

global calc_status
calc_status="not finished"

def num_0():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() != "0":
        calculator_window.monitor.setText(calculator_window.monitor.text()+'0')
    calc_status="not finished"

def num_1():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() == "0":
        calculator_window.monitor.setText('1')
    else:
        calculator_window.monitor.setText(calculator_window.monitor.text()+'1')
    calc_status="not finished"
    
def num_2():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() == "0":
        calculator_window.monitor.setText('2')
    else:
        calculator_window.monitor.setText(calculator_window.monitor.text()+'2')
    calc_status="not finished"
    
def num_3():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() == "0":
        calculator_window.monitor.setText('3')
    else:
        calculator_window.monitor.setText(calculator_window.monitor.text()+'3')
    calc_status="not finished"
    
def num_4():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() == "0":
        calculator_window.monitor.setText('4')
    else:
        calculator_window.monitor.setText(calculator_window.monitor.text()+'4')
    calc_status="not finished"
    
def num_5():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() == "0":
        calculator_window.monitor.setText('5')
    else:
        calculator_window.monitor.setText(calculator_window.monitor.text()+'5')
    calc_status="not finished"
    
def num_6():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() == "0":
        calculator_window.monitor.setText('6')
    else:
        calculator_window.monitor.setText(calculator_window.monitor.text()+'6')
    calc_status="not finished"

    
def num_7():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() == "0":
        calculator_window.monitor.setText('7')
    else:
        calculator_window.monitor.setText(calculator_window.monitor.text()+'7')
    calc_status="not finished"

def num_8():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() == "0":
        calculator_window.monitor.setText('8')
    else:
        calculator_window.monitor.setText(calculator_window.monitor.text()+'8')
    calc_status="not finished"

def num_9():
    global calc_status
    if calc_status=="finished":
        calculator_window.monitor.setText("")

    if calculator_window.monitor.text() == "0":
        calculator_window.monitor.setText('9')
    else:
        calculator_window.monitor.setText(calculator_window.monitor.text()+'9')
    calc_status="not finished"

def dot():
    calculator_window.monitor.setText(calculator_window.monitor.text()+'.')



def sum():
    global a
    global oprt
    oprt = "sum"
    a = float(calculator_window.monitor.text())
    calculator_window.monitor.setText('')
    
def sub():
    global a
    global oprt
    oprt = "sub"
    a = float(calculator_window.monitor.text())
    calculator_window.monitor.setText('')
    
def mul():
    global a
    global oprt
    oprt = "mul"
    a = float(calculator_window.monitor.text())
    calculator_window.monitor.setText('')
    
def div():
    global a
    global oprt
    oprt = "div"
    a = float(calculator_window.monitor.text())
    calculator_window.monitor.setText('')
    
def clear_screen():
    calculator_window.monitor.setText('0')

def per():
    global calc_status
    calculator_window.monitor.setText(str(float(calculator_window.monitor.text())/100))
    calc_status="finished"

def sign():
    global calc_status
    calculator_window.monitor.setText(str(float(calculator_window.monitor.text())*(-1)))
    calc_status="finished"

def sin():
    global calc_status
    calculator_window.monitor.setText(str(math.sin(math.radians(float(calculator_window.monitor.text())))))
    calc_status="finished"

def cos():
    global calc_status
    calculator_window.monitor.setText(str(math.cos(math.radians(float(calculator_window.monitor.text())))))
    calc_status="finished"

def tan():
    global calc_status
    try:
        calculator_window.monitor.setText(str(math.tan(math.radians(float(calculator_window.monitor.text())))))
    except ZeroDivisionError:
        calculator_window.monitor.setText("Value Error!")
    calc_status="finished"

def cot():
    global calc_status
    try:
        calculator_window.monitor.setText(str(1/math.tan(math.radians(float(calculator_window.monitor.text())))))
    except ZeroDivisionError:
        calculator_window.monitor.setText("Value Error!")
    calc_status="finished"

def log():
    global calc_status
    calculator_window.monitor.setText(str(math.log(float(calculator_window.monitor.text()))))
    calc_status="finished"

def sqrt():
    global calc_status
    calculator_window.monitor.setText(str(math.sqrt(float(calculator_window.monitor.text()))))
    calc_status="finished"


def result():
    global calc_status

    b = float(calculator_window.monitor.text())

    if oprt == "sum":
        c = a+b
        calculator_window.monitor.setText(str(c))
    elif oprt == "sub":
        c = a-b
        calculator_window.monitor.setText(str(c))
    elif oprt == "mul":
        c = a*b
        calculator_window.monitor.setText(str(c))
    elif oprt == "div":
        try:
            c = a/b
            calculator_window.monitor.setText(str(c))
        except ZeroDivisionError:
            calculator_window.monitor.setText("Error! Division by zero!")
            calc_status="finished"

    calc_status="finished"

def backspace():
    text=calculator_window.monitor.text()
    text=text[:-1]
    calculator_window.monitor.setText(text)


    

    




my_calculator=QApplication([])

loader=QUiLoader()
calculator_window=loader.load("calculator-mainpage.ui")
calculator_window.show()


calculator_window.monitor.setText('0')

calculator_window.Button_0.clicked.connect(num_0)
calculator_window.Button_1.clicked.connect(num_1)
calculator_window.Button_2.clicked.connect(num_2)
calculator_window.Button_3.clicked.connect(num_3)
calculator_window.Button_4.clicked.connect(num_4)
calculator_window.Button_5.clicked.connect(num_5)
calculator_window.Button_6.clicked.connect(num_6)
calculator_window.Button_7.clicked.connect(num_7)
calculator_window.Button_8.clicked.connect(num_8)
calculator_window.Button_9.clicked.connect(num_9)

calculator_window.Button_dot.clicked.connect(dot)

calculator_window.Button_sum.clicked.connect(sum)
calculator_window.Button_sub.clicked.connect(sub)
calculator_window.Button_mul.clicked.connect(mul)
calculator_window.Button_div.clicked.connect(div)
calculator_window.Button_sin.clicked.connect(sin)
calculator_window.Button_cos.clicked.connect(cos)
calculator_window.Button_tan.clicked.connect(tan)
calculator_window.Button_cot.clicked.connect(cot)
calculator_window.Button_log.clicked.connect(log)
calculator_window.Button_sqrt.clicked.connect(sqrt)

calculator_window.Button_per.clicked.connect(per)
calculator_window.Button_sign.clicked.connect(sign)

calculator_window.Button_eq.clicked.connect(result)
calculator_window.Button_bs.clicked.connect(backspace)
calculator_window.Button_c.clicked.connect(clear_screen)








my_calculator.exec()