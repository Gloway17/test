import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QMainWindow
from PyQt5.QtGui import QFontDatabase, QFont
from A01 import MainUI
from A02 import CaseCreationUI
from A03 import CaseCreationUI as CaseCreationUI3
from A04 import AnalysisProgressUI
from A05 import AnalysisResultUI
from A06 import DetailedAnalysisUI
from A07 import TimelineViewerUI
from B01 import ChatBotUI
from B02 import ChatMainUI

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        
        # A01 메인 UI와 A02 Case Creation UI 추가
        self.main_ui = MainUI(self.stacked_widget)
        self.case_creation_ui = [ CaseCreationUI(self.stacked_widget)
        ,CaseCreationUI3(self.stacked_widget)
        ,AnalysisProgressUI(self.stacked_widget)
        ,AnalysisResultUI(self.stacked_widget)
        ,DetailedAnalysisUI(self.stacked_widget)
        ,TimelineViewerUI(self.stacked_widget)
        ,ChatBotUI(self.stacked_widget)
        ,ChatMainUI(self.stacked_widget) ]
        
        # 스택에 각 위젯 추가
        self.stacked_widget.addWidget(self.main_ui)         # Index 0
        for i in range(len(self.case_creation_ui)):
            self.stacked_widget.addWidget(self.case_creation_ui[i])
        
        # 스택 위젯 설정
        self.setCentralWidget(self.stacked_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec_())
