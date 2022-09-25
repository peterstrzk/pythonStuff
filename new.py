names = [] 
sizes = []

#append and zip names and sizes
def name_input(name, size):
    names.append(name)
    print(names)
    sizes.append(size)
    c = zip(names, sizes)
    return c
    # result_c = dict(c)
    # for k, v in result_c.items():
    #     print(k, v)

#putting zipped stuff into dictionary
def zipped(c):
    result_c=dict(c)
    print(result_c)
    for k, v in result_c.items():
        print(k, v)
        
#looping with input condition
shouldend = False
while not shouldend:
    a = input("type a name \n")
    b = input("type size \n")
    b = b.upper()
    inputed_name = name_input(name = a, size = b)
    zipped(c = inputed_name)
    restart = input("want to restart? if you want type y, if not type n.")
    if restart == "n":
        shouldend = True 