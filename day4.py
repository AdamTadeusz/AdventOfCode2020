import os
dir_path = os.path.dirname(os.path.realpath(__file__))

def count_valid_passports(input_list):
    counter = 0
    
    for document in input_list:
        length = len(document.values())
        has_cid = "cid" in document
        if (length == 8) or (length == 7 and not has_cid):
            counter +=1

    return counter

def prepare_input():
    input_file = open("C:\\Users\\Adam Tomaszewski\\Desktop\\\xa0\\adventOfCode\\resources\\day4input.txt","r")
    input_list = []
    to_append = {}

    #empty line triggers addition of to_append to list of documents
    for line in input_file:
        if line == "\n":
            print(to_append)
            input_list.append(to_append)
            to_append = {}
        else:
            line.replace("\n","")
            key_value_pairs = line.split()
            for key_value_pair in key_value_pairs:
                #convert key_value_pair from list to dictionary
                key_value_pair = key_value_pair.split(":")
                to_append[key_value_pair[0]] = key_value_pair[1]

    #there may not be an empty line after the last document, in that case add to_append to list of documents anyway
    if to_append:
        input_list.append(to_append)

    return(input_list)

def main():
    print(count_valid_passports(prepare_input()))

main()