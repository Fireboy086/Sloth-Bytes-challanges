def birthdayCakeCandles(candles):
    """Count how many candles have the maximum height"""
    if len(candles) == 0:
        return 0
    sortedCandles = sorted(candles, reverse=True)
    # print("  Sorted candles by height:", sortedCandles)
    highestCandle = sortedCandles[0]
    # print("  Highest candle:", highestCandle)
    for i, height in enumerate(sortedCandles):
        # print(f"    Checking candle with height {height} against highest: {highestCandle}")
        if height < highestCandle:
            # print(f"    Candle {i}:{height} is lower, remove everything after")
            totalCandles = sortedCandles[:i]
            # print(f"    Left with {totalCandles}, len = {len(totalCandles)}")
            return len(totalCandles)
    # print("  Every candle is the same")
    return len(sortedCandles)


if __name__ == "__main__":
    import tester
    from Cases import BIRTHDAY_CANDLES_TEST_CASES
    
    tester.run_tests(
        cases=BIRTHDAY_CANDLES_TEST_CASES,
        test_function=birthdayCakeCandles,
        function_name="birthdayCakeCandles"
    )
