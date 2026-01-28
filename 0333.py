colors = {
"white": "⬜",
"black": "⬛",
"red": "🟥",
"yellow": "🟨",
"orange": "🟧",
}

def chicken_drawing(colors):
    print(colors["white"] * 8 + "\n" + colors["white"] * 8 + "\n" + colors["white"] * 2 + colors["black"] + colors["white"] * 2 + colors["black"] + colors["white"] * 2 + "\n" + colors["white"] * 2 + colors["yellow"] * 4 + colors["white"] * 2 + "\n" + colors["white"] * 2 + colors["orange"] * 4 + colors["white"] * 2)
    for i in range(2):
        print(colors["white"] * 3 + colors["red"] * 2 + colors["white"] * 3)
    print(colors["white"] * 8)
    
chicken_drawing(colors)