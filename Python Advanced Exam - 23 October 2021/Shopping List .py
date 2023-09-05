# Only func

def shopping_list(budget, **kwargs):
    final_text = ''
    if budget < 100:
        final_text = "You do not have enough budget."
        return final_text

    purchase_count = 0
    for name,tuple in kwargs.items():
        if purchase_count == 5: return final_text
        price, quantity = tuple
        if price * quantity <= budget:
            final_text += f"You bought {name} for {price * quantity:.2f} leva.\n"
            budget -= price * quantity
            purchase_count += 1
    return final_text

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))



