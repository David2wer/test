from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint


app = QApplication([])


w = QWidget()
w.setWindowTitle("Лотерея")
w.move(100, 100)
w.resize(400, 200)

button = QPushButton("Випробувати удачу")
button1 = QPushButton("Випробувати удачу 10 разів")
text = QLabel("Натисни щоб взяти участь")
winner = QLabel("?")
winner1 = QLabel("?")
winner2 = QLabel("?")

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(winner1, alignment = Qt.AlignCenter)
line.addWidget(winner2, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
line.addWidget(button1, alignment = Qt.AlignCenter)
w.setLayout(line)
class Cazino():
    def __init__(self):
        self.money = 100
    def cazino(self):
        number = randint(1,10)
        number1 = randint(1,10)
        number2 = randint(1,10)
        winner.setText(str(number))
        winner1.setText(str(number1))
        winner2.setText(str(number2))
        if number == number1 or number2 == number1 or number == number2:
            if number == number1 and number2 == number1 :
                self.money += 100
            else:
                text.setText("Ви виграли джекпот! Зіграйте знову" + str( self.money))
                self.money += 5
                text.setText("Ви виграли! Зіграйте знову" + str( self.money))
        else:
            self.money -= 3
            text.setText("Ви програли! Зіграйте знову" + str( self.money))
    def tap(self):
        for i in range(10):
            self.cazino()
            
        



cazikon = Cazino()
button.clicked.connect(cazikon.cazino)
button1.clicked.connect(cazikon.tap)
w.show()
app.exec_()

