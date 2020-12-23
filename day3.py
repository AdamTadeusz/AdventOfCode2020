import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def find_num_trees(input_list, move):
    counter = 0
    current_position = (0,0)
    width_of_line = len(input_list[0])

    trigger = False
    while not trigger:
        current_position = (((current_position[0]+move[0])%width_of_line), current_position[1]+move[1])
        if current_position[1] >= len(input_list):
            trigger = True
        else:
            if input_list[current_position[1]][current_position[0]] == "#":
                counter+=1
    return counter

def prepare_input():
    input_file = open("C:\\Users\\Adam Tomaszewski\\Desktop\\\xa0\\adventOfCode\\resources\\day3input.txt","r")
    input_list = []
    for line in input_file:
        input_list.append(line.replace("\n",""))
    #print(input_list)
    return(input_list)

def main():
    total = 1
    movements = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for move in movements:
        total = total * find_num_trees(prepare_input(),move)
    print(total)

main()