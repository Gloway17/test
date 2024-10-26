import win32evtlog # 이벤트로그
import sqlite3 # db

def evtx_to_db(filename: str):
    # *.evtx 이벤트로그 파일을 db table(파일이름이 곧, table이름?)에 저장하는 함수
    pass
    return None

def registry_to_db(filename: str):
    # 다섯개의 하이브 파일들을 읽어 "필요한"키의 하위 키를 가공하여 테이블에 저장
    pass
    return None

def activity_cache_to_db(filename: str):
    # 액티비티 캐시의 db를 가공 및 저장
    pass
    return None

def spl_to_db(filename: str):
    # spl파일에서 필요한 정보를 가공 및 db에 저장
    pass
    return None

def docs_parser(filename: str):
    #파일 확장자에 따라 문서의 메타데이터를 딕셔너리 형태로 반환
    pass
    return dict