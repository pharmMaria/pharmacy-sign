import os
import streamlit as st
import google.generativeai as genai

# --- 1. 초기 설정 및 API 키 세팅 (보안 업데이트 🛡️) ---
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except (KeyError, FileNotFoundError):
    GEMINI_API_KEY = "AIzaSyDgWuhSrS-ojHl379aAUS9lUGLp09Aogb0"

genai.configure(api_key=GEMINI_API_KEY)

# --- 2. 가상의 전국 약국 평균 가격 데이터베이스 ---
mock_price_db = {
    "텐텐": "25,000원",
    "타이레놀": "3,000원",
    "탁센": "3,500원",
    "아로나민골드": "28,000원",
    "비맥스메타": "35,000원"
}

# --- 3. AI 모델 설정 ---
model = genai.GenerativeModel('gemini-2.5-flash')


def get_ai_recommendation(product_name):
    """AI를 통해 제품의 종류와 추천 문구를 생성하는 함수"""
    prompt = f"""
    당신은 친절하고 전문적인 약사입니다. 약국 매대에 놓을 '{product_name}'의 안내문을 작성하려고 합니다.
    다음 두 가지 항목을 작성해 주세요.
    
    1. 종류: 이 약/제품의 분류를 짧게 적어주세요 (예: 어린이 영양제, 소염진통제, 비타민 등)
    2. 추천문구: 손님의 구매를 돕는 따뜻하고 센스 있는 추천 문구를 1~2줄로 적어주세요.
    
    출력 형식은 반드시 아래와 같이 해주세요:
    종류: [종류 내용]
    추천문구: [추천문구 내용]
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"종류: 정보 없음\n추천문구: AI 문구 생성 중 오류가 발생했습니다. ({e})"


# --- 4. 사용자 인터페이스 (UI) 구성 ---
st.set_page_config(page_title="약국 매대 안내문 생성기", page_icon="💊")

st.title("💊 약국 매대 제품안내문 자동 생성기(테스트중!)")
st.markdown("제품 이름을 입력하면 평균 가격과 AI 추천 문구가 포함된 안내문이 완성됩니다!")

product_name = st.text_input("제품 이름을 입력하세요 (예: 텐텐, 타이레놀)",
                             placeholder="여기에 약 이름을 적어주세요")

if st.button("✨ 안내문 생성하기"):
    if product_name:
        with st.spinner("AI가 추천 문구를 작성하고 있습니다... 잠시만 기다려주세요."):

            avg_price = mock_price_db.get(product_name,
                                          "가격 정보 없음 (데이터베이스에 없음)")
            ai_result = get_ai_recommendation(product_name)

            category = "정보 없음"
            recommendation = "정보 없음"

            for line in ai_result.split('\n'):
                if line.startswith("종류:"):
                    category = line.replace("종류:", "").strip()
                elif line.startswith("추천문구:"):
                    recommendation = line.replace("추천문구:", "").strip()

            st.success("안내문이 완성되었습니다!")
            st.markdown("---")
            st.markdown(f"### 🏷️ {product_name}")
            st.markdown(f"**분류:** {category}")
            st.markdown(f"**전국 평균 가격:** 💰 {avg_price}")
            st.info(f"💡 **약사님의 추천:**\n\n{recommendation}")
            st.markdown("---")

    else:
        st.warning("제품 이름을 먼저 입력해 주세요!")
