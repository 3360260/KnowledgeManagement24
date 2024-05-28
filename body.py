from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class Body(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the main layout for the content
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        main_layout.setSpacing(0)  # Set spacing to zero

        # Single big box
        body = QLabel('Main Content')
        body.setFixedSize(1280, 640)
        body.setStyleSheet("background-color: lightgrey; padding: 10px; border: 2px solid #D66A28;")
        main_layout.addWidget(body)

        self.setLayout(main_layout)
