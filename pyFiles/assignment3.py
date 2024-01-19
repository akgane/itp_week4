vowels = ['a', 'e', 'i', 'o', 'u']


def lists1():
    def task1(list1, list2):
        result = []
        for i in range(min(len(list1), len(list2))):
            result.append(list1[i])
            result.append(list2[i])
        if len(list1) != len(list2):
            if len(list1) > len(list2):
                for i in range(len(list2), len(list1)):
                    result.append(list1[i])
            else:
                for i in range(len(list1), len(list2)):
                    result.append(list2[i])
        return result

    print("Write two lists of integers. Numbers should be separated by a space."
          "\nExample: 1 2 3 4 5")
    first = list(map(int, input("First list: ").split()))
    second = list(map(int, input("Second list: ").split()))

    print(f"Result list: {task1(first, second)}")


def lists2():
    n = int(input("Enter n: "))
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(i ** 2)
        else:
            result.append(i ** 3)
    print(f"Result list: {result}")


def count_vowels(word):
    count = 0

    for letter in word:
        if letter in vowels:
            count += 1
    return count


def lists3():
    def task3(strings):
        for j in range(len(strings)):
            for i in range(len(strings) - 1):
                if count_vowels(strings[i]) > count_vowels(strings[i + 1]):
                    temp = strings[i]
                    strings[i] = strings[i + 1]
                    strings[i + 1] = temp
        return strings

    print("Enter strings separated by spaces.\nExample: apple car world")
    user_input = list(map(str, input().split()))

    print(f"Result list: {task3(user_input)}")


def lists4():
    def task4(numbers):
        for i in range(0, len(numbers), k):
            if len(numbers[i:]) < k:
                break
            cut = numbers[i: i + k]
            numbers[i: i + k] = reversed(cut)
        return numbers

    k = int(input("Enter k: "))
    print("Enter numbers separated by spaces.\nExample: 1 2 3 4")
    user_input = list(map(int, input().split()))

    print(f"Result list: {task4(user_input)}")


def lists5():
    def task5(first, second):
        result = []
        for i in range(len(first)):
            if first[i] in second and first[i] not in result:
                result.append(first[i])
        return result

    print("Enter two lists of numbers. Numbers should be separated by spaces."
          "\nExample: 1 2 3 4")
    first_list = list(map(int, input().split()))
    second_list = list(map(int, input().split()))

    print(f"Result: {task5(first_list, second_list)}")


def tuples1():
    def tuple_handler(tuples):
        under = []
        over = []
        for i in range(len(tuples)):
            if tuples[i][1] >= 18:
                under.append(tuples[i][0])
            else:
                over.append(tuples[i][2])
        return under, over

    print("Enter the students as shown in the example (name age grade):\n"
          "Akhan 19 3.5, Ismail 18 3.6")
    students_input = list(input().split(','))
    students = []
    for data in students_input:
        data = data.split()
        students.append((data[0], int(data[1]), float(data[2])))
    under, over = tuple_handler(students)
    print(f"Under 18: {under}")
    print(f"Over 18: {over}")
    # Akhan 19 2.3, Nurali 15 2.1, Ismail 18 3.4, Abai 13 1, Asanali 18 3.1


def tuples2():
    def task7(first, second):
        result = []
        for element in first:
            if element in second and element not in result:
                result.append(element)
        return tuple(result)

    print("Enter two tuples of integers. Integers should be separated by space.\n"
          "Example: 1 2 3 4")
    first_tuple = tuple(map(int, input().split()))
    second_tuple = tuple(map(int, input().split()))
    print(f"Result tuple: {task7(first_tuple, second_tuple)}")


def tuples3():
    def task8(user_input):
        vowels_count, consonants_count = 0, 0
        for char in user_input:
            if char.isalpha():
                if char in vowels:
                    vowels_count += 1
                else:
                    consonants_count += 1
        counts = (vowels_count, consonants_count)
        return counts

    user_input = input("Enter string: ").lower()
    print(f"Result tuple: {task8(user_input)}")


