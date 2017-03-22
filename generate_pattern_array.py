#! /usr/bin/python3


def main():
    f= open("7segfont.txt","a+")
    
    print("This script shows you every ASCII character from 0x20 to 0x60")
    print("and prompts you to enter a binary number for the Seven Segment pattern")
    print("where the least significent bit is the 'a' segment")
    print("and the most significent bit is for the decimal point. ")
    print("Other segments are in between.")
    print("for example for the charecter '1' you should enter 01100000 ")
    print("More info about Seven Segments and their pins:")
    print("https://circuitdigest.com/article/7-segment-display")
    
    f.write("// Seven Segment patterns for ASCII characters from 0x20 to 0x60 \n")
    f.write("byte ss_fonts [] = { \n")
    for i in range(0x20, 0x60):
        print(format(i, 'c'), end='')
        x = int(input(" : "), 2)
        s = "0x"
        s += format(x, '02x')
        s += ", // "
        s += format(i, 'c')
        s += "\n"
        print(s)
        f.write(s)
    f.write("} \n")

if __name__ == "__main__": main()
