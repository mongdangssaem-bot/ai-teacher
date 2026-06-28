import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="AI 국어 선생님", page_icon="🌿", layout="centered")

# API 키 설정 (나중에 스트림릿에서 안전하게 연결할 예정입니다)
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🌿 AI 국어 선생님")
st.subheader("초등학생 글쓰기 심층 분석 및 첨삭 보고서 자동 생성")
st.markdown("---")

grade = st.text_input("학생 학년", placeholder="예: 2학년 (또는 2)")
uploaded_file = st.file_uploader("글쓰기 스캔본 업로드 (JPG, PNG)", type=["jpg", "jpeg", "png"])

if st.button("선택한 스캔본 분석 시작하기", type="primary"):
    if not uploaded_file:
        st.error("스캔본을 먼저 업로드해주세요.")
    else:
        with st.spinner("학생의 글을 꼼꼼히 분석하고 있습니다..."):
            image = Image.open(uploaded_file)
            prompt = f"""
            당신은 초등학교 저학년 학생들의 글쓰기를 지도하는 AI 튜터입니다.
            이미지의 글을 판독하고 다음 형식에 맞춰 보고서를 작성하세요.
            1. 원문 추출
            2. 🌟 토닥토닥 칭찬 한마디
            3. ✍️ 맞춤법 및 띄어쓰기 교정 (표 형태)
            4. 💡 표현 제안
            5. 📊 심층 분석 요약 (교사용. 개조식으로 3줄 이내, 간결하게)
            """
            response = model.generate_content([prompt, image])
            st.success("분석이 완료되었습니다!")
            st.write(response.text)
