names = ['Tallinn', 'Delft', 'Manchester', 'Leiden']
number_of_cities = len(names)
print(number_of_cities)

population = [450000, 90000, 500000, 70000]
cities = [names, population]
print(cities[0][2])



if number_of_cities <= 3:
    print('you have lived in 3 cities')
else:
    print('you have lived in many cities')

for i in names:
  print(i)

for i in range(number_of_cities):
    print(cities[0][i], 'has a population of', cities[1][i])
