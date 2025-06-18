def birthdayCakeCandles(candles):
    print("Starting counting candles with these heights:", candles)
    if len(candles) == 0:
        print("  No candles were given")
        return 0
    sortedCandles = sorted(candles, reverse=True)
    print("  Sorted candles by height:", sortedCandles)
    highestCandle = sortedCandles[0]
    print("  Highest candle:", highestCandle)
    for i, height in enumerate(sortedCandles):
        print(f"    Checking candle with height {height} against highest: {highestCandle}")
        if height < highestCandle:
            print(f"    Candle {i}:{height} is lower, remove everything after")
            totalCandles = sortedCandles[:i]
            print(f"    Left with {totalCandles}, len = {len(totalCandles)}")
            return len(totalCandles)
    print("  Every candle is the same")
    return len(sortedCandles)




expected = 2
FuncInput = [4,4,1,3]
print("The output -MATCHES- the requirements"if birthdayCakeCandles(FuncInput)==expected else "The output -DOES NOT MATCH- the reqirements")
print("\n +========================================+ \n")
# The tallest candles are 4. There are 2 candles with this height, so the function should return 2.output = 4
expected = 4
FuncInput = [1,1,1,1]
print("The output -MATCHES- the requirements"if birthdayCakeCandles(FuncInput)==expected else "The output -DOES NOT MATCH- the reqirements")
print("\n +========================================+ \n")
#  All candles are the same height, so all are the tallest.
expected = 0
FuncInput = []
print("The output -MATCHES- the requirements"if birthdayCakeCandles(FuncInput)==expected else "The output -DOES NOT MATCH- the reqirements")
print("\n +========================================+ \n")
# No candles, so nothing to blow out.
