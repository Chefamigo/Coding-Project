hou = input("Enter Hours:")
rat = input("Enter Rate:")
fh = float(hou)
fr = float(rat)
#print(fr, fh)
if fh > 40:
   # print("overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    #print(reg,otp)
    xp = reg + otp
else:
    #print("regular")
    xp = fh * fr
print("pay:" ,xp)
