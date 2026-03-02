def calculate_raw_charisma(inputs: dict, total_charisma: float = 0) -> float:
    minutes = inputs.get("minutes", 0)

    presence = inputs.get("presence", 0)
    expressiveness = inputs.get("expressiveness", 0)
    empathy = inputs.get("empathy", 0)
    charm = inputs.get("charm", 0)
    persuasion = inputs.get("persuasion", 0)
    brand = inputs.get("brand", 0)

    situation_coef = inputs.get("situation_coef", 1)

    elements = [
        presence,
        expressiveness,
        empathy,
        charm,
        persuasion,
        brand
    ]

    elements_sum = sum(elements)

    # =========================
    # АВТО-СИНЕРГИЯ
    # =========================
    strong_elements = len([e for e in elements if e >= 1])

    if strong_elements >= 4:
        synergy_bonus = 0.5
    elif strong_elements == 3:
        synergy_bonus = 0.3
    elif strong_elements == 2:
        synergy_bonus = 0.1
    else:
        synergy_bonus = 0

    # =========================
    # ФОНОВАЯ ХАРИЗМА
    # =========================
    if total_charisma >= 2000:
        background = 0.5
    elif total_charisma >= 1000:
        background = 0.3
    elif total_charisma >= 600:
        background = 0.2
    elif total_charisma >= 300:
        background = 0.15
    elif total_charisma >= 150:
        background = 0.1
    elif total_charisma >= 50:
        background = 0.05
    else:
        background = 0.0

    raw = minutes * ((elements_sum * situation_coef) + synergy_bonus) * (1 + background)

    return raw


def convert_charisma_to_units(raw_charisma: float, L: float = 3, k: float = 700) -> float:
    return L * raw_charisma / (raw_charisma + k)


def calculate_charisma(inputs: dict, total_charisma: float = 0) -> dict:
    raw = calculate_raw_charisma(inputs, total_charisma)
    units = convert_charisma_to_units(raw)

    return {
        "raw": raw,
        "units": round(units, 2)
    }