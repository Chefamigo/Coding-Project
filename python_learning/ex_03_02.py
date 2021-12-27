hou = input("Enter Hours:")
rat = input("Enter Rate:")
try:
    fh = float(hou)
    fr = float(rat)
except:
    print("error, please enter a numaric input")
    quit()
print(fr, fh)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("pay:" ,xp)
