lab = [
    [1,1,1,1,1,1,1],
    [1,0,0,0,1,8,1],
    [1,0,1,0,1,0,1],
    [1,0,1,0,0,0,1],
    [1,0,1,1,1,0,1],
    [1,0,0,0,0,2,1],
    [1,1,1,1,1,1,1]
    ]
line = " –" * 10

def lab_map():
    print("      -лабиринт-".upper()); print(line)
    for lst in lab:
        for x in lst:
            print(f" {x} ", end="")
        print()
    print(line)

def move():
    print(" 1 – влево\n 2 – направо\n 3 – вверх\n 4 – вниз")
    move_player = input(" Куда двигаться: ")
    
lab_map()
move()