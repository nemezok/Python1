from farm import plants
import farm.livestock as lvst


def economy(current_day, order, ec_d):
    """Составление отчета."""
    ec_d['corns'] = plants.corn(current_day)
    ec_d['bunnies'] = lvst.bunnies(current_day)

    ec_d['cows'] = lvst.cow(current_day)
    ec_d['berrybush'] = plants.berrybush(current_day)

    ec_d['berrybush'] = plants.berrybush(current_day)

    report = 'There are\n {} corns\n {} bunnies\n {} milk\n {} bushes, {} berries'.\
        format(ec_d['corns'],
               ec_d['bunnies'],
               ec_d['cows'],
               ec_d['berrybush'][0],
               ec_d['berrybush'][1]
               )
    return report


if __name__ == '__main__':
    """
    Модуль управления фермой.
    Выводит отчет о запасах на ферме в определенном интервале дней.
    """
    days = 60
    house_economy = {
        'corns': 0,
        'bunnies': 0
    }
    for day in range(0, days + 1):
        print("Day №", day)
        print(economy(day, day % 30, house_economy))
        print('---' * 10)
