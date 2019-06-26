import sys
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"] 
Two = [" *** ", "* *", "* * ", " * ", " * ", "* ", "*****"] 
Nine = [" ****", "* *", "* *", " ****", " *", " *", " *"]
Zero=[]
Three=[]
Four=[]
Five=[]
Six=[]
Seven=[]
Eight=[]

Digits=[Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits=sys.argv[1]
    row=0
    while row<7:
        column=0
        while column<len(digits):
            num=int(digits[column])
            print(Digits[num][row],end=" ")
            column+=1
        print()
        row+=1
except IndexError as e:
    print(e)
except ValueError as v:
    print(v)    
