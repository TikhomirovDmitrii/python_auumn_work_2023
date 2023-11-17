# Task #1
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys

class ButtonCounterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.click_count = 0

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Click Count: 0")
        layout.addWidget(self.label)

        self.button = QPushButton("Click me!")
        self.button.clicked.connect(self.increment_count)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def increment_count(self):
        self.click_count += 1
        self.label.setText(f"Click Count: {self.click_count}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ButtonCounterApp()
    window.setWindowTitle("Button Counter")
    window.show()
    sys.exit(app.exec())

# Task #2
def is_palindrome(s):
    s = s.lower()
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

print(is_palindrome("radar"))  # True
print(is_palindrome("hello"))  # False

# Task #3
def to_camel(input_string):
    words = input_string.split()

    camel_case_words = [words[0].capitalize()] + [word.capitalize() for word in words[1:]]
    camel_case_string = ''.join(camel_case_words)
    return camel_case_string

input_str = "camel case word"
camel_case_result = to_camel(input_str)
print(camel_case_result)
