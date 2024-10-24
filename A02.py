import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class CaseCreationUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CASE 생성")
        self.setGeometry(100, 100, 600, 400)
        self.setupUI()

    def setupUI(self):
        # 메인 레이아웃 설정
        main_layout = QVBoxLayout()

        # CASE 생성 제목
        title_label = QLabel("CASE 생성")
        title_label.setFont(QFont("Arial", 16))
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # 입력 필드를 담을 그리드 레이아웃
        grid_layout = QGridLayout()

        # CASE 명 입력
        case_name_label = QLabel("CASE 명")
        case_name_input = QLineEdit("EFG유통")
        grid_layout.addWidget(case_name_label, 0, 0)
        grid_layout.addWidget(case_name_input, 0, 1)

        # 부서명 / 직원명 입력
        department_label = QLabel("부서명 / 직원명")
        department_input = QLineEdit("개발 부서 | 지도화")
        grid_layout.addWidget(department_label, 1, 0)
        grid_layout.addWidget(department_input, 1, 1)

        # 분석 날짜 범위 설정 입력
        date_range_label = QLabel("분석 날짜 범위 설정")
        date_range_input = QLineEdit("(미정 가능) ~ 00년도 00월 00일")
        grid_layout.addWidget(date_range_label, 2, 0)
        grid_layout.addWidget(date_range_input, 2, 1)

        # 업무 시간 필터 입력
        work_time_label = QLabel("업무 시간 필터")
        work_time_input = QLineEdit("00시 00분 ~ 18시 00분")
        grid_layout.addWidget(work_time_label, 3, 0)
        grid_layout.addWidget(work_time_input, 3, 1)

        # 그리드 레이아웃을 메인 레이아웃에 추가
        main_layout.addLayout(grid_layout)

        # 버튼 레이아웃 설정
        button_layout = QHBoxLayout()
        create_button = QPushButton("생성")
        cancel_button = QPushButton("취소")
        button_layout.addWidget(create_button)
        button_layout.addWidget(cancel_button)

        # 버튼 레이아웃을 메인 레이아웃에 추가
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaseCreationUI()
    window.show()
    sys.exit(app.exec_())
