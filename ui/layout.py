import streamlit as st

def setup_page():

    st.set_page_config(
        page_title="Система Игрока",
        page_icon="⚔",
        layout="wide"
    )

    st.markdown("""
    <style>

    .active-btn button {
        border: 2px solid #4a90e2 !important;
        background-color: #111827 !important;
        color: #4a90e2 !important;
    }

    .normal-btn button {
        border: 1px solid #2a2f3a !important;
        background-color: #1a1f2b !important;
        color: #e6e6e6 !important;
    }

    div.stButton > button {
        height: 120px;
        font-size: 20px;
        font-weight: 600;
        border-radius: 12px;
    }

    </style>
    """, unsafe_allow_html=True)