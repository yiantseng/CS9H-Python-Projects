import urllib

#reads html from webpage
url=urllib.urlopen("http://geography.about.com/od/lists/a/statecapitals.htm")
html = url.read()

#cuts out the html data that we will be using
source=html[html.find("Alabama")-1:html.find("Cheyenne")+8]

#prints welcome text
print "Welcome to StateCapitalFinder v1.0 by Yi-An Tseng!"
print "Tell me a state and I'll tell you it's capital!"

user_input="Initial Value"

#loop that asks for input and uses that to produce output
while user_input!="q":
    #get user input
    user_input=raw_input("State(Capitalize the first letters of each word!) or (q)uit:")
    
    #finds the state inputted
    input_source=source[source.find(user_input.lower().capitalize()):]
    
    #checks for validity
    if source.lower().find(user_input.lower())==-1 or len(user_input)<4 or user_input!="q":
        print "Not a state!"
    
    #prints capital
    else:
        output=input_source[input_source.find("-")+2:input_source.find("<")]
        print output

#exit message
if user_input=="q":
    print "Thank you for using StateCapitalFinder!"

