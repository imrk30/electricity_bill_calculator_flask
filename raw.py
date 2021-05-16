
# name_appliance = input('enter the name of appliance : ')
# no_appliance = int(input('enter the no. of appliance: '))
# appliance_rating = float(input('enter the energy rating of '+str(name_appliance)+' (in watts) :'))
# kw = appliance_rating/1000
# time = float(input('enter the time used(in hours) :'))
# na_rate = no_appliance*appliance_rating
# print('total rating multiplied with no. of appliance ',na_rate)
# print(name_appliance.title())
# kwh = kw*time*no_appliance
# #kwh = float(kw_h)
# one_month = kwh * 30
# two_months = kwh * 60
# one_year = kwh * 365
# print('(in kwh) : ',kwh)
# print('for one month : '+ str(one_month)+' kwh')
# print('for two month : '+ str(two_months)+' kwh')
# print('for one year : '+ str(one_year)+' kwh')
# print('\n')


# as of 2021
units=int(input("Number of unit consumed: "))
if(units>0 and units<=100):
    payAmount=units*0
    fixedcharge=0.00
elif(units>100 and units<=200):
    payAmount=(100*0)+(units-100)*1.50
    fixedcharge=20.00
elif(units>200 and units<=500):
    payAmount=(100*0)+(200-100)*2+(units-200)*3
    fixedcharge=30.00
elif(units>500):
    payAmount=(100*0)+(200-100)*3.5+(500-200)*4.6+(units-500)*6.6
    fixedcharge=50.00
else:
    payAmount=0;
    
Total= payAmount+fixedcharge

print("\nElecticity bill pay: " ,Total);