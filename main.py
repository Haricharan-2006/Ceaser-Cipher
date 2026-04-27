def encrypt(text,shift_number):
    alphabets = [chr(x) for x in range(ord('a'),ord('z')+1)]
    shift_number %= 26
    res = ""
    for i in text:
        if i in alphabets:
            res += alphabets[(alphabets.index(i)+shift_number)%26]
        else:
            res += i
    print("Encrypted message is",res)
def decrypt(text,shift_number):
    alphabets = [chr(x) for x in range(ord('a'),ord('z')+1)]
    shift_number %= 26
    res = ""
    for i in text:
        if i in alphabets:
            res += alphabets[(alphabets.index(i)-shift_number)]
        else:
            res += i
    print("Decrypted message is",res)
def ceaser_cipher():
    flag = True
    while flag:
        choice = input("Type 'encode' to encrypt or 'decode' to decrypt: ")
        if choice == 'encode':
            text = input("Enter the text to be encrypted: ")
            shift_number = int(input("Enter the shift number: "))
            encrypt(text,shift_number)
        elif choice == "decode":
            text = input("Enter the text to be decrypted: ")
            shift_number = int(input("Enter the shift number: "))
            decrypt(text,shift_number)
        else:
            print("Choice is not available!!!!")
        print("Type 'yes' for to do again and 'no' for exit")
        flag = True if input() == 'yes' else False
ceaser_cipher()
