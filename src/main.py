from config import input_x4_save_file
from storages.file_storage import FileStorage
from x4_save_processor.universe import ETUniverse


if __name__ == "__main__":
    ETUniverse(input_x4_save_file).process(FileStorage())
