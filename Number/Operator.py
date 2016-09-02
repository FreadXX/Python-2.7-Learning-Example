#Define 3 Number
intNum = 1234;
doubleNum = -24e-2;
radiusNum = 1 + 3j;

#Test Operators
addResult = intNum + doubleNum;
minusResult = radiusNum - intNum;
multiResult = intNum * doubleNum;
powResult = intNum ** 3;
# moveResult = doubleNum << 1;  Error Code!   '<<' Only used for Integer
moveResult = intNum << 2;

#Print The Results of Operators
print("Integer + Double:" + str(addResult));
print("Radius - Integer:" + str(minusResult));
print("Integer * Double:" + str(multiResult));
print("Integer ^ 3:" + str(powResult));
print("Integer << 2:" + str(moveResult));


#Test Math Function
absResult = abs(doubleNum);
roundResult = round(doubleNum+1, 2);

#Print The Results of Math Functions
print("The Absolution of Double:" + str(absResult));
print("The Round Value of Double:" + str(roundResult));
