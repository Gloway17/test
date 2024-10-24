import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

import A01, A02, A03, A04, A05, A06, A07, B01, B02

class MainUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A.B.C.D")
        self.setGeometry(100, 100, 900, 500)
        self.setupUI()

    def setupUI(self):
        # 메인 레이아웃 설정
        main_layout = QHBoxLayout()

        # 좌측 레이아웃 (로고 및 텍스트)
        left_layout = QVBoxLayout()
        left_layout.setAlignment(Qt.AlignCenter)
        left_layout.setSpacing(20)
        
        # 로고 이미지 추가 (예시 이미지 사용)
        logo_label = QLabel(self)
        pixmap = QPixmap('logo.png')  # 로고 이미지 파일 경로 설정
        pixmap = pixmap.scaled(300, 150, Qt.KeepAspectRatio)  # 로고 크기 조절
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)

        # 텍스트 라벨 설정
        text_label = QLabel("A . B . C . D")
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setFont(QFont("Arial", 14))

        # 레이아웃에 로고와 텍스트 추가
        left_layout.addWidget(logo_label)
        left_layout.addWidget(text_label)

        # 우측 레이아웃 (분석 시작 텍스트와 버튼)
        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignCenter)
        right_layout.setSpacing(20)

        # "분석 시작" 텍스트
        analysis_label = QLabel("▶ 분석 시작")
        analysis_label.setFont(QFont("Arial", 12))
        analysis_label.setAlignment(Qt.AlignLeft)

        # "NEW CASE" 버튼
        new_case_button = QPushButton("NEW CASE", self)
        new_case_button.setFixedSize(150, 40)

        # 레이아웃에 텍스트와 버튼 추가
        right_layout.addWidget(analysis_label)
        right_layout.addWidget(new_case_button)

        # 메인 레이아웃에 좌측 및 우측 레이아웃 추가
        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())
