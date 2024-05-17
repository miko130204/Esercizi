#2

def transform(x: int) -> int:
    if x % 2 == 0:
        x /= 2
    elif x % 2 != 0:
        x *= 3
        x -= 1
    return x


#3

def calcola_stipendio(ore_lavorate: int) -> float:
    if ore_lavorate <= 40:
        stipendio = ore_lavorate * 10
    elif ore_lavorate > 40:
        ore_extra = ore_lavorate - 40
        stipendio_extra = ore_extra * 15
        stipendio_40 = 40 * 10
        stipendio = stipendio_40 + stipendio_extra
    return stipendio


#4

def print_seq(): 
    
    print("Sequenza a):")
    x = 1
    i = 0
    while i < 7:
        i += 1
        print(x)
        x += 1
    print()

    print("Sequenza b):")
    x = 3
    i = 0
    while i < 5:
        i += 1
        print(x)
        x += 5
    print()

    print("Sequenza c):")
    x = 20
    i = 0
    while i < 6:
        i += 1
        print(x)
        x -= 6
    print()

    print("Sequenza d):")
    x = 19
    i = 0
    while i < 5:
        i += 1
        print(x)
        x += 8
    print()
    
    return


#5

def integerPower(base: int, exp: int) -> int:
    i = exp
    b = base
    while i > 1:
        base *= b
        i -= 1
    return base


#6

import math

def hypotenuse(base: float, height: float) -> float:
    hyp = (base**2) + (height**2)
    hypotenuse = math.sqrt(hyp)
    return hypotenuse

#7

def find_element(lst: list[int], element: int) -> bool:
    for item in lst:
        if item == element:
            return True
    return False


#8

def seconds_since_noon(h: int, m: int, s: int) -> int:
    h_sec: int = (h * 60) * 60
    m_sec: int = m * 60
    time_sec: int = h_sec + m_sec + s
    return time_sec
    
def time_difference(h1: int, m1: int, s1: int, h2: int, m2: int, s2: int):
    h_sec: int = (abs(h1 - h2) * 60) * 60 
    m_sec: int = abs(m1 - m2) * 60
    sec: int = abs(s1 - s2)
    time_sec = h_sec + m_sec + sec
    return time_sec