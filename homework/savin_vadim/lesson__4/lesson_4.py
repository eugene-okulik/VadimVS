my_dict = {
    "tuplee": (1, "ttuple", False, 4.42, 11),
    "listt": [2, 22, "llist", True, "я смогу", 2.22],
    "dictt": {
        "intt": 3,
        "textt": "ddict",
        "bool_first": False,
        "bool_second": True,
        "floatt": 3.33,
    },
    "sett": {4, 44, True, "apple", 4.44}
}


# выведите на экран последний элемент
print(my_dict["tuplee"][-1])


# добавьте в конец списка еще один элемент
my_dict["listt"].append("last_element")
# удалите второй элемент списка
my_dict["listt"].pop(1)


# добавьте элемент с ключом ('i am a tuple',) и любым значением
my_dict["dictt"]["i am a tuple"] = "странное название кортеж конечно"
# удалите какой-нибудь элемент
last_items = my_dict["dictt"].pop("textt")


# добавьте новый элемент в множество
my_dict["sett"].add("new")
# удалите элемент из мнOжествa
my_dict["sett"].remove(True)
