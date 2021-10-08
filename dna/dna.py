import sys
import csv
import re

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # create a list that has every row from csv file as separate dictionary
    dnaStrDB = []
    with open(sys.argv[1]) as csvFile:
        reader = csv.DictReader(csvFile)
        STRs = reader.fieldnames[1:]
        for row in reader:
            dnaStrDB.append(row)

    # read the .txt file to dnaSequance string
    with open(sys.argv[2]) as txtFile:
        dnaSequence = txtFile.read()

    # create a list of how much every STR in STRs repeats consequantly in .txt file
    strConsecRepeats = []
    for STR in STRs:
        strConsecRepeats.append({STR : consec_Str_repeats(dnaSequence, STR)})

    
    match = []

    # look for matching STRs in dnaStrDB
    for everyRow in dnaStrDB:
        b = 0
        hits = 0
        for STR in STRs:
            jj = int(everyRow[STR])
            pp = strConsecRepeats[b][STR]
            if int(everyRow[STR]) == strConsecRepeats[b][STR]:
                hits += 1
            b += 1
        if hits == len(STRs):
            # match found
            match.append(everyRow['name'])
    
    if len(match) != 0:
        for everyName in match:
            print(everyName)
    else:
        print("No match.")
    


#FUNCTIONS
def consec_Str_repeats(dnaSequence, STR):
    stringLength = len(STR)
    i = 0
    j = stringLength

    maxRepeats = 0
    tempRepeats = 0
    
    for a in range(0, len(dnaSequence)):
        #substring = dnaSequence[i:j] #for debugging here
        if dnaSequence[i:j] == STR:
            tempRepeats += 1
            if tempRepeats > maxRepeats:
                maxRepeats = tempRepeats
            i += stringLength
            j += stringLength
        else:
            i += 1
            j += 1
            tempRepeats = 0

    return maxRepeats

if __name__ == "__main__":
    main()