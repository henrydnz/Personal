# exploring a number searcher algorithm

def search(n, max) -> int:
    search = 0
    i = 0

    while not search == n:

        if 2 ** i > max: sum = 1
        else: sum = int(max / 2 ** i)

        if search > n: search -= sum
        if search < n: search += sum  
        i+=1

    return i # iterations

while True:

    maximum = int(input('max n: '))
    n = int(input('n to search: '))

    if maximum >= n and n > 0:     
        iterations = search(n, maximum)
        print(f"{iterations=}")
    else: 
        continue





