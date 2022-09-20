from pathlib import Path
from pprint import pprint
import sys
import shutil

audio = [".mp3", ".aac", ".ac3", ".wav", ".amr", ".ogg"]

video = [".mp4", ".mov", ".avi", ".mkv"]

image = [".jpg", ".jpeg", ".png", ".svg", ".gif"]

doc = [".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".pptx"]

book = [".fb2", ".epub", ".mobi"]

archive = [".zip", ".rar", ".tar", ".gz"]

all_files = {
    'Audio': [],
    'Video': [],
    'Images': [],
    'Documents': [],
    'Archives': [],
    'Books': [],
    'Other': []
}

known_types = set()

unknown_types = set()


def main():
    path = get_path()

    sort_files(path)

    delete_empty(path)

    print(f'Script sorted next file types: {known_types}')
    print(
        f'Extensions: {unknown_types} are unknown')
    pprint(f'All sorted files in {path}: \n {all_files}', indent=4)


def get_path():

    if len(sys.argv) < 2:
        path = Path('.')

    else:
        path = Path(sys.argv[1])

    if path.exists():
        if path.is_dir():
            return path
        else:
            print(f'Path {path.absolute()} is not a directory')

    else:
        print(f'Path {path.absolute()} is not exist')


def normalize(file_name):

    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = t
        TRANS[ord(c.upper())] = t.upper()

    for sign in "!#$%&' \(\)\+,-;=@[]^`\{\}~.№":
        file_name = file_name.replace(sign, "_")

    new_file_name = file_name.translate(TRANS)

    return new_file_name


def sort_files(path):

    if path.is_dir():
        if path.name in ['Music', 'Video', 'Images', 'Documents', 'Archive', 'Books']:
            for element in path.iterdir():
                sort_files(element)

        else:
            try:
                new_name = path.parent.joinpath(normalize(path.name))
                path.rename(new_name)
                for element in new_name.iterdir():
                    sort_files(element)

            except PermissionError:
                for element in path.iterdir():
                    sort_files(element)

# if path is file:
    else:

        if is_audio(path):

            audio_path = get_path().joinpath("Audio")
            audio_path.mkdir(exist_ok=True)

            new_name = audio_path.joinpath(normalize(path.stem) + path.suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = audio_path.joinpath(
                    normalize(path.stem) + '(1)' + path.suffix)
                path.rename(new_name)

            all_files['Audio'].append(new_name.name)
            known_types.add(new_name.suffix)

        elif is_image(path):

            images_path = get_path().joinpath("Images")
            images_path.mkdir(exist_ok=True)

            new_name = images_path.joinpath(normalize(path.stem) + path.suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = images_path.joinpath(
                    normalize(path.stem) + '(1)' + path.suffix)
                path.rename(new_name)

            all_files['Images'].append(new_name.name)
            known_types.add(new_name.suffix)

        elif is_video(path):

            video_path = get_path().joinpath("Video")
            video_path.mkdir(exist_ok=True)

            new_name = video_path.joinpath(normalize(path.stem) + path.suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = video_path.joinpath(
                    normalize(path.stem) + '(1)' + path.suffix)
                path.rename(new_name)

            all_files['Video'].append(new_name.name)
            known_types.add(new_name.suffix)

        elif is_doc(path):

            doc_path = get_path().joinpath("Documents")
            doc_path.mkdir(exist_ok=True)

            new_name = doc_path.joinpath(normalize(path.stem) + path.suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = doc_path.joinpath(
                    normalize(path.stem) + '(1)' + path.suffix)
                path.rename(new_name)

            all_files['Documents'].append(new_name.name)
            known_types.add(new_name.suffix)

        elif is_book(path):

            book_path = get_path().joinpath("Books")
            book_path.mkdir(exist_ok=True)

            new_name = book_path.joinpath(normalize(path.stem) + path.suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = doc_path.joinpath(
                    normalize(path.stem) + '(1)' + path.suffix)
                path.rename(new_name)

            all_files['Books'].append(new_name.name)
            known_types.add(new_name.suffix)

        elif is_archive(path):

            archive_path = get_path().joinpath("Archives")
            archive_path.mkdir(exist_ok=True)

            try:
                new_name = archive_path.joinpath(
                    normalize(path.stem) + path.suffix)
                path.rename(new_name)

            except FileExistsError:
                new_name = archive_path.joinpath(
                    normalize(path.stem) + '(1)' + path.suffix)
                path.rename(new_name)

            all_files['Archives'].append(new_name.name)
            known_types.add(new_name.suffix)

            shutil.unpack_archive(
                new_name, archive_path.joinpath(new_name.stem))

        else:
            new_name = path.parent.joinpath(normalize(path.stem) + path.suffix)

            try:
                path.rename(new_name)

            except FileExistsError:
                new_name = path.parent.joinpath(
                    normalize(path.stem) + '(1)' + path.suffix)
                path.rename(new_name)

            all_files['Other'].append(new_name.name)
            unknown_types.add(path.suffix)


def delete_empty(path):
    if path.is_dir():
        for element in path.iterdir():
            if element.is_dir():
                delete_empty(element)
                try:
                    element.rmdir()
                except OSError:
                    pass


def is_audio(file_path):
    return (file_path.suffix).lower() in audio


def is_image(file_path):
    return (file_path.suffix).lower() in image


def is_video(file_path):
    return (file_path.suffix).lower() in video


def is_doc(file_path):
    return (file_path.suffix).lower() in doc


def is_book(file_path):
    return (file_path.suffix).lower() in book


def is_archive(file_path):
    return (file_path.suffix).lower() in archive


if __name__ == "__main__":
    main()
