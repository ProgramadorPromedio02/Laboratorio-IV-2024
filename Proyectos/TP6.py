# TP6
print('TP6\n')

## 1.
print('1.')
my_names = ['Carl', 'Ryder', 'Sweet', 'Smoke', 'César']
print(my_names[1]) # Ryder
print()

## 2.
print('2.')
my_numbers = [24, 67, 81, 32, 12, 45]
my_numbers.append(21)
my_numbers.insert(1, 30)
print(my_numbers)
print()

## 3.
print('3.')
my_frutes = ['banana', 'orange', 'tomate', 'apple', 'melon', 'citron', 'grape']
print(my_frutes)
my_frutes.remove('apple')
print(my_frutes)
print()

## 4.
print('4.')
my_numbers2 = [44, 22, 66, 99, 111]
print(22 in my_numbers2) # True
print(33 in my_numbers2) # False
print(my_numbers2.index(66))
print()

## 5.
print('5.')
my_colors = ['blue', 'red', 'orange', 'green', 'yellow', 'purple', 'pink', 'white', 'black']
print(my_colors)
my_colors[6] = 'violate'
print(my_colors)
print()

## 6.
print('6.')
my_items = ['a', 1, 'c', 'a', 'b', 1, 1, 2, 'b', 3, 'a', 3, 'c', 3, 'b', 1, 'a', 2, 'c', 'b', 'c']
print(f'• 1: {my_items.count(1)}\n• 2: {my_items.count(2)}\n• 3: {my_items.count(3)}\n• a: {my_items.count('a')}\n• b: {my_items.count('b')}\n• c: {my_items.count('c')}\n')

## 7.
print('7.')
my_list1 = [1, 4, 5, 7, 2, 'c']
my_list2 = ['a', 'z', 't', 'r', 3]
print(f'• my_list1: {my_list1}\n• my_list2: {my_list2}')
my_list1.extend(my_list2)
print(f'• my_list1 and my_list2: {my_list1}\n')

## 8.
print('8.')
my_list = [1, 'a', 10, 'z', 'c']
print(my_list)
my_list.pop()
print(my_list)
print()

## 9.
print('9.')
my_list = ['día', 'noche', 'amanecer', 'atardecer', 'biomas', 'biología', 'geografía', 404, 201, 101]
print(my_list)
my_list.reverse()
print(my_list)

## 10.
print('10.')
my_list = [34, 65, 12, 15, 50, 40, 10]
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
