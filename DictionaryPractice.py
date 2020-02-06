"""
Objective : Read a file, check the word count and print the max count for corresponding word
"""
count = {}
largestCount = 0
theWord = None
with open("clown.txt") as file:
    print("File Name:", file.name)
    line = file.read()
    print("File Content: ", line)
    word = line.strip().split()
    for w in word:
        count[w] = count.get(w, 0)+1

    for k, v in count.items():
        if largestCount < v:
            largestCount = v
            theWord = k
    print("Largest word count in the input file is {0} for the word '{1}'.".format(largestCount, theWord))


"""
OUTPUT:
File Name: clown.txt
File Content:  the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car 

Largest word count in the input file is 7 for the word 'the'.
"""
