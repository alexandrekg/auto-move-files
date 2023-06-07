import sys
import glob
import os


def main():
    if len(sys.argv) == 1:
        print('You have to select a option')
        return
    if len(sys.argv) == 2:
        print('Insert the name of the new folder')
        return

    option = sys.argv[1]
    new_folder = sys.argv[2]
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

    if not os.path.isdir(new_folder):
        os.makedirs(new_folder)
        print(f'A folder named {new_folder} was created.')
    else:
        print(f'Already have a folder named {new_folder}')


if __name__ == "__main__":
    main()
