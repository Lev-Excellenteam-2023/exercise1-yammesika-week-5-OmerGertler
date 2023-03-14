import os


def get_files_from_dir(directory):
    """
    Returns a list of all the files in a given directory that start with 'deep'
    :param directory: The directory for searching
    :return: List of the files in the directory that start with 'deep'
    """
    return [f for f in os.scandir(directory) if os.path.isfile(f) and f.startswith('deep')]


def main():
    direction = input('Enter directory:\n')
    files = get_files_from_dir(direction)
    print(f'{files}\nfinish')


if __name__ == "__main__":
    main()
