
dict_homework = {
    "key1":{
        "d":44,
        "f":None,
        "s":{
            8:44,
            9:None,
            10:{"mm":["s", "GET ME", 7]},
        },
    },
    "key2":{
        "fff1":44,
        "f":None,
    },
}

#variant1
x=dict_homework['key1']['s']
y=(x[10])
print(y['mm'][1])

#variant2
print(dict_homework['key1']['s'][10]['mm'][1])
