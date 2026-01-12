from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # [중요] 'By' 도구를 추가해야 합니다!
import time

# 1. 크롬 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. 무신사 상품 페이지 이동
url = "https://www.musinsa.com/app/goods/3164998"
driver.get(url)

# 3. 페이지 로딩 대기 (3초면 충분)
time.sleep(3)

# 4. [핵심] 아까 복사한 XPath로 가격 찾기
# 따옴표 안에 아까 복사한 주소를 붙여넣으세요! (Ctrl+V)
# 예: //*[@id="root"]/div/div... 어쩌고
my_xpath = '//*[@id="root"]/div[1]/div[2]/div/div[3]/div/div/div[2]/span'

try:
    price_tag = driver.find_element(By.XPATH, my_xpath)
    print("찾은 가격:", price_tag.text) # 가격 텍스트만 쏙 뽑아서 출력!
except:
    print("가격을 못 찾았어요 ㅠㅠ XPath를 다시 확인해주세요.")

# 5. 확인을 위해 잠시 대기
time.sleep(100)
driver.quit()