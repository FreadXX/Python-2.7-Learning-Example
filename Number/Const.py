#Define 3 Integer Number
intNum1 = 1234;
intNum2 = -24;
intNum3 = 0;

#Print 3 Numbers
print('Integer 1:' + str(intNum1));
print('Integer 2:' + str(intNum2));
print('Integer 3:' + str(intNum3));

#Define 3 Double Number;
doubleNum1 = 3.14e-10;
doubleNum2 = 4E210;
doubleNum3 = 4.0e+210;

#Print 3 Double Number
print('Double 1:' + str(doubleNum1));
print('Double 2:' + str(doubleNum2));
print('Double 3:' + str(doubleNum3));

#Define 3 Int Number(Oct Format, Hex Format, Binary Format);
octNum = 0177;
hexNum = 0x1bf;
binNum = 0b10110110;

#Print 3 Int Number(Oct Format, Hex Format, Binary Format);
#Notice : str()function automaticlly convert all format integer to decimal format
print('Octual Number:' + str(octNum));
print('Hex Number:' + str(hexNum));
print('Binary Number:' + str(binNum));

#Print with Convert function (Print the correspoding format of specified number)
print('Octual Number:' + oct(octNum));
print('Hex Number:' + hex(hexNum));
print('Binary Number:' + bin(binNum));



