# string
str1 = 'hello python'
str2 = str1
str2 += ' journey'
print(str2 is str1)  # False -> string is immutable

print(str1)  # hello python -> string is immutable

print(len(str1))  # 12

# split by space
result = str2.split(' ')
print(result) # ['hello', 'python', 'journey']

# join by ***
result_back = '***'.join(result)
print(result_back)  # hello***python***journey

# The string first char
str3 = 'abcd'
print(str3[0])  # can print the first char, but cant set it.
