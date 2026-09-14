#Shopper 1
shopper_1_name = "Jane Marple"
shopper_2_name = "hercule poirot"
grocery_1_price, grocery_1_quant = 5.04, 1
grocery_1_net = grocery_1_price * grocery_1_quant #sets money spent on grocery 1 in total
grocery_2_price, grocery_2_quant = 2.56, 0.5
grocery_2_net = grocery_2_price * grocery_2_quant
grocery_3_price,grocery_3_quant  = 1.75, 1
grocery_3_net = grocery_3_price * grocery_3_quant
grocery_4_price = 4.25
grocery_4_quant = 1
grocery_4_net = grocery_4_price * grocery_4_quant
grocery_5_price = 10.95
grocery_5_quant = 2
grocery_5_net = grocery_5_price * grocery_5_quant
total = grocery_1_net + grocery_2_net + grocery_3_net + grocery_4_net + grocery_5_net #sets total bill
total_quant = grocery_1_quant + grocery_2_quant + grocery_3_quant + grocery_4_quant + grocery_5_quant
unit_avg = total / total_quant #calculates average unit price for various groceries
print( f"==={shopper_1_name.title()}=== \nTotal Bill: {total} \nAverage Price per Item: {unit_avg}")

#Shopper 2
