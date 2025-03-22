PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_price_list = {
                x.split(" ")[0]: int(x.split(" ")[1][:-1])
                for x in PRICE_LIST.splitlines()}

print(new_price_list)
