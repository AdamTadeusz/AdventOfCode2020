import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def main(input_list):
    for x in (input_list):
        for y in (input_list):
            for z in (input_list):
                if x+y+z == 2020:
                    return x*y*z
    return False

input_file = open("C:\\Users\\Adam Tomaszewski\\Desktop\\\xa0\\adventOfCode\\resources\\day1input.txt","r")
input_list = []
for line in input_file:
    input_list.append(int(line.replace("\n","")))
print(input_list)
result = main(input_list)
print(result)