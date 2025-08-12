# main_gui.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit
import myagent

class AgentGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Agent - PySide6")
        self.setGeometry(200, 200, 500, 400)

        layout = QVBoxLayout()

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type your message here...")
        layout.addWidget(self.input_box)

        self.send_button = QPushButton("Send")
        layout.addWidget(self.send_button)

        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        self.setLayout(layout)

        # Events
        self.send_button.clicked.connect(self.handle_send)
        self.input_box.returnPressed.connect(self.handle_send)

    def handle_send(self):
        user_text = self.input_box.text().strip()
        if not user_text:
            return
        response = myagent.process_input(user_text)
        self.output_area.append(f"You: {user_text}")
        self.output_area.append(f"Agent: {response}")
        self.output_area.append("")  # spacing
        self.input_box.clear()

if __name__ == "__main__":
    myagent.init_db()
    app = QApplication(sys.argv)
    window = AgentGUI()
    window.show()
    sys.exit(app.exec())
