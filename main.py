import sys
import glob
import os
import shutil

SOURCE_PATH = './tmp/'


def main():
    _validate_args(sys.argv)

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

    print('Process of copy files has finished.')


def _validate_args(args):
    if len(args) == 1:
        print('You have to select a option')
        raise SystemExit
    if len(args) == 2:
        print('Insert the name of the new folder')
        raise SystemExit


if __name__ == "__main__":
    main()
