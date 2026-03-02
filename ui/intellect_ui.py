import streamlit as st


def render_intellect_ui():
    inputs = {}

    st.markdown("## 🧠 Параметры умственной работы")

    # =========================
    # ВРЕМЯ
    # =========================
    inputs["minutes"] = st.number_input(
        "⏱ Время работы (минут)",
        min_value=0,
        max_value=500,
        value=30,
        step=1,
        key="intel_minutes"
    )

    # =========================
    # УМСТВЕННАЯ НАГРУЗКА
    # =========================
    load_map = {
        "Лёгкая (0.5)": 0.5,
        "Средняя (1)": 1,
        "Сильная (1.5)": 1.5,
        "Очень высокая (2)": 2
    }

    if "intel_load" not in st.session_state:
        st.session_state["intel_load"] = 1

    st.markdown("### 🔥 Умственная нагрузка")

    cols = st.columns(2)

    for i, (label, value) in enumerate(load_map.items()):
        active = st.session_state["intel_load"] == value
        btn_label = f"▶ {label}" if active else label

        with cols[i % 2]:
            if st.button(btn_label, use_container_width=True, key=f"load_{i}"):
                st.session_state["intel_load"] = value
                st.rerun()

    inputs["mental_load"] = st.session_state["intel_load"]

    # =========================
    # ОСОЗНАННОСТЬ
    # =========================
    awareness_map = {
        "Поверхностно (0)": 0,
        "Понял (1)": 1,
        "Записал и могу объяснить (1.5)": 1.5
    }

    if "intel_awareness" not in st.session_state:
        st.session_state["intel_awareness"] = 1

    st.markdown("### 🧩 Осознанность")

    cols = st.columns(2)

    for i, (label, value) in enumerate(awareness_map.items()):
        active = st.session_state["intel_awareness"] == value
        btn_label = f"▶ {label}" if active else label

        with cols[i % 2]:
            if st.button(btn_label, use_container_width=True, key=f"aware_{i}"):
                st.session_state["intel_awareness"] = value
                st.rerun()

    inputs["awareness"] = st.session_state["intel_awareness"]

    # =========================
    # НОВИЗНА
    # =========================
    novelty_map = {
        "Повтор старого (0.8)": 0.8,
        "Новый материал (1)": 1,
        "Меняет мировоззрение (1.3)": 1.3
    }

    if "intel_novelty" not in st.session_state:
        st.session_state["intel_novelty"] = 1

    st.markdown("### 🌱 Новизна")

    cols = st.columns(2)

    for i, (label, value) in enumerate(novelty_map.items()):
        active = st.session_state["intel_novelty"] == value
        btn_label = f"▶ {label}" if active else label

        with cols[i % 2]:
            if st.button(btn_label, use_container_width=True, key=f"novelty_{i}"):
                st.session_state["intel_novelty"] = value
                st.rerun()

    inputs["novelty"] = st.session_state["intel_novelty"]

    # =========================
    # ПРИМЕНЕНИЕ
    # =========================
    application_map = {
        "Не применил (0.5)": 0.5,
        "Понял теорию (1)": 1,
        "Применил на практике (1.5)": 1.5
    }

    if "intel_application" not in st.session_state:
        st.session_state["intel_application"] = 1

    st.markdown("### ⚙ Применение")

    cols = st.columns(2)

    for i, (label, value) in enumerate(application_map.items()):
        active = st.session_state["intel_application"] == value
        btn_label = f"▶ {label}" if active else label

        with cols[i % 2]:
            if st.button(btn_label, use_container_width=True, key=f"application_{i}"):
                st.session_state["intel_application"] = value
                st.rerun()

    inputs["application"] = st.session_state["intel_application"]

    
    return inputs