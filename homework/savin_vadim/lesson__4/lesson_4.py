my_dict = {"tuplee":(1, "ttuple", False, 4.42, 11),
           "listt":[2,22,"llist", True,"я смогу", 2.22],
           "dictt":{"intt":3,"textt":"ddict","bool_first":False, "bool_second":True,"floatt":3.33},
           "sett":{4,44,True,"apple", 4.44}}
print(my_dict["tuplee"][-1])

my_dict["listt"].append("last_element")
my_dict["listt"].pop(1)


my_dict["dictt"]["i am a tuple"] = "странное название кортеж конечно"
last_items = my_dict["dictt"].pop("textt")
print(my_dict["dictt"])

# print(my_dict["dictt"][-1] )
print(type(my_dict["sett"]))
