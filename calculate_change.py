def calculate_change(payment, cost):
    change = payment - cost
    fifty_thousand = change //50000
    print(f'50000원 지폐: {fifty_thousand}장')
    ten_thousand = (change - (fifty_thousand * 50000)) // 10000
    print(f'10000원 지폐: {ten_thousand}장')
    five_thousand = (change - ((fifty_thousand * 50000) + (ten_thousand * 10000))) // 5000
    print(f'5000원 지폐: {five_thousand}장')
    one_thousand = (change - ((fifty_thousand * 50000) + (ten_thousand * 10000) + (five_thousand * 5000))) // 1000
    print(f'1000원 지폐: {one_thousand}장')
    

#test
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)
