def calculate_total(pack_fee, *food_fee, delivery_fee=10, **coupon):
    total = pack_fee + delivery_fee
    for fee in food_fee:
        total += fee

    for key, value in coupon.items():
        if key != 'discount':
            total -= value

    if 'discount' in coupon:
        total *= coupon['discount']

    return total


result = calculate_total(5, 10, 20, first_order=5, discount=0.8)
print(result)