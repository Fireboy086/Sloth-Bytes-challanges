def transform_to_dict(original):
    prev_check = None
    analyzed = []
    for i in original:
        #print(f"======================> checking: {i}")
        if i != prev_check:
            prev_check = i
            analyzed.append({i:1})
            #print(f"created entry {i}, {analyzed}")
        elif i == prev_check:
            analyzed[len(analyzed)-1][i] +=1
            #print(f"added 1 to {i} in analyzed[{len(analyzed)-1}],  {analyzed}")
    return analyzed

def subtract_lists(list1,list2):
    out_list = []
    for i,dictionary in enumerate(list1):
        # Since there's exactly one item, you can unpack it directly
        (key, value), = dictionary.items()
        try:
            (key2,value2), = list2[i].items()
        except IndexError:
            # print("indexError")
            return False
        if key == key2:
            subtraction = value2- value
            if subtraction >=0:
                out_list.append({key:subtraction})
            else: 
                # print("not enough")
                return False
        else: 
            # print("keys dont match")
            return False
    return out_list

def isLongPressed(original,typed):
    """Check if typed string could be result of long pressing keys while typing original"""
    original_list = transform_to_dict(original)
    typed_list = transform_to_dict(typed)

    test1 = subtract_lists(original_list,typed_list) #checks for more than needed keys, not enough keys,some other situations
    test2 = "".join(next(iter(s)) for s in original_list) == "".join(next(iter(c)) for c in typed_list) #tests only for if hey were supposed to be the same
    if test1 != False and test2:
        return True
    else: 
        return False

if __name__ == "__main__":
    import tester
    from Cases import STICKY_KEYS_TEST_CASES
    
    tester.run_tests(
        cases=STICKY_KEYS_TEST_CASES,
        test_function=lambda original, typed: isLongPressed(original, typed),
        function_name="isLongPressed"
    )
