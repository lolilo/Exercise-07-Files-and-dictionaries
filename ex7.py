# opens a file named on the command line

from sys import argv

# The command exists returns True if a file exists, based on its name in a string as an argument. 
# It returns False if not.
from os.path import exists

# Takes in Python script and one file as arguments. 
script, input_file = argv
isValid = True

# Check if input_file exists.
if not exists(input_file):
    print "%r does not exist!" % input_file
    isValid = False

if isValid:
# Opens and reads input_file.
    in_file = open(input_file)

    # Is the cursor at the end of the file?
    in_file_ended = False 
    
    dictionary = {}

    while not in_file_ended:
        indata = in_file.readline()
        if indata == '':
            in_file_ended = True
            break
        split_indata = indata.split(':')
        # print split_indata
        restaurant = split_indata[0]
        score = split_indata[1].strip() 
        # print ''
        # print restaurant, score

        if dictionary.get(restaurant) != None:
            continue # continue on to the next iteration of the while-loop 
            # skips everythings after this point
            # contrast with "break" -- breaks completely out of while-loop
        dictionary[restaurant] = score
        
        # if dictionary.get(restaurant) == None:
        #     dictionary[restaurant] = score
        # else:
        #     pass

    sorted_restaurants = sorted(dictionary.keys())
    # print sorted_restaurants

    for restaurant in sorted_restaurants:
        print "Restaurant '%s' is rated at %s." %(restaurant, dictionary[restaurant])




    # indata = in_file.read()

    # # Split indata string on all white space. 
    # indata_splitted = indata.split(:)
    # print indata_splitted

    # # Create dictionary.
    # dictionary = {}