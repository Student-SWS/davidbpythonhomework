def tipcalc(total_def, num_def, percent_def):
    if num_def <= 0 or total_def <=0:                                                   # bool, False
        raise ValueError("'bill' and 'number in party' must be greater than 0")
    final_amount = total_def * (1+percent_def/100)                                      # float, 120.0
    return final_amount / num_def

total = 100.0                                                                           # float, 100.0
num = 4                                                                                 # int, 4
tip_pct = 20                                                                            # tip_pct, 20

share = tipcalc(total, num, tip_pct)                                                    # float, 30.0
print(share)

share = tipcalc(150, 3, 15)                                                             # float, 57.5
print(share)
