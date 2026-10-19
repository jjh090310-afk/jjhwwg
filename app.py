import pathlib
import streamlit as st
import streamlit.components.v1 as components

# 1. 페이지 기본 설정 (와이드 모드, 레이아웃 깔끔화)
st.set_page_config(
    page_title="MIND LAB PRO - 심리테스트 모음집",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. 기존 Streamlit 여백 및 헤더/푸터 제거를 위한 커스텀 CSS 적용
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            border: none;
            width: 100% !important;
            height: 100vh !important;
        }
    </style>
""",
    unsafe_allow_html=True,
)


# 3. htmls/index.html 파일 불러오기 함수
def load_html():
    html_path = pathlib.Path("htmls/index.html")

    if html_path.exists():
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        st.error(
            "❌ `htmls/index.html` 파일을 찾을 수 없습니다. 경로를 확인해주세요!"
        )
        return None


# 4. HTML 파일 렌더링
html_content = load_html()

if html_content:
    components.html(html_content, height=1000, scrolling=True)
