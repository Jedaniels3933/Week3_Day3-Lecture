#REGex - regex to match a string against a pattern 
#Usecases - Usecase to match a string against a pattern

# Search Text for data of a particular pattern
# Validates data , email- password and other fields
# Also to manipulate data in a particular pattern or analysis
 # Terminology 
#literal chars : exact char. a,b,v,f,d,2,4,5,', "
#meta_chars = Special symbols that represent broader categories
# Dot = #Regex pattern for cat is c.t = Wildcard

#Caret ^ = #Regex pattern for ^cat = cat at the beginning of the string
#Example: ^cat = must be at beginning of string
# $ = #Regex pattern for cat$ = cat at the end of the string Example: cat$ = must be at end of string I like cats$ = must be at end of string

# * - asterix  Zero or more occurances  ba* = matches are bat, back , battle, baa, b 

# plus symbol + = one or more occurances ba+ = matches are bat, back, battle, baa but not b
# Question mark ? = specif 0 or 1 :  ba? = matches are bat, ba but not back, battle, baa, preceding char is optional

#Backslash \ = escape char, to escape a special char, use \ before the special char.   \. = special char .  \* = special char     \. = (., .)
# [] = character sets  find all vowels in a string [aeiou] = a, e, i, o, u   :Regular Radicals ['Re', 'Ra']

#Pipe = or operator  Task: match cat or dog , (| | |) |cat|dog|cow|hamster
# 
# Groups () = Finds repetitions of a pattern  (cat)+ = cat, catcat, catcatcat, catcatcatcat
# "(wolf|meow)" = The cat says meow the dog says wolf= will return "meow, wolf"
# Special Sequences = \d = digit, \w = word, \s = whitespace, \b = word boundary, \A = beginning of string, \Z = end of string
# {} = curley braces = specify exact occuruinngs of the search string ba{2} = matches baa but not bat, back, battle, b
# {2,3} = specify range of occurances ba{2,3} = matches baa, baaa but not bat, back, battle, bacacaaca/
# \d = digit, 304-442-2326 = \d{3}-\d{3}-\d{4} = 304-442-2326
#  \w = finds word chars (letters, digits, underscores)  \w{3,} = matches 3 or more word chars \w*\d\w* = matches w0w.
# \s = finds whitespace \s = matches whitespace (spaces, tabs, new lines)   /s+ = can find spaces in between other chars
# \D = non-digit \D+ = matches non-digits \D(0 or more = +), 
# \W = non-word char \W+ = matches non-word chars \W(0 or more = +), will give you all non-word chars like commas and spaces, underscores , #$^%&$#*%^ any of this 
# \S = non white space in string \S+ = matches non-whitespace chars \S(0 or more = +),  will print out every individul char in the string "This" =  "T", "h", "i", "s"
# \b = Used to mark the start or end of a word 
#find words that start with \b in string \b\w* = matches all words that start with \b in a string matches boy , bark, bee
# \B = used to mark something that does not start with \B\w* = matches python, anything that deos not start with b
#  



