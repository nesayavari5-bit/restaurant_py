mnu = {"burger":180000,"pizza":250000,"sandwich":120000,"drink":40000}
name = input("enter customer name:")
product = input("enter product name:").title()
count = int(input("enter quantity:"))
if product in menu:
  price = menu[product]
  total = price*count
if total > 500000
   discount = total*0.10
else:
    discount = 0
  final_price =total-discount
print("\n-----order information-----")
print("customer:" ,name)
print("product:" , product)
print("quantity:" ,count)
print("total price:" , total)
print("discount:" , discount)
print("final price:" , final_price)
elgse:
     print("sorry! this product is not available.")
