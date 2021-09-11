from src.storages.file_storage import FileStorage
from src.x4_save_processor.universe import ETUniverse


if __name__ == "__main__":
    ETUniverse("D:/X4_reverse/001.xml").process(FileStorage())
