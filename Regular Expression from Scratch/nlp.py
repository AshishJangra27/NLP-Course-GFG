def capitalize(text):  
    if (len(text) != 0):
        return upper(text[0]) + lower(text[1:])
    else:
        return None
    
    
def upper(text):
    string = ''
    for char in text:
        if ( ord(char) >= 97 and ord(char) <= 122 ):
            string += chr(ord(char) - 32)           
        else:
            string += char        
    return string

def lower(text):  
    string = ''
    for char in text:
        if ( ord(char) >= 65 and ord(char) <= 90 ):
            string += chr(ord(char) + 32)          
        else:
            string += char
    return string

def isalpha(text):
    c = 0
    for i in text:
        if ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
            c += 1
    if (len(text) == c):
        return True
    else:
        return False
    
def isdigit(text):
    c = 0
    for i in text:
        if (ord(i) >= 48 and ord(i) <= 57):
            c += 1
            
    if (len(text) == c):
        return True
    else:
        return False
    
def isalnum(text):
    c = 0
    for i in text:
        if ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57)):
            c += 1
    if (len(text) == c):
        return True
    else:
        return False
    
def title(text):

    output = []
    for word in text.split(' '):
        output.append(upper(word[0]) + lower(word[1:]))
    return ' '.join(output)