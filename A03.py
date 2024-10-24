import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QListWidget, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CaseCreationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CASE 생성")
        self.setGeometry(100, 100, 900, 600)
        self.setupUI()

    def setupUI(self):
        # 메인 레이아웃 설정
        main_layout = QHBoxLayout()

        # 왼쪽 메뉴 레이아웃 설정
        left_layout = QVBoxLayout()
        left_layout.setSpacing(10)

        # 메뉴 상단 라벨
        header_label = QLabel("EFG유통")
        header_label.setFont(QFont("Arial", 14))
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

        # 하단 텍스트
        pc_label = QLabel("PC-30")
        pc_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(pc_label)

        # 왼쪽 레이아웃을 프레임으로 감싸기
        left_frame = QFrame()
        left_frame.setLayout(left_layout)
        left_frame.setFrameShape(QFrame.StyledPanel)

        # 오른쪽 레이아웃 설정
        right_layout = QVBoxLayout()
        right_layout.setSpacing(10)

        # CASE 생성 제목
        title_label = QLabel("CASE 생성")
        title_label.setFont(QFont("Arial", 16))
        title_label.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(title_label)

        # 파일 선택 필드와 버튼을 담을 그리드 레이아웃
        grid_layout = QGridLayout()

        # 입력 필드와 버튼 설정
        labels = ["Csv 일괄 추출", "Spool 파일", "Activitycache", "Eventlog", "Registry key"]
        for i, text in enumerate(labels):
            label = QLabel(text)
            line_edit = QLineEdit()
            select_button = QPushButton("...")
            grid_layout.addWidget(label, i, 0)
            grid_layout.addWidget(line_edit, i, 1)
            grid_layout.addWidget(select_button, i, 2)

        right_layout.addLayout(grid_layout)

        # 하단 버튼 레이아웃
        button_layout = QHBoxLayout()
        guide_button = QPushButton("추출 가이드")
        analyze_button = QPushButton("분석")
        cancel_button = QPushButton("취소")
        button_layout.addWidget(guide_button)
        button_layout.addWidget(analyze_button)
        button_layout.addWidget(cancel_button)

        right_layout.addLayout(button_layout)

        # 메인 레이아웃에 좌측 및 우측 레이아웃 추가
        main_layout.addWidget(left_frame)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaseCreationUI()
    window.show()
    sys.exit(app.exec_())
