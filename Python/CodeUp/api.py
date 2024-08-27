import time
import requests
import json
from xml.etree.ElementTree import fromstring
from xmljson import badgerfish as bf
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 데이터베이스 설정
DATABASE_URL = "sqlite:///saju.db"  # SQLite 데이터베이스 예시
Base = declarative_base()

# SajuDb 테이블 정의
class SajuDb(Base):
    __tablename__ = "sajudb"
    id = Column(String, primary_key=True)
    lun_iljin = Column(String)
    lun_wolgeon = Column(String)
    lun_secha = Column(String)
    sol_day = Column(String)
    sol_month = Column(String)
    sol_year = Column(String)
    sol_jd = Column(String)

# SQLAlchemy 설정
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

class MaridDBSave:

    def __init__(self, api_key):
        self.api_key = api_key
        self.saju_db_list = []

    def start(self):
        for i in range(1950, 2050):  # 10년씩 끊어서 데이터 받아오기
            self.fetch_and_save_year_data(i)
            print(f"저장 시작 연도 {i}")

    def fetch_and_save_year_data(self, lun_year):
        for lun_month in range(1, 13):
            max_days = self.get_max_days_in_month(lun_year, lun_month)
            for lun_day in range(1, max_days + 1):
                self.fetch_data_and_add_to_list(lun_year, lun_month, lun_day)
        
        try:
            session.add_all(self.saju_db_list)
            session.commit()
            print("DB 저장 확인 필요")
        except Exception as e:
            print(f"Save Error: {str(e)}")

    def get_max_days_in_month(self, year, month):
        if month == 2:
            return 29 if year % 4 == 0 else 28
        elif month in [4, 6, 9, 11]:
            return 30
        else:
            return 31

    def fetch_data_and_add_to_list(self, lun_year, lun_month, lun_day):
        url = self.build_url(lun_year, lun_month, lun_day)
        json_response = self.get_api_response(url)
        self.parse_and_add_to_db_list(json_response)

    def build_url(self, lun_year, lun_month, lun_day):
        base_url = "http://apis.data.go.kr/B090041/openapi/service/LrsrCldInfoService/getLunCalInfo"
        params = {
            "serviceKey": self.api_key,
            "solYear": lun_year,
            "solMonth": f"{lun_month:02d}",
            "solDay": f"{lun_day:02d}"
        }
        query_string = "&".join([f"{key}={value}" for key, value in params.items()])
        return f"{base_url}?{query_string}"

    def get_api_response(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            response.raise_for_status()

    def parse_and_add_to_db_list(self, xml_response):
        success = False

        while not success:
            try:
                json_response = bf.data(fromstring(xml_response))
                item = json_response['response']['body']['items']['item']

                saju_db = SajuDb(
                    lun_iljin=item['lunIljin']['$'],
                    lun_wolgeon=item['lunWolgeon']['$'],
                    lun_secha=item['lunSecha']['$'],
                    sol_day=str(item['solDay']['$']),
                    sol_month=str(item['solMonth']['$']),
                    sol_year=str(item['solYear']['$']),
                    sol_jd=str(item['solJd']['$'])
                )

                self.saju_db_list.append(saju_db)
                success = True

            except Exception as e:
                print(f"Parse Error: {str(e)}")
                print("오류 발생, 1일 후 다시 시도합니다.")
                time.sleep(86400)  # 하루 대기 (86400초)

        time.sleep(1)  # 일반적인 대기 시간

if __name__ == "__main__":
    api_key = "your_api_key_here"  # 여기에 API 키를 입력하세요
    marid_db_save = MaridDBSave(api_key)
    marid_db_save.start()
