#Shopper 1
shopper_1_name = "Jane Marple"
grocery_1_1_name = "eggs (dozen)"
grocery_1_1_price = 5.04
grocery_1_1_quant = 1
grocery_1_1_net = grocery_1_1_price * grocery_1_1_quant
grocery_1_2_name = "peaches (lbs)"
grocery_1_2_price = 2.56
grocery_1_2_quant = 0.5
grocery_1_2_net = grocery_1_2_price * grocery_1_2_quant
grocery_1_3_name = "bread (loaf)"
grocery_1_3_price = 1.75
grocery_1_3_quant = 1
grocery_1_3_net = grocery_1_3_price * grocery_1_3_quant
grocery_1_4_name = "water (case)"
grocery_1_4_price = 4.25
grocery_1_4_quant = 1
grocery_1_4_net = grocery_1_4_price * grocery_1_4_quant
grocery_1_5_name = "peanut butter (jar)"
grocery_1_5_price = 10.95
grocery_1_5_quant = 2
grocery_1_5_net = grocery_1_5_price * grocery_1_5_quant
total_1 = grocery_1_1_net + grocery_1_2_net + grocery_1_3_net + grocery_1_4_net + grocery_1_5_net
total_quant_1 = grocery_1_1_quant + grocery_1_2_quant + grocery_1_3_quant + grocery_1_4_quant + grocery_1_5_quant
unit_avg_1 = total_1 / total_quant_1
print( f"==={shopper_1_name.title()}=== \nTotal Bill: {total_1} \nAverage Price per Item: {unit_avg_1}")

#Shopper 2
shopper_2_name = "Hercule Poirot"