from x4_save_parser.config import input_x4_save_file
from x4_save_parser.universe import ETUniverse


if __name__ == "__main__":
    ETUniverse(input_x4_save_file).parse()
