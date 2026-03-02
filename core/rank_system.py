def update_rank(data):
    total = sum(data["stats"].values())

    if total >= 6000:
        return "A"
    elif total >= 3500:
        return "B"
    elif total >= 1500:
        return "C"
    elif total >= 700:
        return "D"
    else:
        return "E"