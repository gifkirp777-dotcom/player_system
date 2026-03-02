import streamlit as st


def render_finance_ui():
    inputs = {}

    st.markdown("## 💰 Параметры финансового действия")

    # ВРЕМЯ
    inputs["minutes"] = st.number_input(
        "⏱ Время финансовой активности (минут)",
        min_value=0,
        max_value=1000,
        value=60,
        step=1,
        key="fin_minutes"
    )

    scale = {
        "0 — отсутствует": 0,
        "0.5 — слабое участие": 0.5,
        "1 — стандартный уровень": 1,
        "1.2 — усиленный уровень": 1.2,
        "1.5 — максимальный вклад": 1.5
    }

    def select_block(title, key):
        st.markdown(f"### {title}")
        value = st.selectbox(title, list(scale.keys()), key=key)
        return scale[value]

    inputs["creation"] = select_block("Созидание", "fin_creation")
    inputs["management"] = select_block("Управление", "fin_management")
    inputs["multiplication"] = select_block("Умножение", "fin_multiplication")
    inputs["restraint"] = select_block("Сдержанность", "fin_restraint")
    inputs["influence"] = select_block("Влияние", "fin_influence")
    inputs["independence"] = select_block("Независимость", "fin_independence")

    # КОЭФФИЦИЕНТ ЭФФЕКТА
    effect_map = {
        "Минимальный эффект (0.5)": 0.5,
        "Обычное действие (1)": 1,
        "Значимое действие (1.5)": 1.5,
        "Ключевое действие (2)": 2
    }

    st.markdown("### 📈 Коэффициент эффекта")
    effect_choice = st.selectbox("Насколько значимо действие?", list(effect_map.keys()))
    inputs["effect_coef"] = effect_map[effect_choice]

 # =========================
    # ВНЕШНИЕ УСЛОВИЯ
    # =========================
    external_map = {
        "Сильный негатив (рыночный кризис, потери) (-0.5)": -0.5,
        "Небольшой негатив (-0.3)": -0.3,
        "Без изменений (0)": 0,
        "Удачное сотрудничество (+0.3)": 0.3,
        "Сильный позитив (бонус, прорыв) (+0.5)": 0.5
    }

    st.markdown("### 🌍 Внешние условия")

    external_choice = st.selectbox(
        "Как повлияла внешняя среда?",
        list(external_map.keys()),
        key="fin_external"
    )

    inputs["external"] = external_map[external_choice]

    

    return inputs