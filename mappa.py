mappa_test = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

mappa_big = [
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
    [1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0],
    [1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0],
    [1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0],
    [1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,1,0],
    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,1,0],
    [1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0],
    [1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,1,1,0],
    [1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0]
    #0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
]

mappa_bigger = [
    x+x for x in mappa_big
]