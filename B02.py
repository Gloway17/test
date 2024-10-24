import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, 
                             QMainWindow, QComboBox, QFrame, QLineEdit, QMenu, QAction, QTextEdit, QDialog)
from PyQt5.QtCore import Qt

class ChatMainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Main UI")
        self.setGeometry(100, 100, 900, 600)
        self.setupUI()

    def setupUI(self):
        # 메인 레이아웃 설정
        main_layout = QHBoxLayout()

        # 왼쪽 메뉴 레이아웃 설정
        left_layout = QVBoxLayout()
        left_layout.setSpacing(10)

        # 메뉴 상단 라벨
        header_label = QLabel("EFG유통\n개발·지도화")
        header_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(header_label)

        # 메뉴 리스트
        menu_list = QListWidget()
        menu_list.addItem("▶ csv input")
        menu_list.addItem("▶ 분석 결과")
        menu_list.addItem("▶ 상세 분석 결과")
        menu_list.addItem("▶ 타임라인 뷰어")
        menu_list.addItem("▶ chat")
        menu_list.setFixedWidth(150)
        left_layout.addWidget(menu_list)

        # 왼쪽 레이아웃을 프레임으로 감싸기
        left_frame = QFrame()
        left_frame.setLayout(left_layout)
        left_frame.setFrameShape(QFrame.StyledPanel)

        # 오른쪽 레이아웃 설정
        right_layout = QVBoxLayout()
        right_layout.setSpacing(10)

        # START NEW CHAT 버튼
        new_chat_button = QPushButton("START NEW CHAT")
        new_chat_button.setFixedHeight(40)
        new_chat_button.clicked.connect(self.start_new_chat)
        right_layout.addWidget(new_chat_button)

        # 기존 채팅 목록
        chat_layout = QVBoxLayout()
        chat_box = QHBoxLayout()

        # 채팅 아이템과 수정/삭제 메뉴
        chat_item = QLabel("CSV추출 방식")
        chat_item.setStyleSheet("border: 1px solid black; padding: 5px;")
        chat_item.setFixedHeight(50)

        menu_button = QPushButton("...")
        menu_button.setFixedWidth(30)
        menu_button.setFixedHeight(50)
        menu_button.setStyleSheet("border: 1px solid black;")
        menu_button.setMenu(self.create_chat_menu())

        chat_box.addWidget(chat_item)
        chat_box.addWidget(menu_button)
        chat_layout.addLayout(chat_box)

        right_layout.addLayout(chat_layout)

        # 메인 레이아웃에 좌측 및 우측 레이아웃 추가
        main_layout.addWidget(left_frame)
        main_layout.addLayout(right_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def create_chat_menu(self):
        # 채팅 메뉴 생성
        menu = QMenu()
        delete_action = QAction("삭제", self)
        edit_action = QAction("수정", self)
        delete_action.triggered.connect(self.delete_chat)
        edit_action.triggered.connect(self.edit_chat)
        menu.addAction(delete_action)
        menu.addAction(edit_action)
        return menu

    def delete_chat(self):
        print("채팅 삭제 기능 동작")

    def edit_chat(self):
        print("채팅 수정 기능 동작")

    def start_new_chat(self):
        self.new_chat_window = ChatDialog()
        self.new_chat_window.exec_()

class ChatDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LLM Chatbot")
        self.setGeometry(300, 300, 300, 400)
        self.setupUI()

    def setupUI(self):
        # 대화창 레이아웃 설정
        main_layout = QVBoxLayout()

        # 예시 메시지
        message1 = QLabel("어떻게 csv파일을 넣어야 해??")
        message1.setStyleSheet("border: 1px solid black; padding: 5px; background-color: #f0f0f0;")
        message1.setWordWrap(True)
        message2 = QLabel("프리패치라는 게 뭐야? 어떤 역할이길래 이메일 의심 근거로 사용된 거야?")
        message2.setStyleSheet("border: 1px solid black; padding: 5px; background-color: #f0f0f0;")
        message2.setWordWrap(True)

        main_layout.addWidget(message1)
        main_layout.addWidget(message2)

        # 하단 질문 입력 섹션
        input_layout = QHBoxLayout()
        input_field = QTextEdit()
        input_field.setFixedHeight(50)
        send_button = QPushButton("질의 응답")
        send_button.setFixedWidth(80)
        input_layout.addWidget(input_field)
        input_layout.addWidget(send_button)

        main_layout.addLayout(input_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatMainUI()
    window.show()
    sys.exit(app.exec_())
