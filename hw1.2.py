billamount = input('Please enter the total bill amount: ') #string, 80
numpeople = input('Please enter the number in your party: ') #string, 4
tippercent = input('Please enter the desired tip percentage (for example, "20" for 20%): ') #string, 25

tipamount = float(billamount)*float(tippercent)/100 #float, 20.0
billwithtip = float(billamount) + tipamount ##float, 100.0
payperperson = billwithtip/int(numpeople) ##float, 25.0

print('A ' + tippercent + '% ($' + str(tipamount) + ') was added to the bill, for a total of $' + str(billwithtip) + ' With ' + numpeople + ' in your party, each person must pay $' + str(payperperson))
