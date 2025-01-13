import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(100, 100, 300, 200)

        # Layout
        self.layout = QVBoxLayout()

        # Girdi alanları
        self.input1 = QLineEdit(self)
        self.input1.setPlaceholderText("Birinci Sayı")
        self.layout.addWidget(self.input1)

        self.input2 = QLineEdit(self)
        self.input2.setPlaceholderText("İkinci Sayı")
        self.layout.addWidget(self.input2)

        # İşlem butonları
        self.add_button = QPushButton("Topla", self)
        self.add_button.clicked.connect(self.add)
        self.layout.addWidget(self.add_button)

        self.subtract_button = QPushButton("Çıkar", self)
        self.subtract_button.clicked.connect(self.subtract)
        self.layout.addWidget(self.subtract_button)

        self.multiply_button = QPushButton("Çarp", self)
        self.multiply_button.clicked.connect(self.multiply)
        self.layout.addWidget(self.multiply_button)

        self.divide_button = QPushButton("Böl", self)
        self.divide_button.clicked.connect(self.divide)
        self.layout.addWidget(self.divide_button)

        # Sonuç etiketi
        self.result_label = QLabel("Sonuç: ", self)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def add(self):
        try:
            result = float(self.input1.text()) + float(self.input2.text())
            self.result_label.setText(f"Sonuç: {result}")
        except ValueError:
            self.result_label.setText("Hata: Geçersiz giriş!")

    def subtract(self):
        try:
            result = float(self.input1.text()) - float(self.input2.text())
            self.result_label.setText(f"Sonuç: {result}")
        except ValueError:
            self.result_label.setText("Hata: Geçersiz giriş!")

    def multiply(self):
        try:
            result = float(self.input1.text()) * float(self.input2.text())
            self.result_label.setText(f"Sonuç: {result}")
        except ValueError:
            self.result_label.setText("Hata: Geçersiz giriş!")

    def divide(self):
        try:
            divisor = float(self.input2.text())
            if divisor == 0:
                self.result_label.setText("Hata: Sıfıra bölünemez!")
            else:
                result = float(self.input1.text()) / divisor
                self.result_label.setText(f"Sonuç: {result}")
        except ValueError:
            self.result_label.setText("Hata: Geçersiz giriş!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
