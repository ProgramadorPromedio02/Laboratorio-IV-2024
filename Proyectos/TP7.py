# TP7
print('TP7\n')

## 1.
print('1.')
my_tuple = (2, 5, 7, 9, 11)
print(my_tuple[3]) # 9
print()

## 2.
print('2.')
my_frutes = ('banana', 'apple', 'orange', 'cherry', 'citron', 'grape')
print('grape' in my_frutes) # True
print('melon' in my_frutes) # False
print(my_frutes.index('apple')) # 1

## 3.
print('3.')
my_items = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c')
print(f'• 1: {my_items.count(1)}\n• 2: {my_items.count(2)}\n• 3: {my_items.count(3)}\n• a: {my_items.count('a')}\n• b: {my_items.count('b')}\n• c: {my_items.count('c')}\n')

## 4.
print('4.')
my_tuple = ('world', 'table', 'girl', 'boy', 'wood', 'summer', 'city', 'town', 'jungle', 'tropical', 'desert')
print(my_tuple[-2])
print()

## 5.
print('5.')
my_numbers = (1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 1, 7, 2, 7, 4, 5, 3)
print(f'• 7: {my_numbers.count(7)}\n')

## 6.
print('6.')
my_colors = ('red', 'blue', 'green', 'yellow', 'pink', 'black', 'white', 'orange', 'purple')
print('verde' in my_colors) # False
print('green' in my_colors) # True
print()