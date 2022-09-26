from operator import countOf


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
        self.result_c = result_c
        print(result_c)
        fin_mex = max(result_c, key=result_c.get)
        self.fin_mex = fin_mex
        return fin_mex

    def tie(self):
        count_of_values = countOf(self.result_c.values(), self.result_c[self.fin_mex])
        return count_of_values
        # if a > 1:
            # print(a, "There is a tie!")
           


    def ending(self):
        print(f"{self.fin_mex}")
    #looping with input condition


shouldEnd = False
while not shouldEnd:
    a = input("Type a name \n")
    b = int(input("Type value \n"))
    
    s = MyClass(name = a, value = b)
    s.zipped()
    s.tie() 

    restart = input("Want to restart? If you want type Y, if not type N.")
    if restart == "n":
        if s.tie() > 1:
            print('there is a tie!')
            names.clear(), values.clear()
            shouldEnd = False
        else:
            s.ending()

            shouldEnd = True
            print("goodbye")
        