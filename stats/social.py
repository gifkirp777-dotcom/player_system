def calculate_raw_social(inputs: dict) -> float:
    minutes = inputs.get("minutes", 0)
    intensity = inputs.get("intensity", 1)
    awareness = inputs.get("awareness", 1)
    influence = inputs.get("influence", 1)
    difficulty = inputs.get("difficulty", 1)
    connections = inputs.get("connections", 1)

    return minutes * intensity * awareness * influence * difficulty * connections


def convert_social_to_units(raw_social: float, L: float = 3, k: float = 150) -> float:
    # Units = L × So / (So + k)
    return L * raw_social / (raw_social + k)


def calculate_social(inputs: dict) -> dict:
    raw = calculate_raw_social(inputs)
    units = convert_social_to_units(raw)

    return {
        "raw": raw,
        "units": round(units, 2)
    }