#!/usr/local/bin/python3

from Can import Can

drinks = []

drink1 = Drink()
drink2 = Drink()

drink1.name = 'margarita'

drinks.append(drink1)

print(f'{drinks[0].name}')