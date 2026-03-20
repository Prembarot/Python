# wap to input principle amount , rate of intrest , no. of year and find out matureity amount also find intrest u got on principle amount 

principle_amount=int(input("Enter principle amount : "))
rate_intrest=float(input("Enter ROI :"))
numberof_year=int(input("Enter Number of Yeras :"))
maturity_amount= ((principle_amount*rate_intrest/100)*numberof_year)
print("Rate of Intrest", maturity_amount)
maturity_amount= ((principle_amount*rate_intrest/100)*numberof_year)+principle_amount
print("Maturity amount :", maturity_amount)