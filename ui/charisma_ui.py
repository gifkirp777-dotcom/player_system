import streamlit as st


def render_charisma_ui():
    inputs = {}

    st.markdown("## ✨ Параметры проявления харизмы")

    # ВРЕМЯ
    inputs["minutes"] = st.number_input(
        "⏱ Время проявления (минут)",
        min_value=0,
        max_value=300,
        value=20,
        step=1,
        key="char_minutes"
    )

    # ОБЩАЯ ШКАЛА ДЛЯ ЭЛЕМЕНТОВ
    scale = {
        "0 — отсутствует": 0,
        "0.5 — слабое проявление": 0.5,
        "1 — заметный уровень": 1,
        "1.5 — сильное влияние": 1.5
    }

    def select_element(title, key):
        st.markdown(f"### {title}")
        value = st.selectbox(title, list(scale.keys()), key=key)
        return scale[value]

    inputs["presence"] = select_element("Присутствие", "char_presence")
    inputs["expressiveness"] = select_element("Выразительность", "char_express")
    inputs["empathy"] = select_element("Эмпатия", "char_empathy")
    inputs["charm"] = select_element("Обаяние", "char_charm")
    inputs["persuasion"] = select_element("Убеждение", "char_persuasion")
    inputs["brand"] = select_element("Личный бренд", "char_brand")

    # КОЭФФИЦИЕНТ СИТУАЦИИ
    situation_map = {
        "Обычная ситуация (1.0)": 1.0,
        "Социальная среда (1.3)": 1.3,
        "Публичная / стрессовая (1.7)": 1.7,
        "Сцена / конфликт / высокая ответственность (2.0)": 2.0
    }

    st.markdown("### 🎭 Коэффициент ситуации")
    situation_choice = st.selectbox("Контекст проявления", list(situation_map.keys()))
    inputs["situation_coef"] = situation_map[situation_choice]

   

    return inputs