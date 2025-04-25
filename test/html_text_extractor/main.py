# Find a file path
# ask for html parser
# extract the text and save it into a file

import re
import os

def get_file_path():
    while True:
        path = input("Please enter the file path: ").strip()

        #check if directory format is valid
        if re.search(r"^(.+)/([^/]+\.html)$", path):
            return path
        else:
            print("The Directory address format is not valid!")

def extract_text_from_xpath():
    pass

def get_html_xpath():
    xpath = input("Please enter the inner html xpath: ")
    return xpath

# def check_file_existence(path):
#     pass


def main():

    while True:
        path = get_file_path()
        if os.path.exists(path):
            break
        else:
            print("File doesn't exist!")
    file = path.rsplit('/',1)[-1]
    print(file)
    xpath = get_html_xpath()
    read_file = open(file, 'r')
    read_file = read_file.readlines()
    for row in read_file:
        if xpath not in read_file:
            print("Xpath not found!\n Are you sure about the Xpath format?")


if __name__ == "__main__":
    main()

#/home/ariyan/Desktop/practice/test/html_text_extractor/sample.html