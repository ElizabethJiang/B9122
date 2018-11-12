print('I am now making changes to this py file in order to finish my homework3.')

hrs=input('Enter Hours:')
print(hrs)
h=float(hrs)
rate=input('Enter Rate:')
r=float(rate)
if h<=40:
    pay=h*r
else:
    pay=40*r+(h-40)*r*1.5
print(pay)
