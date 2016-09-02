#Test Print Format of Double Number
num = 1 / 3.0;
#Case1 : Directly Print (Like repr function)
print(repr(num));
#Case2 : Use print Function (Like str function)
print(str(num));
#Case3 : Use String format expression
print('%e' % num);
#Case4 : Use Alternative floating-point format
print('%4.2f' % num);
#Case4 : Use String firmating method
print('{0:4.2f}'.format(num));
