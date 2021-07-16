heads=int(input("No.of heads:"))
legs=int(input("No.of legs:"))

if legs%2!=0 or heads==0 or heads>legs:
    print("No solution")
else:
    rab=int((legs+(-2*heads))/2)
    ch=int(heads-rab)
print("{},{}".format(ch,rab))