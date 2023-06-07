import sys
import glob
import os
import shutil

SOURCE_PATH = './tmp/'


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
        all_files_path = SOURCE_PATH + '*'
        _copy_files(all_files_path, new_folder)
    else:
        specific_files_path = SOURCE_PATH + f'*.{option}'
        _copy_files(specific_files_path, new_folder)


def _create_new_folder(new_folder_name):
    if not os.path.isdir(new_folder_name):
        os.makedirs(new_folder_name)
        return


def _copy_files(source_dir, destination_dir):
    for file in glob.glob(source_dir):
        print(f"Copying {file} to {destination_dir}")
        shutil.copy(file, destination_dir)

    print('Finished')


if __name__ == "__main__":
    main()
