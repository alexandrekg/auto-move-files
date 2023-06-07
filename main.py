import sys
import glob


def main():
    if len(sys.argv) == 1:
        print('You have to select a option')
        return

    option = sys.argv[1]
    if option == 'all':
        print('Copy all files')
        print(glob.glob('./tmp/*'))
    elif option == 'pdf':
        print('Copy only pdf files')
        print(glob.glob('./tmp/*.pdf'))
    elif option == 'json':
        print('Copy only json files')
        print(glob.glob('./tmp/*.json'))
    else:
        print('Option not valid')


if __name__ == "__main__":
    main()
