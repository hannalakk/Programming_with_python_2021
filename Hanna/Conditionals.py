my_city_name = 'Hanna town'
my_city_population = 6500000
my_other_city_name = 'Barcelona'
my_other_city_population = 5500000

if my_city_population > 10000000:
    print('My city is a Megacity')

elif my_city_population > 1500000:
    print('My city is metropol')
    if my_city_population > my_other_city_population:
        result = my_city_name + ' is bigger than ' + my_other_city_name
        print(result)

else:
    print('My city is not a megacity or metropol')