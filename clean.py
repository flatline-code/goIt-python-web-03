from threading import Thread
import os
import sys
import zipfile


def sort_files(original_path) -> None:
    all_folders = {
        'images': ['jpeg', 'png', 'jpg', 'svg'],
        'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx'],
        'audio': ['mp3', 'ogg', 'wav', 'amr'],
        'video': ['avi', 'mp4', 'mov', 'mkv'],
        'archives': ['zip'],
    }

    all_files = os.listdir(original_path)

    for file in all_files:
        file_path = os.path.join(original_path, file)

        if os.path.isdir(file_path):
            
            if file in all_folders:
                continue

            if not os.listdir(file_path):
                os.rmdir(file_path)
                continue

            thread = Thread(target=sort_files, args=(file_path,))
            thread.start()

        file_type = file.split('.')[-1]

        def sort(files: str) -> None:
            if file_type in all_folders[files]:
                if not os.path.exists(os.path.join(original_path, files)):
                    os.makedirs(os.path.join(original_path, files))

                new_file_path = os.path.join(os.path.join(original_path, files), file)
                thread = Thread(target=os.replace, args=(file_path, new_file_path))
                thread.start()

                return True

        if sort('images'):
            continue

        if sort('documents'):
            continue

        if sort('audio'):
            continue

        if sort('video'):
            continue

        sort('archives')
            
            
if __name__ == '__main__':
    try:
        original_path = os.path.join(sys.argv[1])
        sort_files(original_path)
    except IndexError:
        print('Enter path to the directory.')
        