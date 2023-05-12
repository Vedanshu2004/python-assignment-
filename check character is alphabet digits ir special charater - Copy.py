ch = input('enter thr character : ')
if((ch>='A' and ch<='Z') or (ch>='a' and ch<='z')):
    print('Character ',ch, ' is alphabet')
elif((ch<='0' and ch>='9')):
     print('character ',ch, ' is digit')
else:
    print('character ',ch, 'is special character ')
