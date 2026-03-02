import streamlit as st


def render_social_ui():
    inputs = {}

    st.markdown("## 🌐 Параметры социального действия")

    # =========================
    # ВРЕМЯ
    # =========================
    inputs["minutes"] = st.number_input(
        "⏱ Время взаимодействия (минут)",
        min_value=0,
        max_value=600,
        value=30,
        step=1,
        key="social_minutes"
    )

    # =========================
    # ИНТЕНСИВНОСТЬ
    # =========================
    intensity_map = {
        "Наблюдал / слушал (0.5)": 0.5,
        "Участвовал в разговоре (1)": 1,
        "Вёл диалог / мотивировал (1.5)": 1.5,
        "Руководил / организовывал (2)": 2
    }

    st.markdown("### 🔥 Интенсивность")
    inputs["intensity"] = st.selectbox("Выбери уровень активности", list(intensity_map.keys()))
    inputs["intensity"] = intensity_map[inputs["intensity"]]

    # =========================
    # ОСОЗНАННОСТЬ
    # =========================
    awareness_map = {
        "Случайное действие (0.5)": 0.5,
        "Понимал цель (1)": 1,
        "Применил стратегию (1.5)": 1.5
    }

    st.markdown("### 🧠 Осознанность")
    inputs["awareness"] = st.selectbox("Насколько действия были продуманы?", list(awareness_map.keys()))
    inputs["awareness"] = awareness_map[inputs["awareness"]]

    # =========================
    # ВЛИЯНИЕ
    # =========================
    influence_map = {
        "Минимальное (0.5)": 0.5,
        "Заметное (1)": 1,
        "Существенное (1.5)": 1.5
    }

    st.markdown("### 📈 Влияние")
    inputs["influence"] = st.selectbox("Какой был эффект?", list(influence_map.keys()))
    inputs["influence"] = influence_map[inputs["influence"]]

    # =========================
    # СЛОЖНОСТЬ
    # =========================
    difficulty_map = {
        "Простое взаимодействие (0.8)": 0.8,
        "Средняя трудность (1)": 1,
        "Сложная / конфликтная ситуация (1.3)": 1.3
    }

    st.markdown("### ⚖ Сложность ситуации")
    inputs["difficulty"] = st.selectbox("Насколько ситуация была сложной?", list(difficulty_map.keys()))
    inputs["difficulty"] = difficulty_map[inputs["difficulty"]]

    # =========================
    # СВЯЗИ
    # =========================
    connections_map = {
        "Формальный контакт (0.8)": 0.8,
        "Обычное взаимодействие (1)": 1,
        "Сильное взаимодействие (1.3)": 1.3,
        "Ключевое знакомство (1.5)": 1.5
    }

    st.markdown("### 🔗 Связи")
    inputs["connections"] = st.selectbox("Какой результат по контактам?", list(connections_map.keys()))
    inputs["connections"] = connections_map[inputs["connections"]]

   

    return inputs