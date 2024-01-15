import os


def get_path():
    path = input("Enter the path: ")
    print(os.listdir(path))


def current_directory():
    print(os.getcwd())


def check_exists():
    path = input("Enter the path: ")
    print("File exists" if os.path.exists(path) else "File does not exists")


def create_directory():
    name = input("Enter the name of the directory: ")
    os.mkdir(name)


def file_size():
    path = input("Enter the path of the file: ")
    print(os.path.getsize(path))


def files_of_extension():
    path = input("Enter the path of the directory: ")
    extension = input("Enter the file extension without dot: ")
    all_files = os.listdir(path)
    for file in all_files:
        if file.endswith(extension):
            print(file)


def home_directory():
    path = input("Enter the path of the directory: ")
    print(os.path.expanduser(path))


def remove_file():
    path = input("Enter the path of the file: ")
    os.remove(path)


def is_directory():
    path = input("Enter the path of the directory: ")
    print("Is directory" if os.path.isdir(path) else "Is not directory")


def execute_command():
    command = input("Enter the system command: ")
    os.system(command)


