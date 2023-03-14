# Author: Omer Gertler

DIRECTORY = r"C:\Users\omer\Desktop\Notebooks-master\Notebooks-master\week05\resources\logo.jpg"


def find_secrete_messages(my_dir):
    """
    The function search for secret massages in binary file.
    Message is sequence of at least 5 lowercase letters that ends with '!'.
    :param my_dir: file for searching
    :return: all secret messages from the file
    """
    my_str = ''
    with open(my_dir, 'rb') as f:
        tav = f.read(1)
        while tav:
            if tav.islower():
                my_str += tav.decode()
            elif tav == b'!' and len(my_str) >= 5:
                my_str += tav.decode()
                yield my_str
                my_str = ''
            tav = f.read(1)


my_generator = find_secrete_messages(DIRECTORY)
for item in my_generator:
    print(item)
