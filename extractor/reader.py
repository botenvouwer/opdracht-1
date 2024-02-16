from abc import abstractmethod, ABC
import re
from pathlib import Path


class Reader(ABC):

    def __init__(self, file_path):
        self.file_path = Path(file_path)
        self.__name = None

    def get_name(self):
        if self.__name is None:
            name = self.file_path.stem
            self.set_name(name)

        return self.__name

    def set_name(self, name: str):
        sanitized_name = re.sub(r'[^a-zA-Z0-9_]', '_', name)
        sanitized_name = re.sub(r'^\d+', '', sanitized_name)
        # Ensure the name is not empty after sanitization
        if sanitized_name:
            self.__name = sanitized_name.lower()

        else:
            raise ValueError("Name cannot be empty after sanitization")

    @abstractmethod
    def get_header_info(self):
        pass

    @abstractmethod
    def get_header_names(self):
        pass
    
    @abstractmethod
    def __iter__(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass

    # TODO fixed: voeg alle abstracte methoden toe
