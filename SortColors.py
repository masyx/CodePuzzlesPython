def sort_colors(colors):
    return colors

def sort_colors_counting(colors):
    count = [0, 0, 0]
    
    # Count the occurrences of each color
    for color in colors:
        count[color] += 1
    
    index = 0
    for color in range(3):
        for _ in range(count[color]):
            colors[index] = color
            index += 1
    return colors

def main():
    colors = [2, 1, 0]
    #colors = [2, 1, 0, 2, 1, 0, 0, 1, 1, 2, 2, 1, 1, 0]
    print(sort_colors_counting(colors))
    

if __name__ == "__main__":
    main()