"""
I wrote this the way I write professional code:
- Function and variable names should be balanced between being explainatory and being succint.
- SRP (single responsibility principle) for functions so each can be easily reasoned about, tested, and modified.
- SRP/Single op for each line of code to aid readability and to make bug tracking easy.
- DRY (do not repeat yourself)
- I used more comments than I would have in production because this is "teaching" code. In production, comments tend to become inaccurate over time.
- Code broken into functions is more easily reusable and can be shifted to a library if warranted in the future.
"""

# function to read a text file and return a list of text lines.
def read_file(filename):
    with open(filename, 'r') as f:
        return f.readlines()    

# function to convert a space seperated string into a 2 element list
# where the first value must be an integer and the second value is a string
def ssv_to_list(ssv):

    result = [0,""]

    ssv_as_list = ssv.split(' ')
    
    # convert the first value to an integer
    result[0] = int(ssv_as_list[0])
    # convert the second value to a string
    result[1] = str(ssv_as_list[1])
    
    return result

# function to iterate over a list of ssv (space seperated values) strings and return a list of lists
# where each member list is a 2d. 
# The first value must be an integer and the second value is a string
def convert_to_sorted_list(data):
    list_of_lists = []
    for line in data:
        # strip the newline character from the end of the ssv string
        line = line.rstrip()
        if(line == ""):
            continue
        # convert the ssv string to a list of values (integers and strings)
        ssv_as_list = ssv_to_list(line)
        list_of_lists.append( ssv_as_list )

    # order the list of lists by the first value, which is an integer
    list_of_lists.sort(key=lambda x: x[0])
    
    return list_of_lists 

def convert_to_list_of_words(data):
    list_of_words = []
    for line in data:
        list_of_words.append(line[1])
    return list_of_words

# function to build a pyramid from a list of words
def build_word_pyramid(list_of_words):

    # Create an empty pyramid that will hold multiple levels. 
    pyramid = []

    # Create an empty level.
    this_level = []

    # Iterate over the list of words and build the pyramid level by level.
    for word in list_of_words:
        this_level.append(word)
        if( len(this_level) == len(pyramid) + 1):
            pyramid.append(this_level)  
            # Reset the level to start a new one.          
            this_level = []
    return pyramid

# function to build a message from the last element of each level in a pyramid
def build_message(pyramid):
    message = ""
    for level in pyramid:
        message += (level[-1] + " " )
    return message

def decode(message_file):
    
    data = read_file(message_file)

    sorted_numbers_and_words = convert_to_sorted_list(data)   

    list_of_words = convert_to_list_of_words(sorted_numbers_and_words)

    word_pyramid = build_word_pyramid(list_of_words)
    
    print(build_message(word_pyramid))

decode("./data2.txt")



