warehouse = {
    "warehousename": "zain electronics",
    "products": {
        "laptop": {"price": 50000, "stock": 10},
        "mouse": {"price": 1500, "stock": 50},
        "keyboard": {"price": 3000, "stock": 20}
    }
}



warehouse['products']['mouse']['stock'] = 90

T0tal_worth = warehouse["products"]["laptop"]["stock"]*warehouse["products"]["laptop"]["price"]

worth_after_tex = (T0tal_worth)* 1.13
print(f"The name of ware house is {warehouse['warehousename'].title()}")
print(f"The total worth of laptop is {T0tal_worth}")
print(f"Worth after Tex {worth_after_tex}")