import math


# =========================
# 1 ЧАСТЬ — СС ЭЛЕМЕНТА
# =========================
def calculate_spirit_element(inputs: dict) -> float:
    minutes = inputs.get("minutes", 0)
    intensity = inputs.get("intensity", 1)
    awareness = inputs.get("awareness", 1)
    context = inputs.get("context", 1)
    emotional_control = inputs.get("emotional_control", 1)
    transformation = inputs.get("transformation", 1)

    return (
        minutes
        * intensity
        * awareness
        * context
        * emotional_control
        * transformation
    )


# =========================
# 2 ЧАСТЬ — АСКЕЗЫ
# =========================
def calculate_spirit_askesis(askesis_list: list, gamma: float = 0.1) -> float:
    """
    askesis_list = [
        {"base": 1.5, "k": 1, "days": 10},
        ...
    ]
    """

    if not askesis_list:
        return 0

    values = []

    for a in askesis_list:
        base = a.get("base", 1)
        k = a.get("k", 1)
        days = a.get("days", 1)

        ai = base * k * math.sqrt(days)
        values.append(ai)

    ss_sum = sum(values)

    N = len(askesis_list)

    weakening_coef = 1 / (1 + gamma * (N - 1))

    return ss_sum * weakening_coef


# =========================
# 3 ОБЩАЯ СУММА
# =========================
def calculate_spirit(inputs: dict) -> dict:

    element_part = calculate_spirit_element(inputs)

    askesis_list = inputs.get("askesis", [])
    gamma = inputs.get("gamma", 0.1)

    askesis_part = calculate_spirit_askesis(askesis_list, gamma)

    SS = element_part + askesis_part

    # =========================
    # НОРМАЛИЗАЦИЯ (L=3, k=120)
    # =========================
    L = 3
    k = 120

    units = L * SS / (SS + k) if SS > 0 else 0

    return {
        "raw": SS,
        "units": round(units, 2)
    }