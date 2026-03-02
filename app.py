import streamlit as st

from ui.layout import setup_page
from core.session import init_session
from core.power_system import calculate_power
from core.rank_system import update_rank
from ui.profile_ui import render_profile
from ui.stats_ui import render_stats_tab

setup_page()
st.sidebar.markdown("## ⚔ Система")
init_session()

# Обновляем систему
st.session_state.data["stats"]["Власть"] = calculate_power(
    st.session_state.data["stats"]
)

st.session_state.data["rank"] = update_rank(
    st.session_state.data
)

# ===== НАВИГАЦИЯ В SIDEBAR =====

menu = st.sidebar.radio(
    "⚔ НАВИГАЦИЯ",
    ["Профиль", "Статы"]
)

if menu == "Профиль":
    render_profile(st.session_state.data)

elif menu == "Статы":
    render_stats_tab()