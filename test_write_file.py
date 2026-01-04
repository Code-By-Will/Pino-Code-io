from functions.utils import indent
from functions.write_file import write_file
'''
Test Cases:
    write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
'''

def check_passed(result, expect_success=True):
    if result.startswith("Error:") and expect_success:
        return indent("- Test failed. Expected Success")
    if result.startswith("Error:") and not expect_success:
        return indent("- Test Passed! Error expected")
    if result.startswith("Successfully wrote to ") and expect_success:
        return indent("- Test Passed! Write was successfull")
    if result.startswith("Successfully wrote to ") and not expect_success:
        return indent("- Test failed. Error expected, but test passed")
    return "Error: unreachable state."

def main():
    '''
    Test Cases:
        write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    
    uv run test_write_file.py
    Expecting exit code: 0
    Expecting stdout to contain all of:
        28 characters written
        26 characters written
        Error:
    ''' 
    print("Test 1: 'calculator', 'lorem.txt', 'wait, this isn't lorem ipsum'")
    test1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"Result: {test1}")
    print(check_passed(test1))

    print("\nTest 2: 'calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet'")
    test2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"Result: {test2}")
    print(check_passed(test2))

    print("\nTest 3: 'calculator', '/tml/temp.txt', 'this should not be allowed'")
    test3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"Result: {test3}")
    print(check_passed(test3, expect_success=False))

if __name__ == "__main__":
    main()