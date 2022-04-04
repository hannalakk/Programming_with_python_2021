names = ['Tallinn', 'Delft', 'Manchester', 'Leiden']
number_of_cities = len(names)
print(number_of_cities)

population = [450000, 90000, 500000, 70000]
cities = [names, population]
print(cities[0][2])

dict_cities = {}

for i in range(number_of_cities):
    dict_cities [cities[0][i]] = cities [1][i]

print(dict_cities)