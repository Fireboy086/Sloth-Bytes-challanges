def loop(nums,cursor):
    for jump in range(nums[cursor],0,-1):
        if cursor+jump >= len(nums)-1:
            # print("landed outside")
            return True
        landing = nums[cursor+jump]
        # print(landing)
        if landing == 0:
            pass
        else:
            if loop(nums,cursor+jump):
                return True
            else:
                pass
    return False

def func(nums):
    if len(nums) == 1:
        return True
    cursor = 0
    return loop(nums,cursor)


if __name__ == "__main__":
    import tester
    from Cases import JUMPGAME_TEST_CASES
    
    tester.run_tests(JUMPGAME_TEST_CASES,test_function=func,timeout=100)