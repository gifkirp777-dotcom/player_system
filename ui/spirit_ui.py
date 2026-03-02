import streamlit as st


def render_spirit_ui():
    inputs = {}

    st.markdown("## 🔥 Параметры испытания силы духа")

    # ВРЕМЯ
    inputs["minutes"] = st.number_input(
        "⏱ Время преодоления (минут)",
        min_value=0,
        max_value=600,
        value=30,
        step=1,
        key="spirit_minutes"
    )

    # ИНТЕНСИВНОСТЬ
    intensity_map = {
        "Лёгкая (0.5)": 0.5,
        "Средняя (1)": 1,
        "Сильная (1.5)": 1.5,
        "Очень высокая (2)": 2
    }

    st.markdown("### ⚔ Интенсивность выхода из зоны комфорта")
    choice = st.selectbox("Выбери уровень", list(intensity_map.keys()))
    inputs["intensity"] = intensity_map[choice]

    # ОСОЗНАННОСТЬ
    awareness_map = {
        "Поверхностно (0.5)": 0.5,
        "Понял (1)": 1,
        "Закрепил / записал (1.5)": 1.5
    }

    st.markdown("### 🧠 Осознанность")
    choice = st.selectbox("Насколько осознанно проходил испытание?", list(awareness_map.keys()))
    inputs["awareness"] = awareness_map[choice]

    # КОНТЕКСТ
    context_map = {
        "Лёгкий (0.5)": 0.5,
        "Средний (1)": 1,
        "Сильный (1.5)": 1.5,
        "Экстремальный (2)": 2
    }

    st.markdown("### 🌍 Контекст / сложность среды")
    choice = st.selectbox("В каких условиях происходило?", list(context_map.keys()))
    inputs["context"] = context_map[choice]

    # ЭМОЦИОНАЛЬНЫЙ КОНТРОЛЬ
    emotional_map = {
        "Потерял контроль (0.5)": 0.5,
        "Частично контролировал (1)": 1,
        "Полностью держал себя (1.5)": 1.5
    }

    st.markdown("### 🧊 Эмоциональный контроль")
    choice = st.selectbox("Насколько управлял эмоциями?", list(emotional_map.keys()))
    inputs["emotional_control"] = emotional_map[choice]

    # ТРАНСФОРМАЦИЯ
    transform_map = {
        "Не закрепил (0.5)": 0.5,
        "Закрепил навык (1)": 1,
        "Создал новую привычку / ресурс (1.5)": 1.5
    }

    st.markdown("### 🔄 Трансформация")
    choice = st.selectbox("Какой был итог?", list(transform_map.keys()))
    inputs["transformation"] = transform_map[choice]

    # =========================
    # УПРОЩЁННЫЕ АСКЕЗЫ (1 штука)
    # =========================
    st.markdown("## 🧘 Аскеза (если есть)")

    use_askesis = st.checkbox("Есть активная аскеза", key="spirit_has_askesis")

    askesis_list = []

    if use_askesis:
        base = st.slider("Сложность аскезы", 0.5, 2.0, 1.0, 0.1)
        k = st.selectbox(
            "Степень соблюдения",
            ["Частично (0.8)", "Полностью (1)", "Сверхстрого (1.2)"]
        )

        k_map = {
            "Частично (0.8)": 0.8,
            "Полностью (1)": 1,
            "Сверхстрого (1.2)": 1.2
        }

        days = st.number_input("Дней подряд", min_value=1, max_value=365, value=1)

        askesis_list.append({
            "base": base,
            "k": k_map[k],
            "days": days
        })

    inputs["askesis"] = askesis_list
    inputs["gamma"] = 0.1  # базовый реалистичный коэффициент

    

    return inputs