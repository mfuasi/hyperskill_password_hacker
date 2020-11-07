import itertools

for meal, price in zip(
        itertools.product(main_courses, desserts, drinks),
        itertools.product(price_main_courses, price_desserts, price_drinks)):
    if 30 >= sum(price):
        print(*meal, sum(price))
