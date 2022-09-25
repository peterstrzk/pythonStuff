import math
literki = input("wpisz")
literki = literki.split("")
class sortowansko:
    def shellSort(array):
        n = len(array)
        k = int(math.log2(n))
        interval = 2**k -1
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval
                array[j] = temp
            k -= 1
            interval = 2**k -1
        return array




print(sortowansko.shellSort(array=literki))



