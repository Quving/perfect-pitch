from enum import Enum
from os import walk

file_path = 'audiofiles'
filenames = next(walk(file_path), (None, None, []))[2]
filenames = list(filter(lambda c: c.endswith('mp3'), filenames))

filenames.sort()


class Difficulty(Enum):
    EASY = 15
    MEDIUM = 10
    HARD = 5


for index in range(len(filenames)):
    print(index + 1, filenames[index])
