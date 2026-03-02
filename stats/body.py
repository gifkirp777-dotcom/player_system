def calculate_body(inputs):
    SB_raw = (
        inputs["time"]
        * inputs["intensity"]
        * inputs["result"]
    )

    L = 3
    k = 60

    return L * SB_raw / (SB_raw + k) if SB_raw > 0 else 0