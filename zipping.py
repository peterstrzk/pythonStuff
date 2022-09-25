names = []
values = []

#append and zip names and sizes
class MyClass:

    def __init__(self, name, value):
        names.append(name)
        values.append(value)
        c = zip(names, values)
        self.c = c
        
        # result_c = dict(c)
        # for k, v in result_c.items():
        #     print(k, v)

    #putting zipped stuff into dictionary
    def zipped(self):
        result_c= dict(self.c)
        print(result_c)
        fin_mex = max(result_c, key=result_c.get)
        self.fin_mex = fin_mex
        return fin_mex

    def ending(self):
        print(f"Auction{self.fin_mex}")
    #looping with input condition


shouldEnd = False
while not shouldEnd:
    a = input("Type a name \n")
    b = int(input("Type value \n"))
    
    s = MyClass(name = a, value = b)
    s.zipped()
    
    restart = input("Want to restart? If you want type Y, if not type N.")
    if restart == "n":
        s.ending()
        
        shouldEnd = True
        print("goodbye")