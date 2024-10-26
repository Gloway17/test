import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QComboBox, QFrame, QLineEdit, QPushButton, QMainWindow
from PyQt5.QtCore import Qt

class DetailedAnalysisUI(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("상세 분석 결과")
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

        # 상단 파일 선택 컴보박스와 타이틀
        file_selection_layout = QHBoxLayout()
        title_label = QLabel("상세 분석 결과")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        file_selection_layout.addWidget(title_label)

        file_combo = QComboBox()
        file_combo.addItem("2024_조달청.hwp")
        file_selection_layout.addWidget(file_combo)

        right_layout.addLayout(file_selection_layout)

        # 중앙 파일 아이콘 및 파일 이름
        file_layout = QVBoxLayout()
        file_icon_label = QLabel("📄")
        file_icon_label.setAlignment(Qt.AlignCenter)
        file_icon_label.setStyleSheet("font-size: 48px;")
        file_name_label = QLabel("2024_조달청.hwp")
        file_name_label.setAlignment(Qt.AlignCenter)
        file_layout.addWidget(file_icon_label)
        file_layout.addWidget(file_name_label)

        right_layout.addLayout(file_layout)

        # 타데이터 기반 정보
        metadata_layout = QVBoxLayout()
        metadata_label = QLabel("타데이터 기반")
        metadata_label.setStyleSheet("border: 1px solid black; padding: 5px;")
        metadata_info = QLabel("제목\n직상지\n최종 수정자\n생성 시간\n인쇄 시간\n최종 인쇄자\n애플리케이션\n회사\n이름")
        metadata_layout.addWidget(metadata_label)
        metadata_layout.addWidget(metadata_info)

        # 파일 시스템 기반 정보
        filesystem_layout = QVBoxLayout()
        filesystem_label = QLabel("파일 시스템 기반")
        filesystem_label.setStyleSheet("border: 1px solid black; padding: 5px;")
        filesystem_info = QLabel("생성 시간\n수정 시간\n이름 변경 이벤트")
        filesystem_layout.addWidget(filesystem_label)
        filesystem_layout.addWidget(filesystem_info)

        # 시스템 아티팩트 기반 정보
        artifact_layout = QVBoxLayout()
        artifact_label = QLabel("시스템 아티팩트 기반")
        artifact_label.setStyleSheet("border: 1px solid black; padding: 5px;")
        artifact_info = QLabel("Shell bag mru\nActivities cache\nJumplist\nlnk\nrecentdocs")
        artifact_layout.addWidget(artifact_label)
        artifact_layout.addWidget(artifact_info)

        # 정보 레이아웃 설정
        info_layout = QHBoxLayout()
        info_layout.addLayout(metadata_layout)
        info_layout.addLayout(filesystem_layout)
        info_layout.addLayout(artifact_layout)

        right_layout.addLayout(info_layout)

        # 메인 레이아웃에 좌측 및 우측 레이아웃 추가
        main_layout.addWidget(left_frame)
        main_layout.addLayout(right_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)