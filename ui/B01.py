import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QMainWindow, QScrollArea
from PyQt5.QtCore import Qt

class ChatBotUI(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("LLM Chatbot")
        self.setGeometry(100, 100, 400, 500)
        self.setupUI()

    def setupUI(self):
        # 메인 위젯과 레이아웃 설정
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # 스크롤 영역 설정
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.chat_area = QWidget()
        self.chat_layout = QVBoxLayout()
        self.chat_area.setLayout(self.chat_layout)
        self.scroll_area.setWidget(self.chat_area)

        # 예시 대화 추가
        self.add_chat_message("어떻게 csv파일을 넣어야 해??", is_user=True)
        self.add_chat_message("프리패치라는 게 뭐야? 어떤 역할이길래 이메일 의심 근거로 사용된 거야?", is_user=True)

        main_layout.addWidget(self.scroll_area)

        # 하단 질문 입력 레이아웃
        input_layout = QHBoxLayout()
        self.input_field = QTextEdit()
        self.input_field.setFixedHeight(50)
        send_button = QPushButton("질의 응답")
        send_button.setFixedWidth(80)
        send_button.clicked.connect(self.handle_send_message)
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(send_button)

        main_layout.addLayout(input_layout)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def add_chat_message(self, message, is_user=False):
        # 메시지를 라벨로 추가
        message_label = QLabel(message)
        message_label.setWordWrap(True)
        if is_user:
            message_label.setStyleSheet("border: 1px solid black; padding: 5px; background-color: #f0f0f0;")
        else:
            message_label.setStyleSheet("border: 1px solid black; padding: 5px; background-color: #e6f7ff;")

        # 사용자와 챗봇의 메시지를 오른쪽 정렬, 왼쪽 정렬로 구분
        message_layout = QHBoxLayout()
        if is_user:
            message_layout.addStretch()
            message_layout.addWidget(message_label)
        else:
            message_layout.addWidget(message_label)
            message_layout.addStretch()

        # 메시지 레이아웃을 대화창에 추가
        self.chat_layout.addLayout(message_layout)

        # 스크롤 자동으로 아래로 이동
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

    def handle_send_message(self):
        # 사용자가 메시지를 입력하고 "질의 응답" 버튼을 누르면 실행
        user_message = self.input_field.toPlainText().strip()
        if user_message:
            self.add_chat_message(user_message, is_user=True)
            self.input_field.clear()

            # 여기에 챗봇의 응답 로직 추가 가능
            bot_response = "질문에 대한 답변입니다."  # 예시 응답
            self.add_chat_message(bot_response)