import sys
import glob
import os
import shutil


def main():
    if len(sys.argv) == 1:
        print('You have to select a option')
        return
    if len(sys.argv) == 2:
        print('Insert the name of the new folder')
        return

    option = sys.argv[1]
    new_folder = sys.argv[2]
    _create_new_folder(new_folder)

    if option == 'all':
        for file in glob.glob('./tmp/*'):
            print(f'Copying {file} to {new_folder}')
            shutil.copy(file, new_folder)
        print('Finished')
    elif option == 'pdf':
        for file in glob.glob('./tmp/*.pdf'):
            print(f'Copying {file} to {new_folder}')
            shutil.copy(file, new_folder)
        print('Finished')
    elif option == 'json':
        for file in glob.glob('./tmp/*.json'):
            print(f'Copying {file} to {new_folder}')
            shutil.copy(file, new_folder)
        print('Finished')
    else:
        print('Option not valid')


def _create_new_folder(new_folder_name):
    if not os.path.isdir(new_folder_name):
        os.makedirs(new_folder_name)
        return


if __name__ == "__main__":
    main()
