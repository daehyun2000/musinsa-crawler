#
 🛍️ 무신사 가격 변동 알림 봇 (Musinsa Price Crawler)

원하는 무신사 상품의 가격을 실시간으로 감시하다가, **설정한 목표가보다 저렴해지면 텔레그램으로 알림을 보내주는 봇**입니다.

## 📌 주요 기능
* **자동화:** Selenium을 활용해 무신사 웹사이트에 자동으로 접속합니다.
* **데이터 수집:** 상품의 현재 가격 데이터를 실시간으로 크롤링합니다.
* **데이터 가공:** "486,000원" 같은 문자열 데이터를 정수(Integer)로 변환하여 계산합니다.
* **실시간 알림:** Telegram Bot API를 연동하여, 목표 가격 이하일 때 즉시 스마트폰으로 알림을 전송합니다.

## 🛠️ 사용 기술 (Tech Stack)
* **Language:** Python 3.14
* **Library:** Selenium, Requests, Webdriver-manager
* **Tools:** VS Code, GitHub Desktop

## 🔥 트러블 슈팅 (문제 해결 경험)
### 1. 동적 페이지 크롤링 문제
* **문제:** `Requests` 라이브러리만으로는 무신사의 동적 데이터(JavaScript)를 가져올 수 없었음.
* **해결:** `Selenium`을 도입하여 실제 브라우저 환경을 구축해 데이터 로딩 문제를 해결함.

### 2. XPath 요소 찾기 에러
* **문제:** `NoSuchElementException` 에러 발생. 페이지 구조가 복잡해 절대 경로(Absolute XPath)가 불안정했음.
* **해결:** `//span[contains(@class, 'Price')]`와 같은 **상대 경로(Relative XPath)**를 사용하여, 요소 위치가 조금 바뀌어도 정확히 찾을 수 있도록 개선함.

---
**Made by Daehyun Kim**