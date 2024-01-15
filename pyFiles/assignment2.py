def task1():
    primary_colors = ['red', 'green', 'blue']
    first_color = input("Enter first color: ")
    second_color = input("Enter second color: ")
    if first_color not in primary_colors or second_color not in primary_colors:
        print("Error color")
        return
    if first_color == second_color:
        print(first_color)
        return
    # red - r = 114, green - g = 103, blue - b = 98
    first_color = ord(first_color.lower()[0])
    second_color = ord(second_color.lower()[0])
    color_sum = first_color + second_color
    if color_sum == 217:
        print("yellow")
    elif color_sum == 212:
        print("purple")
    elif color_sum == 201:
        print("cyan")

def task2():
    user_input = int(input())
    if user_input < 0 or user_input > 36:
        print("input error")
        return
    if user_input == 0:
        print("green")
        return
    isRed = True
    x = 1
    numbers = [10, 18, 28]
    while x <= 36:
        if x == user_input:
            print("red" if isRed else "black")
            break
        x += 1
        if x not in numbers:
            isRed = not isRed


def task3():
    cells = []
    for i in range(2):
        user_input = input("Enter cell in format a1: ").lower()
        cells.append([ord(user_input[0]), int(user_input[1])])
        if cells[i][0] > 104 or cells[i][0] < 97 or cells[i][1] > 8 or cells[i][1] < 0:
            print("Wrong cell")
            return
    if cells[0][0] - cells[1][0] == cells[0][1] - cells[1][1]:
        print("YES")
    else:
        print("NO")

def task4():
    a1, b1, a2, b2 = map(int, input().split())
    if a2 > b1 or a1 > b2:
        print("Empty set")
        return
    start = max(a1, a2)
    end = min(b1, b2)
    if start == end:
        print(start)
    else:
        print(f'({start} {end})')

def task5():
    shift = int(input())
    user_input = [letter for letter in input().lower()]
    for i in range(len(user_input)):
        if ord(user_input[i]) - shift < 97:
            user_input[i] = chr(122 - (96 - (ord(user_input[i]) - shift)))
        else:
            user_input[i] = chr(ord(user_input[i]) - shift)

    print("".join(let for let in user_input))

def code_examples():
    example_string = "that IS mY EXAMPLE string FoR assignment 2"
    print(f"Example string = '{example_string}'")
    print(f"capitalize: {example_string.capitalize()}")
    print(f"swapcase: {example_string.swapcase()}")
    print(f"title: {example_string.title()}")
    print(f"lower: {example_string.lower()}")
    print(f"upper: {example_string.upper()}")
    print(f"count('a'): {example_string.count('a')}")
    print(f"startswith('that'): {example_string.startswith('that')}")
    print(f"endswith('that'): {example_string.endswith('that')}")
    print(f"rfind('string'): {example_string.rfind('string')}")
    print(f"index('m'): {example_string.index('m')}")
    print(f"rindex('a'): {example_string.rindex('a')}")
    print(f"('  hello, world ').strip: {'  hello, world '.strip()}")
    print(f"('  hello, world ').rstrip: {'  hello, world '.rstrip()}")
    print(f"('  hello, world ').lstring: {'  hello, world '.lstrip()}")
    print(f"replace: {example_string.replace('assignment', 'task')}")
    print(f"isalnum: {example_string.isalnum()}")
    print(f"('b').isalpha: {'b'.isalpha()}")
    print(f"('b').isdigit: {'b'.isdigit()}")
    print(f"('B').islower: {'B'.islower()}")
    print(f"('B').isupper: {'B'.isupper()}")
    print(f"('  ')isspace: {'  '.isspace()}")

def task11():
    leg = int(input())
    count = leg
    while count > 0:
        print("*" * count)
        count -= 1


def task12():
    m, n = map(int, input().split())
    for i in range(m, n + 1) if m < n else range(m, n - 1, -1):
        print(i)


def task13():
    n = int(input())
    numbers = sorted([int(input()) for i in range(n)])
    print(numbers[-1])
    print(numbers[-2])

def task14():
    n = int(input())
    fibbonaci = [1, 1]
    for i in range(n - 2):
        fibbonaci.append(fibbonaci[len(fibbonaci) - 1] + fibbonaci[len(fibbonaci) - 2])
    for number in fibbonaci:
        print(number, end=" ")


def task15():
    count = 0
    mark = int(input())
    while 1 <= mark <= 5:
        if mark == 5:
            count += 1
        mark = int(input())
    print(count)


def task16():
    price = int(input())
    count = 0
    if price > 0:
        while price >= 25:
            price -= 25
            count += 1
        while price >= 10:
            price -= 10
            count += 1
        while price >= 5:
            price -= 5
            count += 1
        if price > 0:
            count += price
    print(count)


def task17():
    sequence = input()
    for i in range(len(sequence) - 2, 0, -1):
        if int(sequence[i]) > int(sequence[i - 1]):
            print("NO")
            return
    print("YES")


def task18_for():
    print("Program will output numbers in range (1, 21) (last number will be 20).")
    input_continue = int(input("Enter a number that program will skip: "))
    input_break = int(input("Enter a number at which program will terminate: "))
    for i in range(1, 21):
        if i == input_continue:
            continue
        if i == input_break:
            print(i)
            break
        print(i, end=" ")

def task19_while():
    print("Program will output letters a-z.")
    input_continue = ord(input("Enter letter that program will skip: "))
    input_break = ord(input("Enter letter at which program will terminate: "))
    counter = 97
    while counter <= 122:
        if counter == input_continue:
            counter += 1
            continue
        if counter == input_break:
            print(chr(counter))
            break
        print(chr(counter), end=" ")
        counter += 1

