#-----------------------------------------
#pdbを使ってみる

#always_breakpoint.py
import math

def compute_rmse(observed, ideal):
    total_err_2 = 0
    count = 0
    for got, wanted in zip(observed, ideal):
        err_2 = (got - wanted) ** 2
        breakpoint() #start the debugger here
        total_err_2 += err_2
        count += 1
    
    mean_err = total_err_2 / count
    rmse = math.sqrt(mean_err)
    return rmse

result = compute_rmse(
    [1.8, 1.7, 3.2, 6],
    [2, 1.5, 3, 5],
)

print(result)

#こんな感じ👇
#-> breakpoint() #start the debugger here
#(Pdb) total_err_2
#0
#(Pdb) err_2
#0.03999999999999998
#(Pdb) 

