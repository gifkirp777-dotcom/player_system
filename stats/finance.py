def calculate_raw_finance(inputs: dict, total_finance: float = 0) -> float:
    minutes = inputs.get("minutes", 0)

    creation = inputs.get("creation", 0)
    management = inputs.get("management", 0)
    multiplication = inputs.get("multiplication", 0)
    restraint = inputs.get("restraint", 0)
    influence = inputs.get("influence", 0)
    independence = inputs.get("independence", 0)

    effect_coef = inputs.get("effect_coef", 1)
    external = inputs.get("external", 0)

    elements_sum = (
        creation
        + management
        + multiplication
        + restraint
        + influence
        + independence
    )

    raw = minutes * elements_sum * effect_coef + external

    # =========================
    # АВТО-ОПЫТ (репутация)
    # =========================
    # опыт зависит от накопленного уровня финансов
    if total_finance >= 5000:
        experience = 0.3
    elif total_finance >= 3000:
        experience = 0.2
    elif total_finance >= 1500:
        experience = 0.1
    elif total_finance >= 500:
        experience = 0.05
    else:
        experience = 0.0

    final_result = raw * (1 + experience)

    return final_result


def convert_finance_to_units(raw_finance: float, L: float = 3, k: float = 3000) -> float:
    return L * raw_finance / (raw_finance + k)


def calculate_finance(inputs: dict, total_finance: float = 0) -> dict:
    raw = calculate_raw_finance(inputs, total_finance)
    units = convert_finance_to_units(raw)

    return {
        "raw": raw,
        "units": round(units, 2)
    }