import streamlit as st
from core.data_manager import load_data

def init_session():

    if "data" not in st.session_state:
        st.session_state.data = load_data()

    if "active_stat" not in st.session_state:
        st.session_state.active_stat = None

    if "active_substat" not in st.session_state:
        st.session_state.active_substat = None