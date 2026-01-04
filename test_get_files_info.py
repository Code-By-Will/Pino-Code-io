from functions.get_files_info import get_files_info
from functions.utils import indent

def main():
    test1 = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(indent(test1))

    test2 = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(indent(test2))

    test3 = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(indent(test3))

    test4 = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(indent(test4))

if __name__ == "__main__":
    main()