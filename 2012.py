from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox

def win():
    text_win = QMessageBox()
    text_win.setText("Правильно! Ви виграли гіроскутер")
    text_win.exec_()

def lose():
    text_win = QMessageBox()
    text_win.setText("Ні, в 2015 році. Ви виграли фірмовий плакат")
    text_win.exec_()
    




app = QApplication([])

w = QWidget()
w.setWindowTitle("Конкурс від Crazy People")
w.resize(400, 200)

question = QLabel("В якому році канал отримав золоту кнопку від YouTube?")
btn_answer1 = QRadioButton("2005")
btn_answer2 = QRadioButton("2010")
btn_answer3 = QRadioButton("2015")
btn_answer4 = QRadioButton("2020")

layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2= QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
w.setLayout(layout_main)


btn_answer1.clicked.connect(win)
btn_answer2.clicked.connect(lose)
btn_answer3.clicked.connect(lose)
btn_answer4.clicked.connect(lose)

w.show()
app.exec_()