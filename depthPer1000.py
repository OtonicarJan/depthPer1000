import argparse

#argparse block za command line inpute
infile = argparse.ArgumentParser(description='Set input file, width of the window and the output file') 
#set the input file
infile.add_argument('file', metavar='file', help='Set input csv depth file', type=argparse.FileType('r')) 
#set the width of the window
infile.add_argument('integers', metavar='width', help='Determine the width of the window', type=int) 
#set the output file
infile.add_argument('dest_file', metavar='output file', help='Set the name of your output file', type=argparse.FileType('w+'))
args = infile.parse_args() 
width = args.integers
f = args.file.readlines() 
o = args.dest_file
#set the score to 0
score = 0  
#i for counting through the lines
i = 1
for line in f:  
    #if the current line isn't n%width = 0, then just add the depth to the sum
    if (i % width != 0): #and (i != 10291): 
        score += int(line.split()[2]) 
        i += 1 
        #else first add the depth to the sum and then write the line output to the output file
    else: 
        score += int(line.split()[2]) 
        # first window is the genome name, second is the start, third is the end, 4th is the average score
        print(line.split()[0], int(i - (width-1)), int(i), int((score/width)), file=o) 
        #set the score (sum) back to 0 
        score = 0
        i += 1
