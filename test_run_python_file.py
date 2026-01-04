from functions.utils import indent
from functions.run_python_file import run_python_file

def test_checks(output, expect_success=True):
    if output.startswith("Error:") and expect_success:
        return indent("- Test failed. Expected success")
    if output.startswith("Error:") and not expect_success:
        return indent("- Test Passed! Error was expected")
    if output.startswith("Process exited with code"):
        if expect_success:
            return indent("- Test failed. Expected exit code 0")
        else:
            return indent("- Test Passed! Non-zero exit code expected")
    if expect_success:
        return indent("- Test Passed! No errors encountered")
    return indent("- Test failed. Should have encountered an error")

def main():
    print("Test 1: 'calculator', 'main.py'")
    test1 = run_python_file("calculator", "main.py")
    print(indent(test1))
    print(test_checks(test1))

    print("Test 2: 'calculator', 'main.py', ['3 + 5']")
    test2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(indent(test2))
    print(test_checks(test2))

    print("Test 3: 'calculator', 'tests.py'")
    test3 = run_python_file("calculator", "tests.py")
    print(indent(test3))
    print(test_checks(test3))

    print("Test 4: 'calculator', '../main.py'")
    test4 = run_python_file("calculator", "../main.py")
    print(indent(test4))
    print(test_checks(test4, expect_success=False))

    print("Test 5: 'calculator', 'nonexistent.py'")
    test5 = run_python_file("calculator", "nonexistent.py")
    print(indent(test5))
    print(test_checks(test5, expect_success=False))

    print("Test 6: 'calculator', 'lorem.txt'")
    test6 = run_python_file("calculator", "lorem.txt")
    print(indent(test6))
    print(test_checks(test6, expect_success=False))

if __name__ == "__main__":
    main()