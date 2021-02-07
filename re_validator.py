import sys,re,qdarkgraystyle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        font=QFont('微軟正黑體',16)
        self.setMinimumSize(400,400)
        self.setWindowTitle('正則表達式驗證器')
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)

        self.lb1=QLabel('輸入規則')
        self.lb2=QLabel('輸入字串')
        self.edit1=QLineEdit('')
        self.edit2=QLineEdit('')
        self.lb3=QLabel('')
        self.btn1=QPushButton('確定')
        self.btn2=QPushButton('清除')

        self.lb1.setFont(font)
        self.lb2.setFont(font)
        self.edit1.setFont(font)
        self.edit2.setFont(font)
        self.lb3.setFont(font)
        self.lb3.setObjectName('lb3')
        self.lb3.setStyleSheet('QLabel#lb3 {background-color:white;color:black}')
        self.lb3.setAlignment(Qt.AlignTop)
        self.btn1.setFont(font)
        self.btn2.setFont(font)

        self.btn1.clicked.connect(self.verify)
        self.btn2.clicked.connect(self.clean)

        layout1=QHBoxLayout()
        layout2=QHBoxLayout()
        layout3=QHBoxLayout()

        layout1.addWidget(self.lb1)
        layout1.addWidget(self.edit1)
        layout2.addWidget(self.lb2)
        layout2.addWidget(self.edit2)
        layout3.addWidget(self.btn1)
        layout3.addWidget(self.btn2)

        self.layout.addLayout(layout1)
        self.layout.addLayout(layout2)
        self.layout.addWidget(self.lb3)
        self.layout.addLayout(layout3)

    def verify(self):
        self.lb3.setStyleSheet('QLabel#lb3 {background-color:white;color:black}')
        try:
            raw_rule=r'{}'.format(self.edit1.text().strip())
            rule=re.compile(raw_rule)
        except:
            self.lb3.setStyleSheet('QLabel#lb3 {background-color:white;color:red}')
            self.lb3.setText('驗證規則輸入錯誤，請重新輸入')
            rule=''

        if rule!='' and self.edit2.text().strip()!="" and self.edit1.text().strip()!="":
            result=rule.findall(self.edit2.text().strip())
            if result==[]:
                self.lb3.setText('沒有符合規則的結果')
            else:
                text='符合篩選條件的結果如下：\n'
                for i in range(len(result)):
                    text+=result[i]
                self.lb3.setText(text)

        elif self.edit2.text().strip()=="" or self.edit1.text().strip()=="":
            self.lb3.setText('請在所有欄位輸入資料')

        if rule=='':
            self.lb3.setText('驗證規則輸入錯誤，請重新輸入')




    def clean(self):
        self.edit1.clear()
        self.edit2.clear()
        self.lb3.clear()



if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setStyleSheet(qdarkgraystyle.load_stylesheet())
    win=Main()
    win.show()
    sys.exit(app.exec_())