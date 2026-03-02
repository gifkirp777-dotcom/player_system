from stats.finance import calculate_finance
import streamlit as st

from stats.body import calculate_body
from stats.social import calculate_social
from stats.intellect import calculate_intellect
from stats.social import calculate_social
from stats.charisma import calculate_charisma
from stats.spirit import calculate_spirit

def calculate_units(stat, substat, inputs):

    if stat == "Интеллект":
        return calculate_intellect(inputs)

    elif stat == "Сила тела":
        return calculate_body(inputs)

    elif stat == "Социум":
         return calculate_social(inputs)

    elif stat == "Харизма":
         total_charisma = st.session_state.data["stats"].get("Харизма", 0)
         return calculate_charisma(inputs, total_charisma)

    elif stat == "Финансы":
        total_finance = st.session_state.data["stats"].get("Финансы", 0)
        return calculate_finance(inputs, total_finance)

    elif stat == "Сила духа":
        return calculate_spirit(inputs)

    return 0