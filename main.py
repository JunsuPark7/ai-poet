# from dotenv import load_dotenv
# load_dotenv()

from langchain.chat_models import ChatOpenAI  # 최신 ChatOpenAI 클래스
import streamlit as st

chat_model = ChatOpenAI()  # 여기 API 키 입력


# print(result2.content)

st.title("인공지능 시인")
title = st.text_input("시의 주제를 제시해주세요.")


if st.button('시 작성 요청하기'):
    with st.spinner('시 작성중...'):
        result = chat_model.invoke(title + "에 대한 시를 써줘")  # predict 대신 invoke 사용
        st.write(result.content)






