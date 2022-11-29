import datetime  as dt
today_date=input("Enter the todays date:\n")
today_date=dt.datetime.strptime(today_date,'%d/%m/%Y').date()
birth_date=input('Enter your Birth date:\n')
birth_date=dt.datetime.strptime(birth_date,'%d/%m/%Y').date()
da=today_date-birth_date
print(type(da))
print(da.days//365)
