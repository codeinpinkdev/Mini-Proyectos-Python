#Inicializar un conjunto
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

#Conjunto a partir de strings
set_from_string = set('hoola')
print(set_from_string)

#Cambiar tupla a conjunto.
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

#Lista a conjunto.
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
