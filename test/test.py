import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from datetime import datetime, timedelta
import numpy as np

# 폰트 파일 경로 지정 (굴림 폰트의 .ttf 파일 경로로 설정)
font_path = "./font/NanumGothic.ttf"  # 폰트 파일 위치
font_prop = fm.FontProperties(fname=font_path)

# 음수 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

# 주요 사건 날짜 및 시간들
yy = 2024
dates = [
    datetime(yy, 9, 1, 9, 0),   # 2024-09-01 09:00
    datetime(yy, 9, 1, 12, 30), # 2024-09-01 12:30
    datetime(yy, 9, 1, 15, 0),  # 2024-09-01 15:00
    datetime(yy, 9, 1, 17, 30), # 2024-09-01 17:30
    datetime(yy, 9, 1, 20, 0),  # 2024-09-01 20:00
    datetime(yy, 9, 1, 22, 30)  # 2024-09-01 22:30
]

# 최소 날짜와 최대 날짜를 구하고, 각각 1시간씩 조정
min_date = min(dates) - timedelta(hours=1)
max_date = max(dates) + timedelta(hours=1)

# 각 사건의 레이블
labels = [
    '파일 생성', 
    'USB 입력', 
    '파일 복사',
    '.spl 파일 삭제',
    'USB에 존재하는 \n문서 열람 기록', 
    'USB 제거'
]
# 날짜와 레이블을 결합해 보기 좋게 표현
labels = ['{0:%Y. %m. %d. %H:%M}\n{1}'.format(d, l) for l, d in zip(labels, dates)]

# 그래프 설정
fig, ax = plt.subplots(figsize=(15, 4), constrained_layout=True)
_ = ax.set_ylim(-2, 1.75)
_ = ax.set_xlim(min_date, max_date)
_ = ax.axhline(0, xmin=0.05, xmax=0.95, c='deeppink', zorder=1)

# 사건 날짜를 점으로 표시
_ = ax.scatter(dates, np.zeros(len(dates)), s=120, c='palevioletred', zorder=2)
_ = ax.scatter(dates, np.zeros(len(dates)), s=30, c='darkmagenta', zorder=3)

label_offsets = np.zeros(len(dates))
label_offsets[::2] = 0.35
label_offsets[1::2] = -0.7

# 각 사건에 대한 텍스트 레이블 추가
for i, (l, d) in enumerate(zip(labels, dates)):
    _ = ax.text(d, label_offsets[i], l, ha='center', fontproperties=font_prop, fontweight='bold', color='royalblue', fontsize=12)

# 줄기(선) 추가로 점을 강조
stems = np.zeros(len(dates))
stems[::2] = 0.3
stems[1::2] = -0.3
markerline, stemline, baseline = ax.stem(dates, stems)
_ = plt.setp(markerline, marker=',', color='darkmagenta')
_ = plt.setp(stemline, color='darkmagenta')

# 그래프 테두리 (위, 아래, 왼쪽, 오른쪽) 숨김 처리
for spine in ["left", "top", "right", "bottom"]:
    _ = ax.spines[spine].set_visible(False)

# 눈금 라벨 숨김 처리
_ = ax.set_xticks([])
_ = ax.set_yticks([])

# 그래프 타이틀 설정 (한글로 변경)
_ = ax.set_title('조달청.hwp의 라이프사이클 타임라인 (시간별)', fontweight="bold", fontproperties=font_prop, fontsize=16, color='royalblue')

# 그래프 표시
plt.show()
