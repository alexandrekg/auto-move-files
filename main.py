import sys


def main():
    option = sys.argv[1]
    if option == 'all':
        return 'Copy all files'
    elif option == 'pdf':
        return 'Copy only pdf files'
    elif option == 'json':
        return 'Copy only json files'
    else:
        return 'Option not valid'


if __name__ == "__main__":
    main()
