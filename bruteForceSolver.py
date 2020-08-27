from numpy import arange

checkRange = [-10000, 10000]

precision = 0.5

answers = []

for x in arange(checkRange[0], checkRange[1], 1):
    Eq = x**2 - 4*x + 3
    if Eq <= precision and Eq >= -precision:
        answers.append(x)

for item in answers:
    print(item)
