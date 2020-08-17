from decimal import Decimal, ROUND_UP

ROUND_PRECISION='.1'

def round_up(num):
    "Rounds up the given number to match up to the nearest 0.05"
    return float(Decimal(num * 2).quantize(Decimal(ROUND_PRECISION), rounding=ROUND_UP) / 2)

