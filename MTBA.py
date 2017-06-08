# Ярцев Денис P3175
# 2017
# Программа, которая переписывает введённый текст большими буквами
# версия 1.0
# поддерживает круглые скобки и арифметические знаки
# не поддерживает нижний регистр латиницы и всю кириллицу

import sys
from PyQt5 import QtCore, QtGui,  QtWidgets
from PyQt5.QtGui import QIcon, QFont

letters = \
    {
        'a':
            [
                "  AAA  ",
                " AA AA ",
                "AA   AA",
                "AA   AA",
                "AAAAAAA",
                "AA   AA",
                "AA   AA"
            ],
        'b':
            [
                "BBBBBB ",
                "BB   BB",
                "BB   BB",
                "BBBBBB ",
                "BB   BB",
                "BB   BB",
                "BBBBBB "
            ],
        'c':
            [
                " CCCCC ",
                "CC   CC",
                "CC     ",
                "CC     ",
                "CC     ",
                "CC   CC",
                " CCCCC "
            ],
        'd':
            [
                "DDDDDD ",
                "DD   DD",
                "DD    D",
                "DD    D",
                "DD    D",
                "DD   DD",
                "DDDDDD "
            ],
        'e':
            [
                "EEEEEEE",
                "EE     ",
                "EE     ",
                "EEEEE  ",
                "EE     ",
                "EE     ",
                "EEEEEEE"
            ],
        'f':
            [
                "FFFFFFF",
                "FF    F",
                "FF     ",
                "FFFF   ",
                "FF     ",
                "FF     ",
                "FF     "
            ],
        'g':
            [
                " GGGGG ",
                "GG    G",
                "GG     ",
                "GG     ",
                "GG GGGG",
                "GG   GG",
                " GGGGG "
            ],
        'h':
            [
                "HH   HH",
                "HH   HH",
                "HH   HH",
                "HHHHHHH",
                "HH   HH",
                "HH   HH",
                "HH   HH"
            ],
        'i':
            [
                "IIIIIII",
                "   I   ",
                "   I   ",
                "   I   ",
                "   I   ",
                "   I   ",
                "IIIIIII"
            ],
        'j':
            [
                "JJJJJJJ",
                "     JJ",
                "     JJ",
                "     JJ",
                "J    JJ",
                "JJ   JJ",
                " JJJJJ "
            ],
        'k':
            [
                "KK   KK",
                "KK  KK ",
                "KK KK  ",
                "KKKK   ",
                "KK KK  ",
                "KK  KK ",
                "KK   KK"
            ],
        'l':
            [
                "LL     ",
                "LL     ",
                "LL     ",
                "LL     ",
                "LL    L",
                "LL    L",
                "LLLLLLL"
            ],
        'm':
            [
                "MM   MM",
                "MM   MM",
                "M M M M",
                "M  M  M",
                "M     M",
                "M     M",
                "M     M"
            ],
        'n':
            [
                "NN   NN",
                "NN   NN",
                "NNN  NN",
                "NN N NN",
                "NN  NNN",
                "NN   NN",
                "NN   NN"
            ],
        'o':
            [
                " OOOOO ",
                "OO   OO",
                "OO   OO",
                "OO   OO",
                "OO   OO",
                "OO   OO",
                " OOOOO "
            ],
        'p':
            [
                "PPPPPP ",
                "PP   PP",
                "PP   PP",
                "PPPPPP ",
                "PP     ",
                "PP     ",
                "PP     "
            ],
        'q':
            [
                " QQQQQ ",
                "QQ   QQ",
                "QQ   QQ",
                "QQ   QQ",
                "QQ   QQ",
                " QQQQQ ",
                "   QQQQ"
            ],
        'r':
            [
                "RRRRRR ",
                "RR   RR",
                "RR   RR",
                "RRRRRR ",
                "RR  RR ",
                "RR  RR ",
                "RR   RR"
            ],
        's':
            [
                " SSSSS ",
                "SS    S",
                "SS     ",
                " SSSSS ",
                "     SS",
                "S    SS",
                " SSSSS "
            ],
        't':
            [
                "TTTTTTT",
                "T  T  T",
                "   T   ",
                "   T   ",
                "   T   ",
                "   T   ",
                "  TTT  "
            ],
        'u':
            [
                "UU   UU",
                "UU   UU",
                "UU   UU",
                "UU   UU",
                "UU   UU",
                "UU   UU",
                " UUUUU "
            ],
        'v':
            [
                "VV   VV",
                "VV   VV",
                "VV   VV",
                "VV   VV",
                " VV VV ",
                "  V V  ",
                "   V   "
            ],
        'w':
            [
                "W     W",
                "W     W",
                "W     W",
                "W  W  W",
                "W W W W",
                "WW   WW",
                "W     W"
            ],
        'x':
            [
                "XX   XX",
                "XX   XX",
                " XX XX ",
                "   X   ",
                " XX XX ",
                "XX   XX",
                "XX   XX"
            ],
        'y':
            [
                "YY   YY",
                "YY   YY",
                " YY YY ",
                "  Y Y  ",
                "   Y   ",
                "   Y   ",
                "  YYY  "
            ],
        'z':
            [
                "ZZZZZZZ",
                "Z    ZZ",
                "    ZZ ",
                "   ZZ  ",
                "  ZZ   ",
                " ZZ   Z",
                "ZZZZZZZ"
            ],
        ' ':
            [
                "       ",
                "       ",
                "       ",
                "       ",
                "       ",
                "       ",
                "       "
            ],
        '1':
            [
                "   11  ",
                "  111  ",
                " 1 11  ",
                "   11  ",
                "   11  ",
                "   11  ",
                " 111111"
            ],
        '2':
            [
                " 22222 ",
                "22   22",
                "     22",
                "    22 ",
                "  22   ",
                " 22   2",
                "2222222"
            ],
        '3':
            [
                " 33333 ",
                "33   33",
                "    33 ",
                "   33  ",
                "     33",
                "33  333",
                " 33333 "
            ],
        '4':
            [
                "    44 ",
                "  4444 ",
                " 44 44 ",
                "44  44 ",
                "4444444",
                "    44 ",
                "    44 "
            ],
        '5':
            [
                "5555555",
                "55    5",
                "55     ",
                "555555 ",
                "     55",
                "55   55",
                " 55555 "
            ],
        '6':
            [
                " 66666 ",
                "66    6",
                "66     ",
                "666666 ",
                "66   66",
                "66   66",
                " 66666 "
            ],
        '7':
            [
                "7777777",
                "7    77",
                "    77 ",
                "   77  ",
                "  77   ",
                "  77   ",
                "  77   "
            ],
        '8':
            [
                " 88888 ",
                "88   88",
                "88   88",
                " 88888 ",
                "88   88",
                "88   88",
                " 88888 "
            ],
        '9':
            [
                " 99999 ",
                "99   99",
                "99   99",
                " 999999",
                "     99",
                "9    99",
                " 99999"
            ],
        '0':
            [
                " 00000 ",
                "00   00",
                "00  000",
                "00 0 00",
                "000  00",
                "00   00",
                " 00000 "
            ],
        '-':
            [
                "       ",
                "       ",
                "       ",
                "-------",
                "       ",
                "       ",
                "       "
            ],
        '+':
            [
                "       ",
                "   +   ",
                "   +   ",
                "+++++++",
                "   +   ",
                "   +   ",
                "       "
            ],
        '=':
            [
                "       ",
                "       ",
                "=======",
                "       ",
                "=======",
                "       ",
                "       "
            ],
        '*':
            [
                "       ",
                "**   **",
                " ** ** ",
                "   *   ",
                " ** ** ",
                "**   **",
                "       "
            ],
        '/':
            [
                "       ",
                "   /   ",
                "       ",
                "///////",
                "       ",
                "   /   ",
                "       "
            ],
        '.':
            [
                "       ",
                "       ",
                "       ",
                "       ",
                "       ",
                " ..    ",
                " ..    "
            ],
        ',':
            [
                "       ",
                "       ",
                "       ",
                "       ",
                "       ",
                " ,,    ",
                "  ,    "
            ],
        '(':
            [
                "     ((",
                "    (( ",
                "   ((  ",
                "   ((  ",
                "   ((  ",
                "    (( ",
                "     (("
            ],
        ')':
            [
                "))     ",
                " ))    ",
                "  ))   ",
                "  ))   ",
                "  ))   ",
                " ))    ",
                "))     "
            ],
        '!':
            [
                "   !   ",
                "   !   ",
                "   !   ",
                "   !   ",
                "   !   ",
                "       ",
                "   !   "
            ],
        '?':
            [
                "  ???  ",
                " ?   ? ",
                " ?   ? ",
                "    ?  ",
                "   ?   ",
                "       ",
                "   ?   "
            ],
        '<':
            [
                "       ",
                "     <<",
                "  <<<  ",
                "<<     ",
                "  <<<  ",
                "     <<",
                "       "
            ],
        '>':
            [
                "       ",
                ">>     ",
                "  >>>  ",
                "     >>",
                "  >>>  ",
                ">>     ",
                "       "
            ]
        }


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.move(100, 100)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle('Make It Bigger')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.setFixedSize(1500, 360)
        self.setFont(QFont("Courier", 16))

        self.inBox = QtWidgets.QLineEdit(self)
        self.inBox.setPlaceholderText("You can write here")
        self.inBox.move(190, 20)
        self.inBox.resize(350, 50)

        self.outBox = QtWidgets.QTextEdit(self)
        self.outBox.setPlaceholderText("Your text will appear here")
        self.outBox.move(20, 90)
        self.outBox.resize(1460, 250)

        self.transform = QtWidgets.QPushButton('Transform', self)
        self.transform.setGeometry(560, 20, 200, 50)
        self.transform.clicked.connect(self.transformClicked)

        self.open = QtWidgets.QPushButton('Import', self)
        self.open.setGeometry(20, 20, 150, 50)
        self.open.clicked.connect(self.openClicked)

        self.save = QtWidgets.QPushButton('Save', self)
        self.save.setGeometry(1380, 20, 100, 50)
        self.save.clicked.connect(self.saveClicked)

        self.show()


    def transformClicked(self):
        textContent = self.inBox.text().lower()
        self.outputContent = ""
        self.outBox.setText("")

        if len(textContent)>11:
            textContent = ""
            buttonReply = QtWidgets.QMessageBox.question(self, 'Error!', "Too long!",
                                                         QtWidgets.QMessageBox.Close)

        try:
            for j in range(7):
                for i in textContent:
                    self.outputContent += letters[i][j] + " "
                self.outputContent += '\n'
        except LookupError:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Error!', "Wrong Symbol",
                                                         QtWidgets.QMessageBox.Close)
        except TypeError:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Error!', "Type Error",
                                                         QtWidgets.QMessageBox.Close)
        self.outBox.setText(self.outputContent)

    def saveClicked(self):
        try:
            file = open('output.txt', 'w')
            file.write(self.outputContent)
            file.close()
        except Exception:
            file.close()

    def openClicked(self):
        output = ""
        try:
            file = open('output.txt', 'r')
            for line in file.readlines():
                output += line
            self.outBox.setText(output)
        except FileNotFoundError:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Error', "File \"output.txt\" not found",
                                                         QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())