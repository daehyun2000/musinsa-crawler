from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests # [필수] 텔레그램 통신용

# ==========================================
# [설정] 방금 성공한 토큰과 ID를 여기에 넣으세요!
# ==========================================
my_token = "7947719889:AAHZy-86EFoh5H7sWRIGjae6kEnFNIjBpEg" 
my_chat_id = "8077219703"

def send_telegram_message(text):
    """텔레그램으로 메시지를 쏘는 함수"""
    url = f"https://api.telegram.org/bot{my_token}/sendMessage"
    params = {"chat_id": my_chat_id, "text": text}
    requests.get(url, params=params)

# 1. 브라우저 몰래 켜기 (옵션 추가)
options = webdriver.ChromeOptions()
# options.add_argument("headless") # 나중에 이 주석(#)을 풀면 창이 안 뜨고 백그라운드에서 돌아요!

print("브라우저를 실행합니다...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 2. 무신사 상품 페이지 이동
url = "https://www.musinsa.com/app/goods/3164998" 
driver.get(url)
time.sleep(5)

# 3. 가격 가져오기 (XPath 사용)
my_xpath = "//span[contains(@class, 'Price__CalculatedPrice')]"
target_price = 500000 # 목표 가격 (이것보다 싸면 알림!)

try:
    price_tag = driver.find_element(By.XPATH, my_xpath)
    raw_price = price_tag.text 
    
    # "486,000원" -> 486000 (숫자)로 변환
    clean_price = int(raw_price.replace("원", "").replace(",", ""))
    print(f"현재 가격: {clean_price}원")
    
    # [핵심 로직] 가격 비교 & 알림 발사
    if clean_price <= target_price:
        msg = f"🔥[대현 알리미] 가격 하락! ({clean_price}원)\n얼른 사러 가세요!\n{url}"
        send_telegram_message(msg)
        print("텔레그램 알림 전송 완료!")
    else:
        print("아직 비싸서 알림 안 보냄.")

except Exception as e:
    print("에러 발생:", e)
    send_telegram_message(f"오류 발생: {e}")

finally:
    driver.quit()
    print("프로그램 종료")