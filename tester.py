import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError

def run_tests(cases: list[tuple], timeout: float = 1.0, test_function=None, function_name: str = "Unknown") -> None:
    """
    Generic test runner for any function.
    Args:
        cases: list of tuples of (input, expected output) or (input_args, expected output) 
        timeout: timeout in seconds
        test_function: function to test
        function_name: name of the function being tested for display
    Returns:
        None
    """
    if not cases:
        print("❌ No test cases provided!")
        return
        
    if test_function is None:
        print("❌ No test function provided!")
        return
    
    passed = 0
    failed = 0
    
    for caseIndex, case in enumerate(cases):
        header = f" -----------====#### Case {caseIndex+1} ####====-----------" + (3-len(str(caseIndex+1)))*"-"+ " "
        print(f"{header:^148}")
        start_time = time.time()
        
        try:
            with ThreadPoolExecutor() as executor:
                # Handle different input formats
                if len(case) == 2:
                    test_input, expected = case
                    if isinstance(test_input, tuple):
                        # Multiple arguments
                        future = executor.submit(test_function, *test_input)
                    else:
                        # Single argument
                        future = executor.submit(test_function, test_input)
                else:
                    print(f"{'❌ Invalid test case format':^148}")
                    failed += 1
                    continue
                    
                test_result = future.result(timeout=timeout)
                
            time_taken = time.time() - start_time
            
            # Check if result is correct
            if expected == test_result:
                msg = f"✅ Passed in {time_taken:.3f}s"
                print(f"{msg:^148}")
                passed += 1
            else:
                print(f"{'❌ Failed: Incorrect result':^148}")
                print(f"{'Expected: ' + str(expected):^148}")
                print(f"{'Got: ' + str(test_result):^148}")
                failed += 1
                
        except TimeoutError:
            print(f"{'⏱️ Failed: took too long':^148}")
            failed += 1
        except Exception as e:
            print(f"{'💥 Failed: Error occurred':^148}")
            print(f"{'Error: ' + str(e):^148}")
            failed += 1
    
    # Summary
    summary_header = f" -----------====#### SUMMARY ####====-----------"
    print(f"{summary_header:^148}")
    summary_msg = f"📊 {passed} passed, {failed} failed"
    print(f"{summary_msg:^148}")
    
    if failed == 0:
        success_msg = "🎉 All tests passed!"
        print(f"{success_msg:^148}")
    else:
        fail_msg = f"😞 {failed} test(s) failed!"
        print(f"{fail_msg:^148}")

def run_simple_tests(test_pairs: list[tuple], function_name: str = "Unknown") -> bool:
    """
    Simple test runner for quick boolean pass/fail tests.
    Args:
        test_pairs: list of (test_description, boolean_result)
        function_name: name of the function being tested
    Returns:
        True if all tests passed, False otherwise
    """
    header = f" -----------====#### Testing {function_name} ####====-----------"
    print(f"{header:^148}")
    
    passed = 0
    failed = 0
    
    for desc, result in test_pairs:
        if result:
            msg = f"✅ {desc}"
            print(f"{msg:^148}")
            passed += 1
        else:
            msg = f"❌ {desc}"
            print(f"{msg:^148}")
            failed += 1
    
    summary_header = f" -----------====#### SUMMARY ####====-----------"
    print(f"{summary_header:^148}")
    summary_msg = f"📊 {passed} passed, {failed} failed"
    print(f"{summary_msg:^148}")
    
    if failed == 0:
        success_msg = "🎉 All tests passed!"
        print(f"{success_msg:^148}")
    else:
        fail_msg = f"😞 {failed} test(s) failed!"
        print(f"{fail_msg:^148}")
    
    return failed == 0

if __name__ == "__main__":
    print("🧪 Generic tester.py - Use this in your challenge files!")
    print("Example usage:")
    print("import tester")
    print("tester.run_tests(test_cases, test_function=your_function, function_name='Your Function')")