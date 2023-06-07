import sys


def main():
    if len(sys.argv) == 1:
        print('You have to select a option')
        return
    
    option = sys.argv[1]
    if option == 'all':
        print('Copy all files')
    elif option == 'pdf':
        print('Copy only pdf files')
    elif option == 'json':
        print('Copy only json files')
    else:
        print('Option not valid')


if __name__ == "__main__":
    main()
