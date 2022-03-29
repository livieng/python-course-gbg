# ex. 5.8 Ska gå runt i alfabetet i loop, efter z kommer a...
# def cipher2():
#     mess=input("Enter a message to encode: " )
#     k=eval(input("Enter key: "))
#     abc="abcdefghijklmnopqrstuvwxyz"
#     cipher=""
#     for ch in mess:
#         if ch == ' ':
#             cipher+= ' '
#         else:
#             cipher+=chr(ord(ch) + k)
#     print(cipher)
#cipher2()


def main(str): 
    new_str = "" 
    ch = 0
    while ch < len(str): 
        if (str[ch].isdigit()):
            num = ""
            while (str[ch].isdigit()):
                num += str[ch]
                ch += 1
            new_str += " " + num + " "
        else: 
            new_str += str[ch]
        ch += 1
    string = new_str.split() 
  
    print(string) 

if __name__ == "__main__": 
    main("is is the th15 today")
