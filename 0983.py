print("    []")       
print("   [][]")      
print("  [][][]") 
print(" [][][][]") 

brick = "[]"
check = True
def pyramid(end, space=0, level=1) -> str:
    global check
    if check:
        space = end
        level = 1
        check = False
    if level != end:
        for i in range(level):
            print((" " * space) + (brick * level), end="")
        print()
        pyramid(space - 1, level + 1)
    
    
pyramid(int(input()))