def tuples4():
    def tuple_handler(tuples):
        ages1 = []
        names1 = []
        grades1 = []
        for j in range(len(tuples)):
            names1.append(tuples[j][0])
            ages1.append(tuples[j][1])
            grades1.append(tuples[j][2])

        return names1, ages1, grades1

    def task9(students_input):
        for i in range(len(students_input)):
            data = students_input[i].split()
            students_input[i] = (data[0], int(data[1]), float(data[2]))
        return tuple_handler(students_input)

    print("Enter the students as shown in the example (name age grade):\n"
          "Akhan 19 3.5, Ismail 18 3.6")
    students_input = list(input().split(','))
    names, ages, grades = task9()
    print(f"Names: {names}")
    print(f"Ages: {ages}")
    print(f"Grades: {grades}")


def tuples5():
    def task10(salaries):
        for j in range(len(salaries)):
            for i in range(len(salaries) - 1):
                if salaries[i][1] < salaries[i + 1][1]:
                    temp = salaries[i]
                    salaries[i] = salaries[i + 1]
                    salaries[i + 1] = temp
        return salaries

    print("Enter data as shown in the example (name salary):\n"
          "Akhan 95000, Asanali 101000")
    user_input = list(input().split(','))
    salaries = []
    for i in range(len(user_input)):
        data = user_input[i].split()
        salaries.append((data[0], int(data[1])))

    print(f"Result: {task10(salaries)}")


def sets1():
    def set_handler(first_set, second_set):
        return first_set.union(second_set), first_set.intersection(second_set), first_set.difference(second_set)

    print("Enter two sets of integers. Integers should be separated by spaces."
          "\nExample: 1 2 3 4 5")
    first = set(map(int, input().split()))
    second = set(map(int, input().split()))
    union, intersection, difference = set_handler(first, second)
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
    print(f"Difference: {difference}")


def sets2():
    print("Enter numbers separated by spaces.\nExample: 1 2 3 4")
    numbers = list(map(int, input().split()))
    uniques = []
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            continue
        for j in range(len(numbers)):
            if i == j:
                continue
            if numbers[i] == numbers[j] and numbers[i] not in uniques:
                uniques.append(numbers[i])
    return set(uniques)


def sets3():
    user_input = input("Enter the string: ").lower()
    used_vowels = []
    vowels_count = []
    for char in user_input:
        if char.isalpha() and char in vowels:
            if char in used_vowels:
                vowels_count[used_vowels.index(char)] += 1
            else:
                used_vowels.append(char)
                vowels_count.append(1)
    for i in range(len(used_vowels) - 1, -1, -1):
        if vowels_count[i] > 1:
            del used_vowels[i]
            del vowels_count[i]
    return set(used_vowels)


def sets4(sets):
    commons = set.intersection(*sets)
    is_subset = False
    for i, first in enumerate(sets):
        for j, second in enumerate(sets):
            if i != j and first <= second:
                is_subset = True
    return commons, is_subset


def sets5(first_set, second_set):
    return first_set.difference(second_set), first_set.symmetric_difference(second_set)


def dictionaries1(user_dictionary):
    def bubble_sort(numbers):
        for i in range(len(numbers)):
            for j in range(len(numbers) - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers

    for key, numbers in user_dictionary.items():
        user_dictionary[key] = bubble_sort(numbers)
    return user_dictionary


def dictionaries2(tuples_list):
    return {item[0]: item[1] for item in tuples_list}


def dictionaries3(first_dict, second_dict):
    result = {}
    for key, value in first_dict.items():
        for key1, value1 in second_dict.items():
            if key == key1:
                result[key] = value + value1
    return result


def dictionaries4(courses):
    #example
    school_data = {
        'Math': {'Alice': 20, 'Bob': 15, 'Charlie': 18},
        'Science': {'Alice': 25, 'Bob': 22, 'David': 20},
        'History': {'Charlie': 15, 'David': 18}
    }
    count = 0
    for course_key, course in courses.items():
        count += len(course)
    return count

def dictionaries5(user_dictionary):
    result = []
    for key, value in user_dictionary.items():
        result.append((key, value))

    for i in range(len(result)):
        for j in range(len(result) - 1):
            if result[j][1] < result[j + 1][1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


