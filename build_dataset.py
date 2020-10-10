import pandas as pd
import json
import csv
from random import choice
from random import randint

with open('Data/city.json', 'r') as f:
    city = json.load(f)

# price = $5-$25
# Soda, Lemonade, Tea within $8
# Juice, Milkshake, Coffee, wine within $25
# sell count = 0-15000

cities = [x for x, y in city.items()]
burgers = ['Naga Burger', 'The Burger Barn', 'Burger Bros', 'Beefy Burgers', 'Vegan Burger']
sandwiches = ['Chicken Sandwich', 'Sam Sandwich', 'Double Bee Sandwich', 'Golden Sandwich', 'Club Sandwich',
              'Vegan Sandwich']
beverages = ['Cold Tea', 'Hot Coffee', 'Coffeliano', 'Icead Tea', 'Lemonade', 'Milkshake', 'Mango Juice',
             'Hot Chocolate', 'Wine', 'Soda', 'Chocolate Milk']
cheese = [0, 1, 2, '']
bacon = ['yes', 'no', '']
lettuce = ['yes', 'no', '']
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# food_type, name, year, month, cheese, bacon, lettuce, price, sell_count

if __name__ == '__main__':
    arr = []
    for burger in burgers:
        for year in years:
            for month in months:
                cur_cheese = choice(cheese)
                cur_bacon = choice(bacon)
                cur_lettuce = choice(lettuce)
                cur_price = randint(5, 25)
                cur_sell_count = randint(0, 15000)
                d = [1, burger, year, month, cur_cheese, cur_bacon, cur_lettuce, cur_price, cur_sell_count]
                arr.append(d)
    df = pd.DataFrame(arr, columns=['food_type', 'name', 'year', 'month', 'cheese', 'bacon', 'lettuce', 'price',
                                    'sell_count'])
    df.to_csv('Data/dataset.csv', index=False)
    """d = []
    with open('Data/dataset.csv', 'a', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(d)"""
