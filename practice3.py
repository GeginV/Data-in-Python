print('='*5, '12.5.11', '='*5)

name_of_book = input('give name')
print(type(name_of_book))
suname_of_author = input('give surname')
print(type(suname_of_author))
year_publish = int(input('give year'))
print(type(year_publish))

dict = {'name_of_book': name_of_book,
        'suname_of_author' : suname_of_author,
        'year_publish' : year_publish}

print(dict)