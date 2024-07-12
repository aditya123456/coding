from pathlib import Path
from zipfile import ZipFile



class FileManager:
    def __init__(self, fileName):
        self.path = Path(fileName)

    def read(self, encoding='utf-8'):
        return self.path.read_text(encoding)

    def write(self, data, encoding='utf-8'):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix('.zip'), 'w') as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix('.zip'), 'r') as archive:
            archive.extractall(self.path)