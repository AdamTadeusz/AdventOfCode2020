import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def main(input_list):
    num_valid = 0
    for line in input_list:
        first = line[3][line[0]] == line[2]
        second = line[3][line[1]] == line[2]
        if (first and not second) or (second and not first):
            num_valid += 1
    return num_valid

def prepare_input():
    input_file = open("C:\\Users\\Adam Tomaszewski\\Desktop\\\xa0\\adventOfCode\\resources\\day2input.txt","r")
    input_list = []
    for line in input_file:
        to_append = []
        first = line.find("-")
        second = line.find(":")

        to_append.append(int(line[0:first]))
        to_append.append(int(line[first+1:second-1]))
        to_append.append(line[second-1:second])
        to_append.append(line[second+1:].replace("\n",""))
        input_list.append(to_append)
    print(input_list)
    return(input_list)

print(main(prepare_input()))