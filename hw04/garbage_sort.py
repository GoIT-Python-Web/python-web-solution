import os
import pathlib
from threading import Thread


extensions = []
main_path = pathlib.Path.cwd()
threads = []


def create_folder(folder):
    if not isinstance(folder, pathlib.Path):
        folder_path = pathlib.Path(folder)
    else:
        folder_path = folder
    if not folder_path.exists():
        pathlib.Path.mkdir(folder_path)


def replace_file(file_path, new_path):
    if file_path.exists():
        file_path.replace(new_path)


def delete_empty_directories(main_directory_path):
    if not isinstance(main_directory_path, pathlib.Path):
        pathlib_directory_path = pathlib.Path(main_directory_path)
    else:
        pathlib_directory_path = main_directory_path
    for element in pathlib_directory_path.iterdir():
        if element.is_dir():
            delete_empty_directories(element)
            if not os.listdir(element):
                os.rmdir(element)


def clear_directory(directory_path):
    if not isinstance(directory_path, pathlib.Path):
        pathlib_directory_path = pathlib.Path(directory_path)
    else:
        pathlib_directory_path = directory_path
    for element in pathlib_directory_path.iterdir():
        if element.is_dir():
            thread_directory = Thread(target=clear_directory, args=(element,))
            threads.append(thread_directory)
            thread_directory.start()
        elif element.is_file():
            suffix = element.suffix
            suffix_folder_path = main_path.joinpath(suffix)
            if suffix not in extensions:
                extensions.append(suffix)
                create_folder(suffix_folder_path)

            thread_replace = Thread(target=replace_file, args=(element,suffix_folder_path.joinpath(element.name),))
            threads.append(thread_replace)
            thread_replace.start()


if __name__ == '__main__':
    main_path = pathlib.Path('D:/Garbage')
    clear_directory(main_path)
    for thread in threads:
        thread.join()
    print('Garbage is sorted')
    delete_empty_directories(main_path)
    print('Empty directories are removed')
