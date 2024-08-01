import re    #Imports regex functions from the re module
def d():
    print("--" * 65)
def l():
    print("=" * 65)

#Regex Methods and (f)'s
# re.findall method (pattern, text): returns all non -overlapping matches of the pattern 
#find how many times 'and' is used in a sentance pattern
text = "HI, my name is Jeremiah, and I like to go and do stuff and things" 
#need to use a raw string r
ands = re.findall(r"and",text)
print(ands) #prints (and, and, and) 
l()
print(len(ands)) #prints 3
d()

# Find all the #'s in a sentance pattern that are followed by words like a hastag post on twitter
post = "I LOVE # learning # and #python_is_lyfe and #Regex, this is so fun! #Code" 

tags = re.findall(r"#\w+", post)   # pattern then var
print(tags) 
l()

#Find words that start with 'b' and end with 'e'
sentance = "Abe asked to build a bridge but he was told 'beware of the beehives'"

bees = re.findall(r'\bb\w*e\b',sentance)    #\bb = starts with 'b' followed by a word(\w*) then end with an 'e'
print(bees)

#Finding an email address- username( can include letters, ints, underscores, dashes, periods ) , @ symbol=domain name- can include ints, dashes, underscores, = .com is 2-3 chars lets A-Z .gov, .net, .org, .edu , .co  
text = "You can contact me at t.p@gmail.com or travis-p2@codingtemple.com, traviscpeck@email.com"
# [] finds characte sets
emails = re.findall(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", text)      #\w = word char, . = period, - = dash, + = one or more, @ = at symbol, [a-z] = lowercase letters, {2,3} = 2-3 chars (had to use \. because . is a meta char)
d()
print(emails)   #Prints all the emails in sentance = text

sentace2 = ' this is a sentance With some Capitals AND some not So much'

# Find all words with all capital letters

all_cap_words = re.findall(r"\w*[A-Z]+\w*", sentace2)  #\w* = word char, [A-Z] = capital letters, + = one or more, \w* = word char
print(all_cap_words)  #Prints all the words with all capital letters in sentance = sentace2

###  re.search   pattern is the argument that is passed to the re.search method
# re.search(pattern, text) : returns the first match of the pattern in the text
# great for input validation
d()
#email = input("Enter an email here :") #check for proper email 
#found =  re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)
#print(found) 
#print(found.group())  #Prints the email that was entered/ use .group to print the email that was entered
#if found:
    #print(f'{found.group()} is a valid email! PLease click to continue')
#else:
    #print('Invalid email. Please try again.')

    #Validate a phone number 
d()
   # phone = input("Enter a phone number here :")
   #I want to accept a variety of phone numbers , #000-000-0000, or 000 000 0000, or 0000000000, (000) 000-0000

#number = "My phone number is : (770)888-1180"
#phone = re.search(r"\+?\d{0,3}\ss-]?\d{3}[\s-]?/d{4}", number)
#print(phone)


   











