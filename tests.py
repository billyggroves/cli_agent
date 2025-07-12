# from functions.get_files_info import get_files_info
from functions.write_file import write_file

def test_get_files_info1():
    val = write_file("calculator", "main.txt", "hello")
    if val != None:
        print(f"{val}")
    return

# def test_get_files_info2():
#     val = run_python_file("calculator", "tests.py")
#     if val != None:
#         print(f"{val}")
#     return

# def test_get_files_info3():
#     val = run_python_file("calculator", "../main.py")
#     if val != None:
#         print(f"{val}")
#     return

# def test_get_files_info4():
#     val = run_python_file("calculator", "nonexistent.py")
#     if val != None:
#         print(f"{val}")
#     return

# def test_get_files_info5():
#     val = get_file_content("calculator", "\n")
#     if val != None:
#         print(f"{val}")
#     return

# def test_get_files_info6():
#     val = get_file_content("calculator", "main.py")
#     if val != None:
#         print(f"{val}")
#     return

test_get_files_info1()
# test_get_files_info2()
# test_get_files_info3()
# test_get_files_info4()
# test_get_files_info5()
# test_get_files_info6()
