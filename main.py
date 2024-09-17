from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle
from layout_quizz import *
from data import *

app = QApplication([])

i = 0

window = QWidget()
window.resize(800, 700)
window.setWindowTitle("MemoryCard")
window.setLayout(main_line_quizz)
window.show()
shuffle(questions)
questions[i].show_question(lable1, rb1, rb2, rb3, rb4) 

def click_ok():
    global i
    if btn_ok.text() == "Відповісти":
        rbGroupBox.hide()
        ansGroupBox.show()
        btn_ok.setText("Наступне питання")
    else:
        rbGroupBox.show()
        ansGroupBox.hide()
        btn_ok.setText("Відповісти")
        i += 1
        questions[i].show_question(lable1, rb1, rb2, rb3, rb4)

btn_ok.clicked.connect(click_ok)

app.exec()




                                                
















