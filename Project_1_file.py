#Shopper 1
shopper_1_name = "Jane Marple"
grocery_1_price = 5.04
grocery_1_quant = 1
grocery_1_net = grocery_1_price * grocery_1_quant
grocery_2_price = 2.56
grocery_2_quant = 0.5
grocery_2_net = grocery_2_price * grocery_2_quant
grocery_3_price = 1.75
grocery_3_quant = 1
grocery_3_net = grocery_3_price * grocery_3_quant
grocery_4_price = 4.25
grocery_4_quant = 1
grocery_4_net = grocery_4_price * grocery_4_quant
grocery_5_price = 10.95
grocery_5_quant = 2
grocery_5_net = grocery_5_price * grocery_5_quant
total = grocery_1_net + grocery_2_net + grocery_3_net + grocery_4_net + grocery_5_net
total_quant = grocery_1_quant + grocery_2_quant + grocery_3_quant + grocery_4_quant + grocery_5_quant
unit_avg = total / total_quant
print( f"==={shopper_1_name.title()}=== \nTotal Bill: {total} \nAverage Price per Item: {unit_avg}")

#Shopper 2
shopper_2_name = "Hercule Poirot"
grocery_1_price = 5.04
grocery_1_quant = 1
grocery_1_net = grocery_1_price * grocery_1_quant
grocery_2_price = 2.56
grocery_2_quant = 0.5
grocery_2_net = grocery_2_price * grocery_2_quant
grocery_3_price = 1.75
grocery_3_quant = 1
grocery_3_net = grocery_3_price * grocery_3_quant
grocery_4_price = 4.25
grocery_4_quant = 1
grocery_4_net = grocery_4_price * grocery_4_quant
grocery_5_price = 10.95
grocery_5_quant = 2
grocery_5_net = grocery_5_price * grocery_5_quant
total = grocery_1_net + grocery_2_net + grocery_3_net + grocery_4_net + grocery_5_net
total_quant = grocery_1_quant + grocery_2_quant + grocery_3_quant + grocery_4_quant + grocery_5_quant
unit_avg = total / total_quant
print( f"==={shopper_1_name.title()}=== \nTotal Bill: {total} \nAverage Price per Item: {unit_avg}")