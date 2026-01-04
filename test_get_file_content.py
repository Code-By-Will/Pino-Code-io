from config import MAX_CHARS
from functions.get_file_content import get_file_content
from functions.utils import indent

def test_checks(s, expect_success=True):
    if s.startswith("Error:") and expect_success:
        return indent("- Test failed. Expected success")
    if s.startswith("Error:") and not expect_success:
        return indent("- Test Passed! Error was expected")
    if len(s) > MAX_CHARS and "[...File" in s:
        if expect_success:
            return indent("- Test Passed! Text was truncated")
        else:
            return indent("- Test failed. Error was expected")
    if len(s) < MAX_CHARS and expect_success:
        return indent("- Test Passed! Text under MAX_CHARS")
    if len(s) < MAX_CHARS and not expect_success:
        return indent("- Test failed. Error was expected")
    return "Error: unreachable state."

def main():
    print("\nTest 1 'calculator', 'lorem.txt'")
    test1 = get_file_content("calculator", "lorem.txt")
    print(f"test1:\n{indent(test1)}\n")
    print(test_checks(test1))

    print("\nTest 2 'calculator', 'pkg/calculator.py'")
    test2 = get_file_content("calculator", "pkg/calculator.py")
    print(f"test2:\n{indent(test2)}\n")
    print(test_checks(test2))

    print("\nTest 3 'calculator', 'main.py'")
    test3 = get_file_content("calculator", "main.py")
    print(f"test3:\n{indent(test3)}\n")
    print(test_checks(test3))

    print("\nTest 4 'calculator', '/bin/cat'")
    test4 = get_file_content("calculator", "/bin/cat")
    print(f"test4:\n{indent(test4)}\n")
    print(test_checks(test4, False))

    print("\nTest 5 'calculator', 'pkg/does_not_exist.py'")
    test5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"test5:\n{indent(test5)}\n")
    print(test_checks(test5, False))

if __name__ == "__main__":
    main()