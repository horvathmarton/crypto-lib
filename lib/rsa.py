def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a

def egcd(a: int, b: int) -> tuple[int, int, int]:
    if not a:
        return b, 0, 1

    gcd, x1, y1 = egcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def modinv(g: int, p: int) -> int:
    return pow(g, -1, p)
