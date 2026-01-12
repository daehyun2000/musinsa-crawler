import requests

# 1. 아까 받은 토큰 (예: 7123...:AAF...)
token = "7947719889:AAHZy-86EFoh5H7sWRIGjae6kEnFNIjBpEg"

# 2. 숫자 ID (예: 6812...) 
# 주의: @아이디 아닙니다! 무조건 숫자여야 해요.
chat_id = "8077219703"

url = f"https://api.telegram.org/bot{token}/sendMessage"
params = {"chat_id": chat_id, "text": "테스트 메시지입니다!"}

# 메시지를 보내고, 텔레그램 서버의 '답장'을 출력합니다.
res = requests.get(url, params=params)
print(res.json())