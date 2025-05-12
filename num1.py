import random
import string
from pathlib import Path


def generate_random_filename(name_length=8):
    allowed_chars = string.ascii_letters + string.digits
    return ''.join(random.choice(allowed_chars) for _ in range(name_length)) + '.txt'


def create_random_files(output_dir, files_count=10):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)  # Создаем директорию если её нет

    generated_files = []
    for _ in range(files_count):
        new_filename = generate_random_filename()
        full_file_path = output_path / new_filename
        full_file_path.touch()  # Создаем пустой файл
        generated_files.append(full_file_path)

    return generated_files


# Путь где нужно создать файл
output_directory = "random_files"

# Создание файла и получение путей
created_files_list = create_random_files(output_directory)

# Вывод путей
for file_path in created_files_list:
    print(file_path.absolute())