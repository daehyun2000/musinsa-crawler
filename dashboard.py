import streamlit as st
import pandas as pd
import time

# 페이지 기본 설정
st.set_page_config(page_title="무신사 상황판", layout="wide")

st.title("📉 무신사 가격 추적 상황판")
st.markdown("---")

# 1. 데이터 파이프라인 연결 (CSV 읽어오기)
try:
    # CSV 파일 읽기
    df = pd.read_csv('musinsa_log.csv')
    
    # 2. 핵심 지표(KPI) 보여주기
    # 가장 최근 가격 가져오기
    latest_price = df['가격'].iloc[-1] 
    last_time = df['수집시간'].iloc[-1]
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="현재 가격", value=f"{latest_price:,}원", delta="실시간 수집중")
    with col2:
        st.info(f"마지막 업데이트: {last_time}")

    # 3. 가격 변동 그래프 (Line Chart)
    st.subheader("📊 시간별 가격 변동 추이")
    
    # 그래프를 그리기 위해 데이터를 좀 다듬습니다.
    chart_data = df.set_index('수집시간')['가격']
    st.line_chart(chart_data)

    # 4. 상세 데이터 로그
    with st.expander("📂 원본 데이터 로그 보기"):
        st.dataframe(df.sort_index(ascending=False)) # 최신순 정렬

except FileNotFoundError:
    st.error("🚨 아직 수집된 데이터가 없습니다! 'main.py'를 먼저 실행해주세요.")
    
# 5. 수동 크롤링 버튼 (심화 기능: 버튼 누르면 크롤러 실행!)
if st.button("🔄 지금 즉시 가격 확인하기"):
    st.write("크롤러가 출동했습니다... 잠시만 기다려주세요.")