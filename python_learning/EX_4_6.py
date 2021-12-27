def computepay(hours, rate):
    print("In computepay", hours, rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print("Returning",pay )
    return pay

hou = input("Enter Hours:")
rat = input("Enter Rate:")
fh = float(hou)
fr = float(rat)
#print(fr, fh)
xp = computepay(fh, fr)

print("pay:" ,xp)
