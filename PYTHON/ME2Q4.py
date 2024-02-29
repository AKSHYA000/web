"""
Python Program to concatenate string with uncommon characters in Python
"""
str1 = input('String1 : ')
str2 = input('String2 : ')
str1 , str2 = set(str1), set(str2)
uncommon = str1.symmetric_difference(str2)
final_str = ''.join(uncommon)
print(final_str)