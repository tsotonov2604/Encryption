
#Tsvety Sotonov
#Problem 2 Parts 1 & 2

def caesar(num):
    
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num %= 26

    shifted_alphabet_lower = lower[num:] + lower[:num]
    shifted_alphabet_upper = upper[num:] + upper[:num]

    alphabet = lower + upper 
    print("normal:",alphabet)
    shifted_alphabet = shifted_alphabet_lower + shifted_alphabet_upper
    print("cipher:",shifted_alphabet)
    mapping = shifted_alphabet.maketrans(alphabet, shifted_alphabet)
    return mapping
    
def main():
    num = int(input("Enter number of positions to shift to the right: "))
    mapping = caesar(num)
    
    infile = input("Enter file to be encrypted: ")
    split = infile.split(".")
    print("Encrypted file is " + split[0] + "_ENC" + ".txt")

    
    infile = open('The_Tempest.txt','r')
    content = infile.read()
    numofLines = len(content.splitlines())
    numWords =len(content.split())
    numChar = len(content)
    infile.close()
    print(content)
    
   
    
    outfile = open('inputFileName_ENC.txt','w')
    out =outfile.write(content.translate(mapping))
    outfile.close()

    printformat = ('Num Lines:{}   Num Chars:{}   Num Words:{}'.format(numofLines,numChar,numWords))
    print(printformat)
    
    
main()




