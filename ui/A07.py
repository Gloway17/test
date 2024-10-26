import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QComboBox, QFrame, QMainWindow
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def set_matplotlib_korean_font():
    plt.rcParams['font.family'] = 'Gulim'  # 굴림 폰트를 사용
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

class TimelineViewerUI(QMainWindow):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("타임라인 뷰어")
        self.setGeometry(100, 100, 900, 600)
        self.setupUI()

    def setupUI(self):
        # 메인 레이아웃 설정
        main_layout = QHBoxLayout()

        # 왼쪽 메뉴 레이아웃 설정
        left_layout = QVBoxLayout()
        left_layout.setSpacing(10)

        # 메뉴 상단 라벨
        header_label = QLabel("EFG유통\nPC-001")
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
        title_label = QLabel("타임라인 뷰어")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        file_selection_layout.addWidget(title_label)

        file_combo = QComboBox()
        file_combo.addItem("2024_조달청.hwp")
        file_selection_layout.addWidget(file_combo)

        right_layout.addLayout(file_selection_layout)

        # 그래프 추가 (matplotlib)
        graph_layout = QVBoxLayout()
        self.graph_canvas = TimelineGraphCanvas(self)
        graph_layout.addWidget(self.graph_canvas)
        right_layout.addLayout(graph_layout)

        # 이벤트 상세 정보
        details_layout = QVBoxLayout()
        event1 = QLabel("2024-10-23 13:00:00\n외부메일 발송")
        event2 = QLabel("2023-10-23 13:30:02\na. b. c. 문서 인쇄")
        event3 = QLabel("2024-10-23 - 14:00:39\nUsb 저장 연결")

        event1.setStyleSheet("border: 1px solid black; padding: 5px;")
        event2.setStyleSheet("border: 1px solid black; padding: 5px;")
        event3.setStyleSheet("border: 1px solid black; padding: 5px;")

        details_layout.addWidget(event1)
        details_layout.addWidget(event2)
        details_layout.addWidget(event3)

        right_layout.addLayout(details_layout)

        # 메인 레이아웃에 좌측 및 우측 레이아웃 추가
        main_layout.addWidget(left_frame)
        main_layout.addLayout(right_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

class TimelineGraphCanvas(FigureCanvas):
    def __init__(self, parent=None):
        set_matplotlib_korean_font()
        fig = Figure(figsize=(5, 3), dpi=100)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)
        self.plot()

    def plot(self):
        # 샘플 데이터 (시간대별 이메일, USB, 인쇄 이벤트 수)
        times = ['9:00', '11:00', '13:00', '15:00', '17:00', '19:00', '21:00']
        email_counts = [3, 2, 4, 5, 0, 1, 0]
        usb_counts = [1, 0, 0, 2, 3, 0, 1]
        print_counts = [0, 1, 2, 0, 4, 1, 0]

        # 그래프 그리기
        self.axes.clear()
        self.axes.bar(times, email_counts, label='이메일', color='blue', alpha=0.7)
        self.axes.bar(times, usb_counts, label='usb', color='orange', alpha=0.7)
        self.axes.bar(times, print_counts, label='인쇄', color='green', alpha=0.7)
        self.axes.set_title('타임라인 이벤트 그래프')
        self.axes.legend()
        self.draw()
