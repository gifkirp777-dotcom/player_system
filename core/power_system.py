def calculate_power(stats):
    V = (
        stats["Сила тела"]**0.9 +
        stats["Интеллект"]**1.0 +
        stats["Социум"]**0.97 +
        stats["Харизма"]**0.97 +
        stats["Финансы"]**0.98
    )
    return round(V, 2)