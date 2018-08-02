def answer(panels):
    if len(panels) == 1:
        return str(panels[0])

    positives_multiplied = 1
    positives_count = 0
    zeros_found = False
    negatives = []

    for panel_power in panels:
        if panel_power > 0:
            positives_multiplied *= panel_power
            positives_count += 1
        elif panel_power < 0:
            negatives.append(panel_power)
        else:
            zeros_found = True

    neg_count = len(negatives)

    if positives_count == 0 and neg_count % 2 != 0 and zeros_found:
        return "0"
    elif neg_count == 0:
        return str(positives_multiplied)
    elif neg_count % 2 == 0:
        return str(reduce(lambda x, y: x * y, negatives) * positives_multiplied)
    else:
        negatives.sort()
        return str(reduce(lambda x, y: x * y, negatives[:-1]) * positives_multiplied)


assert answer([2, 0, 2, 2, 0]) == "8"
assert answer([-2, -3, 4, -5]) == "60"
