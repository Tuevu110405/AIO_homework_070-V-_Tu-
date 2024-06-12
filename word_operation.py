# Task 1
import numpy as np


def find_max1(lst, k):
    # create sub_list
    lst1 = []
    # list saving max value
    result = []

    # base sub_list
    for i in range(k):
        lst1.append(lst[i])
    result.append(max(lst1))

    # check remaining sub_list
    for i in range(k, len(lst)):
        lst1.pop(0)  # always remove the first element of the sub_list
        lst1.append(lst[i])
        result.append(max(lst1))

    return result


# Task 2
def count_chars(str):
    # dict save result
    result = {}

    for char in str:
        if char in result:
            continue
        else:
            a = str.count(char)
            result[char] = a
    return result


# Task 3
def word_count(path):
    result = {}

    with open(path, "r") as f:
        content = f.read()
        words = content.split()
        for word in words:
            if word in result:
                continue
            else:
                a = words.count(word)
                result[word] = a
    return result


# Task 4


def levenshtein_distance(str1, str2):
    # distance variable
    a = np.zeros((len(str1)+1, len(str2)+1))
    # create inserting row
    for i in range(1, len(str2)+1):
        a[0][i] = i

    # deleting column
    for j in range(1, len(str1)+1):
        a[j][0] = j

    # handeling remaining entry
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2)+1):
            insert = a[i-1][j] + 1
            delete = a[i][j-1] + 1
            if str1[i-1] == str2[j-1]:
                sub = a[i-1][j-1]
            else:
                sub = a[i-1][j-1] + 1
            a[i][j] = min(insert, delete, sub)

    return a[len(str1)][len(str2)]

# function interacting with users


def exercise1():
    input_string = input("Nhập các số nguyên, tách biệt bởi dấu phẩy: ")


    list_elements = [int(element.strip()) for element in input_string.split(',')]

    k = int(input('Nhập số lượng phần tử mỗi list con: '))
    result = find_max1(list_elements, k)
    print(result)


def exercise2():
    str2 = input('Nhập chuỗi bạn muốn đếm số lượng kí tự: ')
    print(count_chars(str2))


def exercise3():
    path = 'Nhập đường dẫn tới file bạn mong muốn: '
    print(word_count(path))


def exercise4():
    str1 = 'Nhập từ ban đầu: '
    str2 = 'Nhập từ bạn muốn chuyển:'
    print(f'khoảng cách lavenshtein: {levenshtein_distance(str1, str2)}')


# Example usage:
assert find_max1([3, 4, 5, 1, -44], 3) == [5, 5, 5]
lst = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(find_max1(lst, k))

assert count_chars("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
string = 'smiles'
print(count_chars(string))


path = "G:\AIO2024\Home_work\module 1\P1_data.txt"
result = word_count(path)
assert result['who'] == 3
print(result['man'])


exercise1()
exercise2()
exercise3()
exercise4()
