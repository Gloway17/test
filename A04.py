import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QProgressBar, QPushButton, QMainWindow
from PyQt5.QtGui import QFont  # QFont 임포트 추가
from PyQt5.QtCore import Qt

class CaseCreationUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CASE 생성")
        self.setGeometry(100, 100, 600, 400)
        self.setupUI()

    def setupUI(self):
        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()

        # CASE 생성 버튼
        analyze_button = QPushButton("분석", self)
        analyze_button.clicked.connect(self.open_analysis_window)
        main_layout.addWidget(analyze_button)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def open_analysis_window(self):
        self.analysis_window = AnalysisProgressUI()
        self.analysis_window.show()

class AnalysisProgressUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("분석 진행 사항")
        self.setGeometry(100, 100, 700, 300)
        self.setupUI()

    def setupUI(self):
        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()
        
        # 상단 제목
        title_label = QLabel("분석 진행 사항")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 14))  # QFont 사용을 위해 임포트 추가
        main_layout.addWidget(title_label)

        # 진행 상황 표시 바
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(77)  # 예시로 77% 설정
        main_layout.addWidget(self.progress_bar)

        # 현재 단계 라벨
        self.current_stage_label = QLabel("현재 단계: 이메일 로그 분석 중")
        main_layout.addWidget(self.current_stage_label)

        # 진행률 정보 라벨
        self.progress_info_label = QLabel("분석 진행률: 77%\n완료 프로세스 / 전체 프로세스 : 23 / 100")
        main_layout.addWidget(self.progress_info_label)

        # 하단 버튼 레이아웃
        button_layout = QHBoxLayout()
        cancel_button = QPushButton("취소", self)
        cancel_button.clicked.connect(self.close)
        button_layout.addStretch()
        button_layout.addWidget(cancel_button)

        # 버튼 레이아웃 추가
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaseCreationUI()
    window.show()
    sys.exit(app.exec_())
