import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QFrame, QLineEdit, QPushButton, QMainWindow
from PyQt5.QtCore import Qt

class AnalysisResultUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("분석 결과")
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

        # 분석 결과 타이틀
        title_label = QLabel("유출 의심 문서 목록")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        right_layout.addWidget(title_label)

        # 유출 의심 문서 리스트
        doc_layout = QVBoxLayout()
        
        # 첫 번째 문서 정보
        doc1_layout = QHBoxLayout()
        doc1_name = QLineEdit("2024_조달청_머시기.hwp")
        doc1_name.setFixedHeight(30)
        doc1_path = QLabel("경로: C:\\Users\\001\\Documents\\비밀")
        doc1_layout.addWidget(doc1_name)
        doc1_layout.addWidget(doc1_path)
        doc_layout.addLayout(doc1_layout)

        # 두 번째 문서 정보
        doc2_layout = QHBoxLayout()
        doc2_name = QLineEdit("줄리다.pdf")
        doc2_name.setFixedHeight(30)
        doc2_path = QLabel("경로: C:\\Users\\001\\Documents\\업무")
        doc2_layout.addWidget(doc2_name)
        doc2_layout.addWidget(doc2_path)
        doc_layout.addLayout(doc2_layout)

        # 문서 목록을 오른쪽 레이아웃에 추가
        right_layout.addLayout(doc_layout)

        # 디렉터리 입력 섹션
        directory_layout = QHBoxLayout()
        directory_label = QLabel("추출 문서 디렉터리 입력")
        directory_input = QLineEdit()
        directory_button = QPushButton("...")
        directory_layout.addWidget(directory_label)
        directory_layout.addWidget(directory_input)
        directory_layout.addWidget(directory_button)
        right_layout.addLayout(directory_layout)

        # 하단 버튼 레이아웃
        bottom_button_layout = QHBoxLayout()
        guide_button = QPushButton("추출 가이드")
        detailed_result_button = QPushButton("상세 분석 결과")
        bottom_button_layout.addWidget(guide_button)
        bottom_button_layout.addWidget(detailed_result_button)
        right_layout.addLayout(bottom_button_layout)

        # 메인 레이아웃에 좌측 및 우측 레이아웃 추가
        main_layout.addWidget(left_frame)
        main_layout.addLayout(right_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnalysisResultUI()
    window.show()
    sys.exit(app.exec_())
