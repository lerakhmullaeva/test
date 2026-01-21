def add_numbers(a: float, b: float) -> float:
    return a + b

def dishes(big_pizza: int, medium_pizza: int, juice: int, cake: int, water: int) -> int:
    return (big_pizza * 4) + (medium_pizza * 2) + (juice * 4) + cake + (water * 3)


def photobook(total_photos: int, max_photo_per_page: int) -> int:
    return (total_photos + max_photo_per_page - 1) // max_photo_per_page


def garden(boys: int, sick_boys: int, absent_girl: int) -> int:
    girls = boys // 2
    return (boys - sick_boys) + (girls - absent_girl)


def temperature(before_lunch_t: int) -> int:
    after_lunch_t = before_lunch_t - 10
    afternoon_t = after_lunch_t + 4
    return afternoon_t
