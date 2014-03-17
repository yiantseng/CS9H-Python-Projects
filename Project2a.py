#Welcome text
print "Welcome to Python-powered Unit Converter by Yi-An Tseng"
print "You can convert Distances, Weights, Volumes & Times to one another but only withing units of the same category, which are shown below."
print "Please use the format in amount source_unit in dest_unit. For example to convert m to km use 10 m in km."
print ""
print "Distances: ft cm mm mi m yd km in"
print "Weights: lb mg kg oz g"
print "Volumes: floz qt cup mL L gal pint"
print ""

#Dictionary with base conversion

distances={"m":1,"cm":100,"mm":1000,"km":0.001,"in":39.3701,"ft":3.28084,"yd":1.09361,"mi":0.000621371}
volumes={"L":1,"mL":1000,"floz":33.814,"cup":4.22675,"pint":2.11338,"qt":1.05669,"gal":0.264172}
weights={"g":1,"kg":0.001,"mg":1000,"oz":0.035274,"lb":0.00220462}

#while loop that continues to ask for conversion until q
source_input="Initial Value"
while source_input!="q":
    #gets input
    source_input=raw_input("Enter amount source_unit in dest_unit, or (q)uit: ")
    input_values=source_input.split()
    
    #checks for corrent input length and extracts the units and amount from the input
    if len(input_values)==4:
        source_unit=input_values[1]
        dest_unit=input_values[3]
        amount=input_values[0]
        
        #checks if its the same unit type
        if ((source_unit in distances) and (dest_unit in distances)) or ((source_unit in volumes) and (dest_unit in volumes)) or ((source_unit in weights) and (dest_unit in weights)):
            #converts distances
            if source_unit in distances:
                conversion=float(amount)*(float(distances[dest_unit])/float(distances[source_unit]))
                output= amount+source_unit+"="+str(conversion)+dest_unit
            #converts volumes
            elif source_unit in volumes:
                conversion=float(amount)*(float(volumes[dest_unit])/float(volumes[source_unit]))
                output= amount+source_unit+"="+str(conversion)+dest_unit
            #converts weights
            elif source_unit in weights:
                conversion=float(amount)*(float(weights[dest_unit])/float(weights[source_unit]))
                output= amount+source_unit+"="+str(conversion)+dest_unit
            #prints conversion output
            print output
        #Tells user that the input format is wrong    
        else: 
            print "Cannot convert, please use the same type of units and correct notation"
    #quits program
    elif source_input=="q":
        print "Thank you for using Python-powered Unit Converter by Yi-An Tseng"
    #Tells user that input format is wrong, if not the correct length
    else:
        print "Cannot convert, please use the same type of units and correct notation"

