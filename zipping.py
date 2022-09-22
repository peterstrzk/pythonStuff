names = []
values = []

#append and zip names and sizes
class MyClass:

    def name_input(name, value):
        names.append(name)
        values.append(value)
        c = zip(names, values)
        return c
        # result_c = dict(c)
        # for k, v in result_c.items():
        #     print(k, v)

    #putting zipped stuff into dictionary
    def zipped(c, self):
        result_c= dict(c)
        print(result_c)
        fin_mex = max(result_c, key=result_c.get)
        self.fin_mex = fin_mex
        return fin_mex
        # print(f"{fin_max} wins!")
        # lol = who_wins(fin_max)
        # return lol
        # for k, v in result_c.items():
            # print(k, v)
    # def who_wins(who):

    #     print(f"{who} wins!")

    #looping with input condition
    shouldEnd = False
    while not shouldEnd:
        a = input("Type a name \n")
        b = int(input("Type value \n"))
        
        inputed_name = name_input(name = a, value = b)
        zipped(c = inputed_name)
        restart = input("Want to restart? If you want type Y, if not type N.")
        if restart == "n":
            # print(fin_mex)
            shouldEnd = True
            ("goodbye!")