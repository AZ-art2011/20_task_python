# Задача 20.

list_str = [['A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т'],
            ['Д, К, Л, М, П, У, D, G'],
            ['B, C, M, P, Б, Г, Ё, Ь, Я'],
            ['F, H, V, W, Y, Й, Ы'],
            ['K, Ж, З, Х, Ц, Ч'],
            ['J, X, Ш, Э, Ю'],
            ['Q, Z, Ф, Щ, Ъ']]
price_list = [1, 2, 3, 4, 5, 8, 10]
dict_price = {}

for o, i in enumerate(list_str):
    list_symb = (str(i).replace(',', '').split())
    
    for j in list_symb:
        symb = (j.replace("['", '').replace("']", ''))
        dict_price[symb] = price_list[o]

string_1 = (input('Введите текст для подсчета стоимости символов: '))
string_1 = string_1.upper()
price = 0

for i in list(string_1):
    price = price + dict_price[i]

print(f'Стоимость строки = {price}')
