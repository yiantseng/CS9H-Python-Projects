import sys

rule=sys.argv[1]
rows=sys.argv[2]
previousRow=None
debug=False

#defines the rule
def define_rule(n):
    bn=bin(int(n))[2:].zfill(8)
    rules= [0]*8
    for x in range(8):
        rules[7-x]=bn[x]
    return rules
    
    
#prints first row
def firstRow(n):
    n=int(n)
    print "P1" + str((n*2)+1)+" "+ str(n+1)
    currentString=""
    for i in range(n):
        currentString+="0"
    currentString+="1"
    for i in range(n):
        currentString+="0"
    print currentString
    return currentString

#mainfunction to print rows
def main_function(rule,rows,debug):
    main_rule=define_rule(rule)
    previousRow=firstRow(rows)
    stringToOutput=""
    if debug:
        print "Rule is:" + str(main_rule)
    
    while rows!=0:
        stringToOutput=""
        #loops through entire row
        for previousRowIndex in range(-1,len(previousRow)-1):
            #if off the screen on the left
            if previousRowIndex==-1:
                stringToOutput+="0"
            else:
                #if off the screen on the right
                if previousRowIndex+3>len(previousRow):
                    stringToOutput+="0"
                    if debug:
                        print "Too large of Index: " + stringToOutput
                    continue
                else:
                    chunk=previousRow[previousRowIndex:previousRowIndex+3]
                    if debug:
                        print "Chunk is: " + chunk
                    #converts the chunk into an integer    
                    currInput=int(chunk,2)
                    if debug:
                        print "Current input number is: " + str(currInput)
                    #goes into the array of main rule to check for whether it should be 0 or 1 and appends it    
                    stringToOutput+=main_rule[currInput]
        print stringToOutput
        if debug:
            print "Row number " +str(rows)+ " is: " +stringToOutput
        previousRow=stringToOutput
        rows-=1

main_function(rule,int(rows),debug)


