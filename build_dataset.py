import pandas as pd
import json
import csv
from random import choice
from random import randint
from random import uniform
from math import ceil

cities = ['Las Vegas', 'San Francisco', 'New York', 'Greensboro', 'Boca Raton', 'Morristown']
burgers = ['Naga Burger', 'The Burger Barn', 'Burger Bros', 'Beefy Burgers', 'Vegan Beef Burger']
sandwiches = ['Vegan Chicken Sandwich', 'Sam Sandwich', 'Double Bee Sandwich', 'Golden Sandwich']
beverages = ['Cold Tea', 'Hot Coffee', 'Coffeliano', 'Iced Tea', 'Lemonade', 'Milkshake', 'Mango Juice',
             'Hot Chocolate', 'Wine', 'Soda', 'Chocolate Milkshake']
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

burgers_ini_price_high = dict()
burgers_ini_price_high['Naga Burger'] = [5, 1223, 10]
burgers_ini_price_high['Burger Bros'] = [3, 1501, 9]
burgers_ini_price_high['Beefy Burgers'] = [4, 1265, 10]
burgers_ini_price_high['Bacon Blast'] = [3, 1694, 8]
burgers_ini_price_high['Vegan Beef Burger'] = [5, 69, 15]
burgers_ini_price_high['The Burger Barn'] = [2, 630, 7]

burgers_ini_price_low = dict()
burgers_ini_price_low['Naga Burger'] = [3, 322, 5]
burgers_ini_price_low['Burger Bros'] = [2, 542, 4]
burgers_ini_price_low['Beefy Burgers'] = [2, 635, 7]
burgers_ini_price_low['Bacon Blast'] = [2, 321, 3]
burgers_ini_price_low['Vegan Beef Burger'] = [8, 5, 30]
burgers_ini_price_low['The Burger Barn'] = [3, 235, 8]

sandwiches_high = dict()
sandwiches_high['Vegan Chicken Sandwich'] = [7, 1232, 25]
sandwiches_high['Sam Sandwich'] = [2, 1671, 15]
sandwiches_high['Double Bee Sandwich'] = [3, 1475, 8]
sandwiches_high['Golden Sandwich'] = [4, 1844, 10]

sandwiches_low = dict()
sandwiches_low['Vegan Chicken Sandwich'] = [3, 322, 35]
sandwiches_low['Sam Sandwich'] = [2, 542, 10]
sandwiches_low['Double Bee Sandwich'] = [2, 635, 7]
sandwiches_low['Golden Sandwich'] = [2, 321, 6]

beverages_high = dict()
beverages_high['Cold Tea'] = [4, 3223, 7]
beverages_high['Hot Coffee'] = [4, 4501, 8]
beverages_high['Coffeliano'] = [5, 1265, 10]
beverages_high['Iced Tea'] = [5, 6694, 8]
beverages_high['Lemonade'] = [3, 3931, 5]
beverages_high['Milkshake'] = [5, 2630, 10]
beverages_high['Mango Juice'] = [5, 5222, 9]
beverages_high['Hot Chocolate'] = [7, 1522, 11]
beverages_high['Wine'] = [20, 3637, 30]
beverages_high['Soda'] = [3, 2321, 5]
beverages_high['Chocolate Milkshake'] = [6, 1253, 10]

beverages_low = dict()
beverages_low['Cold Tea'] = [1, 2215, 3]
beverages_low['Hot Coffee'] = [2, 1272, 4]
beverages_low['Coffeliano'] = [2, 1235, 6]
beverages_low['Iced Tea'] = [1, 3655, 3]
beverages_low['Lemonade'] = [1, 1109, 2]
beverages_low['Milkshake'] = [2, 625, 4]
beverages_low['Mango Juice'] = [3, 2795, 4]
beverages_low['Hot Chocolate'] = [2, 1532, 4]
beverages_low['Wine'] = [25, 6754, 35]
beverages_low['Soda'] = [1, 2351, 2]
beverages_low['Chocolate Milkshake'] = [3, 875, 10]

# 3223 4501 1265 6694 3931 2630 5222 1522 3637 2321 1253

# food_type, name, year, month, city, cheese, bacon, lettuce, price, sell_count

if __name__ == '__main__':
    arr = []
    for city in cities[:3]:
        for beverage in beverages:
            price = beverages_high[beverage][0]
            sell_count = int()
            for year in years:
                for month in months:
                    if month == 'jan' and year == 2000:
                        cur_price = price
                        cur_sell_count = beverages_high[beverage][1]
                        sell_count = cur_sell_count
                    else:

                        x = price - ((price * 10) / 100)
                        y = price + ((price * 15) / 100)

                        price = max(min(uniform(x, y), beverages_high[beverage][2]),
                                    beverages_high[beverage][0])
                        cur_price = price

                        x = sell_count - ((sell_count * 15) / 100)
                        y = sell_count + ((sell_count * 15) / 100)
                        tmp = randint(int(x), int(y))
                        sell_count = tmp if tmp != 0 else 5
                        cur_sell_count = sell_count

                    d = [3, beverage, year, month, city, float("{:.2f}".format(cur_price)), cur_sell_count]
                    print(d)
                    arr.append(d)
    df = pd.DataFrame(arr, columns=['food_type', 'name', 'year', 'month', 'city', 'price', 'sell_count'])
    df.to_csv('Data/dataset.csv', index=False)

    """for burger in burgers:
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
    df.to_csv('Data/dataset_sample.csv', index=False)
    d = []
    with open('Data/dataset_sample.csv', 'a', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(d)"""
