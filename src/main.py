from x4_save_processor.config import input_x4_save_file
from x4_save_processor.universe import ETUniverse


if __name__ == "__main__":
    ETUniverse(input_x4_save_file).process()
