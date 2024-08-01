import re

#re.match(pattern,text): Check for pattern match

text = "Hello, world!"
obj = re.match(r"Hello", text)
print(obj)


url = "https://something.com"

secure = re.match(r"https", url)
if secure:
    print("URL is secure")
else:
    print("URL is not secure")

#   re.split(pattern, text)    # Split text by pattern can only handle one argument 
print('=' *40)
text2 = 'Pythion , Regex;Splitting-Examlple. Fun right?'
words = re.split(r"[,.;\s-]+" , text2)
print(words)

Pnumber = "(770) 888-1180"
formatted_num = re.sub(r"\D",                "",                Pnumber)   #Takes away all the symbols 
print(formatted_num)   #  ^ not a digit     #^ empty string     
                                            # space between ) and 8
#Anon chat using re.sub 
chat = '''
@YeeBee : I like Reg Ex
@Travis : Are you married 
@YeeBee : Whatever
@Travis : HIde this 
'''
anon_chat = re.sub(r"@\w+"  ,'@user-anon'   ,  chat    )     #Replaces all the @words with @user-anon
print(anon_chat)

makecheateranon = re.sub(r"YeeBee", 'redacted', chat)
print(makecheateranon)  #playing around 

#Grouping  (grouping)

pattern = r"(\d+)-(\d+)" 
thematch = re.search(pattern, text)
if thematch:
    print(thematch.group()) #match
    print(f"Group1: {thematch.group(1)}")
    print(f"Group 2: {thematch.group(2)}")
    





