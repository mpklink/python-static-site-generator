from typing import List
from pathlib import Path

class Parser:
    extensions = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path, source, dest):
        raise NotImplementedError()