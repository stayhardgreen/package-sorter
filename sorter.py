# sorter.py

BULKY_VOLUME_THRESHOLD = 1_000_000
BULKY_DIM_THRESHOLD = 150
HEAVY_MASS_THRESHOLD = 20

def sort(width, height, length, mass):
    for v in (width, height, length, mass):
        if v is None:
            raise ValueError("Inputs cannot be None")
        if not isinstance(v, (int, float)):
            raise TypeError("Inputs must be numbers")
        if v < 0:
            raise ValueError("Inputs cannot be negative")

    volume = width * height * length
    bulky = (
        volume >= BULKY_VOLUME_THRESHOLD
        or width >= BULKY_DIM_THRESHOLD
        or height >= BULKY_DIM_THRESHOLD
        or length >= BULKY_DIM_THRESHOLD
    )
    heavy = mass >= HEAVY_MASS_THRESHOLD

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
