# ex.5.3. gives a grade for the scale 1-100
def scor():
    score=eval(input("Enter score (1-100 points): "))
    if score in range(90,101):
        print("Grade: A")
    elif score in range(80,90):
        print("Grade: B")
    elif score in range(70,80):
        print("Grade: C")
    elif score in range(60,70):
        print("Grade: D")
    else:
        print("Grade: F")
#score()

# ex. 5.4
def phrase():
    phrase=input("Enter a phrase: ")
    words=phrase.split(" ")
    acr=""
    for word in words:
        letter=word[0]
        acr+=letter.upper()
    print(acr)
#phrase()

# ex. 5.5
def namenum():
    name=input("Enter your first name: ")
    num=0
    for letter in name:
        num+=ord(letter)-96
    print(num)
#namenum()

# ex. 5.6
def name2num():
    name=input("Enter your full name: ")
    fullname=name.split(" ")
    char="".join(fullname)
    char2=char.lower()
    num=0
    for letters in char2:
        num=num+(ord(letters)-96)
    print(num)
#name2num()

# ex. 5.7 ceasars cipher
def cipher():
    mess=input("Enter a message to encode: " )
    k=eval(input("Enter key: "))
    cipher=""
    for ch in mess:
        if ch == ' ':
            cipher+= ' '
        else:
            cipher+=chr(ord(ch) + k)
    print(cipher)
#cipher()

# count words, lines, characters
def wordcount():
    text=input("Enter filename: ")
    doc=open(text, "r").read()
    words=doc.split()
    wc= len(words)
    lines=len(doc.splitlines())
    ch=len("".join(doc))
    print(wc,lines,ch)
#wordcount()