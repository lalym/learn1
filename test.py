#Словарь, в котором ключи - имена людей, а значения - словари с ключами city, temperature, wind
mydict={'Mike':
            {'city': 'New York', 'temperature': '26', 'wind': 'NW'},
        'Peter':
            {'city': 'Boston', 'temperature': '23', 'wind': 'EW'},
        "John":
            {'city': 'Montreal', 'temperature': '24', 'wind': 'SW'}}
name = input('Are you Mike or Peter or John? Please choose one: ')
print('Hi, my friend '+ name)
user = mydict.get(name)
if user:
    print(user['city'], user['temperature'], user['wind'])
else:
    print('Try again, please.')

