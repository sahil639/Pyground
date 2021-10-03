#formula
# Amount  = Principal amount(1 + Rate/100) time
# Compound Interest = A – P 


p = int(input("enter the principal amount"))
t = int(input("enter the time"))
r = int(input("enter the rate"))
Amount = p * (pow((1 + r / 100), t))
c = Amount - p
print(c)

