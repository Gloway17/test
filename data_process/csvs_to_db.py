import os
import pandas as pd
import sqlite3
import chardet

# CSV 파일이 저장된 디렉토리 경로
csv_directory = r'C:\Users\soke0\Desktop\DFAS'

# 하나의 SQLite 데이터베이스 파일 생성
db_file = 'merged_database.db'
conn = sqlite3.connect(db_file)

# 인코딩 자동 감지 함수
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

# 디렉토리 내 모든 .csv 파일 읽기
for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_directory, filename)
        
        # 파일명에서 테이블 이름 생성 (확장자 제거)
        table_name = os.path.splitext(filename)[0]
        
        # 파일의 인코딩 감지
        encoding = detect_encoding(file_path)
        
        try:
            # 감지된 인코딩으로 CSV 파일 읽기 (공백 구분자 사용)
            df = pd.read_csv(file_path, encoding=encoding, sep='\s+', on_bad_lines='skip')
        except (UnicodeDecodeError, pd.errors.ParserError) as e:
            print(f"{table_name} 테이블 생성 중 오류 발생: {e}")
            continue
        
        # SQLite DB에 DataFrame 저장 (테이블 이름: CSV 파일 이름)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f'{table_name} 테이블이 생성되었습니다.')

# 연결 종료
conn.close()
print('모든 CSV 파일이 하나의 SQLite 데이터베이스에 저장되었습니다.')
