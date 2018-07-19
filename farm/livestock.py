def fib(n):
    """Вычисления числа Фибоначчи."""
    a = 2
    b = 3
    for __ in range(n):
        a, b = b, a + b
    return a


def bunnies(day):
    """
    Подсчёт выводка кроликов.
    Кролики размножаются раз в 10 дней в соответствии с числами Фибоначчи.
    """
    how_many_times = day // 10
    return fib(how_many_times)

def cow(day):
    """
    Подсчёт выводка кроликов.
    Кролики размножаются раз в 10 дней в соответствии с числами Фибоначчи.
    """

    cows = 1
    milk = 0
    milk_yield = 550
    max_milk_yeld = 550
    frequency = (day + 2) // 3

    for _ in range(frequency):
        # print(_, frequency, _ % 10)
        if(_ % 10 == 0):
            milk_yield = max_milk_yeld

        milk_yield -= 50
        milk = milk + milk_yield

    how_many_times = day // 3
    return milk