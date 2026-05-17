shop = {
    "mobile_shop": {
        "brand": "Samsung",
    },

    "stock_models": {
        "S21",
        "S22",
        "S23"
      
    },

    "pricing": {
        "S23": 100000,
        "S22": 800000

    }
}

Newmodel = shop["stock_models"].add("S24")
print(f"New model is added in {shop['stock_models']}")

check = shop["pricing"].get("S21","Its not available")
print(check)

price_of_S23 = shop["pricing"]["S23"]
print(f"The price of S23 is {price_of_S23}")
if price_of_S23 > 90000:
    print(f"You give discount 10%")
    price_after_discount = price_of_S23*0.90
else:
    print(f"you give only 5% discount because the price of mobile is already low")
    price_after_discount = price_of_S23*0.95
print(price_after_discount)