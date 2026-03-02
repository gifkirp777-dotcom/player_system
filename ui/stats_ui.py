import streamlit as st

from core.power_system import calculate_power
from core.rank_system import update_rank
from core.data_manager import save_data
from core.unit_router import calculate_units

from ui.body_ui import render_body_ui
from ui.intellect_ui import render_intellect_ui
from ui.social_ui import render_social_ui
from ui.charisma_ui import render_charisma_ui
from ui.finance_ui import render_finance_ui
from ui.spirit_ui import render_spirit_ui

def render_stats_tab():

    # ===============================
    # УРОВЕНЬ 1 — ВЫБОР СТАТА
    # ===============================

    if st.session_state.active_stat is None:

        st.markdown("<h2 style='text-align:center'>⚔ Выбери направление</h2>", unsafe_allow_html=True)

        stats_list = [
            "Сила тела",
            "Интеллект",
            "Социум",
            "Сила духа",
            "Харизма",
            "Финансы"
        ]

        cols = st.columns(2)

        for i, stat in enumerate(stats_list):
            if cols[i % 2].button(
                f"{stat}\n\n{round(st.session_state.data['stats'].get(stat, 0),2)}",
                use_container_width=True,
                key=f"stat_btn_{stat}"
            ):
                st.session_state.active_stat = stat
                st.session_state.active_substat = None
                st.rerun()

    # ===============================
    # УРОВЕНЬ 2 — ПОДСТАТЫ
    # ===============================

    elif st.session_state.active_substat is None:

        stat = st.session_state.active_stat

        st.markdown(f"<h2 style='text-align:center'>{stat}</h2>", unsafe_allow_html=True)

        substats_map = {
            "Сила тела": ["Сила", "Выносливость", "Гибкость", "Скорость", "Контроль"],
            "Интеллект": ["Осознание", "Навыки", "Структура", "Творчество", "Контроль"],
            "Социум": ["Образ", "Репутация", "Пластичность", "Эмпатия", "Лидерство", "Стратегия", "Связи"],
            "Сила духа": ["Ясность", "Выдержка", "Дисциплина", "Цель", "Стойкость", "Трансформация"],
            "Харизма": ["Присутствие", "Выразительность", "Эмпатия", "Обаяние", "Убеждение", "Бренд"],
            "Финансы": ["Созидание", "Управление", "Умножение", "Сдержанность", "Влияние", "Независимость"]
        }

        cols = st.columns(2)

        key_name = f"{stat}_substats"
        substats_data = st.session_state.data.get(key_name, {})

        for i, sub in enumerate(substats_map[stat]):

           value = substats_data.get(sub, 0)

           button_label = f"{sub}  ({round(value, 2)})"

           if cols[i % 2].button(
              button_label,
              use_container_width=True,
              key=f"sub_btn_{stat}_{sub}"
           ):
               st.session_state.active_substat = sub
               st.rerun()

        st.markdown("---")

        if st.button("⬅ Назад", use_container_width=True):
            st.session_state.active_stat = None
            st.rerun()

    # ===============================
    # УРОВЕНЬ 3 — ПАРАМЕТРЫ
    # ===============================

    else:

        stat = st.session_state.active_stat
        substat = st.session_state.active_substat

        st.markdown(f"<h2 style='text-align:center'>{stat}</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align:center'>{substat}</h3>", unsafe_allow_html=True)

        inputs = {}

        if stat == "Интеллект":
            inputs = render_intellect_ui()

        elif stat == "Сила тела":
            inputs = render_body_ui()

        elif stat == "Социум":
            inputs = render_social_ui()

        elif stat == "Харизма":
            inputs = render_charisma_ui()

        elif stat == "Финансы":
            inputs = render_finance_ui()

        elif stat == "Сила духа":
            inputs = render_spirit_ui()

        if st.button("⚔ Зафиксировать", use_container_width=True):

            result = calculate_units(stat, substat, inputs)

            # 🔥 Универсальная обработка результата
            if isinstance(result, dict):
                units = result.get("units", 0)
            else:
                units = result

            key_name = f"{stat}_substats"

            if key_name not in st.session_state.data:
                st.session_state.data[key_name] = {}

            if substat not in st.session_state.data[key_name]:
                st.session_state.data[key_name][substat] = 0

            st.session_state.data[key_name][substat] += units

            total = sum(st.session_state.data[key_name].values())
            st.session_state.data["stats"][stat] = total

            new_power = calculate_power(st.session_state.data["stats"])
            st.session_state.data["stats"]["Власть"] = new_power

            new_rank = update_rank(st.session_state.data)
            st.session_state.data["rank"] = new_rank

            save_data(st.session_state.data)

            st.session_state.active_stat = None
            st.session_state.active_substat = None

            st.rerun()

        st.markdown("---")

        if st.button("⬅ Назад", use_container_width=True):
            st.session_state.active_substat = None
            st.rerun()