import os

from interfaces.i_logger import ILogger


class FileLogger(ILogger):
    def __init__(self, file_path='output/pv_output.csv'):
        self.file_path = file_path

    def log(self, data: dict):
        with open(self.file_path, 'a') as f:
            f.write(f"{', '.join([str(v) for v in data.values()])}{os.linesep}")
