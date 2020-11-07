def tallest_people(**people):
    print(*sorted(f'{key} : {value}' for key, value in people.items()
                  if value == max(people.values())), sep='\n')


