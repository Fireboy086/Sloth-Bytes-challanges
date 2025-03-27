def lemonade(bills):
    saved_money = []
    for bill in bills:
        if bill == 5:
            saved_money.append(bill)
            print(f"### added 5$ bill to saved_money, {saved_money}")
        elif bill == 10:
            if 5 in saved_money:
                saved_money.remove(5)
                saved_money.append(10)
                print(f"### removed 5$ bill to saved_money, {saved_money}")
            else:
                return False
        elif bill == 20:
            if 5 in saved_money and 10 in saved_money:
                saved_money.remove(10)
                saved_money.remove(5)
                saved_money.append(20)
                print(f"### added 10$ and 5$ bill to saved_money, {saved_money}")
            elif saved_money.count(5)>=3:
                for _ in range(3):
                    saved_money.remove(5)
                    print(f"### removed 3 5$ bills from saved money, {saved_money}")
                    saved_money.append(20)
            else:
                return False
    return True