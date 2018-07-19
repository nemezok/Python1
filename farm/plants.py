import random


def sowing(grains):
    """
    Случайное засевание поля.
    0 - ничего не выросло, 1 - урожайная ячейка.
    """
    field = []
    for _ in range(grains):
        i = random.randint(0, 1)
        field.append(i)
    #return field
    return [random.randint(0, 1) for _ in range(grains)]


def corn(day):
    """Подсчёт початков кукурузы."""
    grains = (day + 1) * 2
    harvest = sowing(grains)
    counter = 0
    for corns in harvest:
        if corns == 1:
            counter += 1
    return counter

def berrybush(day):
    berries = 0
    coef = 1
    bush = 1
    newbush = 1
    frequency = day // 15

    for _ in range(frequency):
        newbush = bush * 15
        coef -= bush / newbush
        bush = newbush

    return [bush, random.randint(int(bush * coef * 50), int(bush * coef * 100))]

    #return [bush, berries]
