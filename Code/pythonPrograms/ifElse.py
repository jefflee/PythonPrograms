grade = 90

# if...else -> there's no ()
if grade >= 90:
    print('Excellent!')
elif grade >= 60:
    print('Good enough!')
else:
    print('Loser!')

####################################################################
h = 180
w = 85
grade = 80

# 身高超過175或是體重超過80，看起來就很大隻
if h > 175 or w > 80:
    print('big dude')

# 成績高於70但是不高於90，就是個普通學生
if grade > 70 and grade < 90:
    print('noraml')

grade = 50
# simplify chained comparison
if 0 < grade <= 70:
    print('low')