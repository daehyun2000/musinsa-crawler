from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd             # [추가] 엑셀 처리를 위한 도구
from datetime import datetime   # [추가] 오늘 날짜 기록용
import os                       # [추가] 파일이 있는지 확인용

# 1. 브라우저 설정 (Headless 모드 추천: 창 안 뜨고 백그라운드 실행)
options = webdriver.ChromeOptions()
options.add_argument("headless") # 이 줄을 주석(#) 처리하면 브라우저가 뜨는 게 보입니다.

print("🕵️ 무신사 잠입 시작...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 2. 타겟 상품 (원하는 상품으로 바꾸셔도 됩니다)
url = "https://www.musinsa.com/app/goods/3164998"
driver.get(url)
time.sleep(3) # 로딩 대기

try:
    # 3. 데이터 수집 (가격 & 상품명)
    xpath_price = "//span[contains(@class, 'Price__CalculatedPrice')]"
    price_tag = driver.find_element(By.XPATH, xpath_price)
    
    # 숫자 변환
    raw_price = price_tag.text 
    clean_price = int(raw_price.replace("원", "").replace(",", ""))
    
    # 현재 시간
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"✅ 수집 성공! 시간: {now} | 가격: {clean_price}원")

    # ---------------------------------------------------------
    # [핵심 엔지니어링] 수집한 데이터를 '창고(CSV)'에 적재하기
    # ---------------------------------------------------------
    
    # 저장할 데이터 뭉치 만들기
    new_data = {
        '수집시간': [now],
        '상품명': ['무신사 셔츠'], # 나중엔 이것도 크롤링하면 됨
        '가격': [clean_price]
    }
    df = pd.DataFrame(new_data)

    # 파일이 없으면 새로 만들고(header=True), 있으면 이어붙이기(mode='a', header=False)
    file_name = 'musinsa_log.csv'
    if not os.path.exists(file_name):
        df.to_csv(file_name, index=False, mode='w', encoding='utf-8-sig')
    else:
        df.to_csv(file_name, index=False, mode='a', header=False, encoding='utf-8-sig')
        
    print(f"💾 '{file_name}' 파일에 안전하게 저장했습니다.")

except Exception as e:
    print(f"❌ 에러 발생: {e}")

finally:
    driver.quit()