prices=[10,20,30]
dis=10
final_prices=[]

for price in prices:
    final_price= price - (price*dis/100)
    final_prices.append(final_price)
    print(final_prices)


  