def calculate_raw_intellect(inputs: dict) -> float:
    minutes = inputs.get("minutes", 0)
    load = inputs.get("mental_load", 1)
    awareness = inputs.get("awareness", 1)
    novelty = inputs.get("novelty", 1)
    application = inputs.get("application", 1)

    return minutes * load * awareness * novelty * application


def convert_to_units(raw_intellect: float, L: float = 3, k: float = 110) -> float:
    # Units = L × I / (I + k)
    return L * raw_intellect / (raw_intellect + k)


def calculate_intellect(inputs: dict) -> dict:
    raw = calculate_raw_intellect(inputs)
    units = convert_to_units(raw)

    return {
        "raw": raw,
        "units": round(units, 2)
    }