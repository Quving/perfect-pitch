import os
import random
from enum import Enum
from os import walk


class Difficulty(Enum):
    EASY = 10
    MEDIUM = 6
    HARD = 3


class Tone:
    def __init__(self, tone, filename, index):
        self.tone = tone
        self.filename = filename
        self.index = index


class Pitcher():
    def __init__(self):
        audiofiles_path = 'audiofiles'
        filenames = next(walk(audiofiles_path), (None, None, []))[2]
        filenames = list(filter(lambda c: c.endswith('mp3'), filenames))
        filenames.sort()

        self.audio_files = [os.path.join(audiofiles_path, filename) for filename in filenames]

        self.tones = []
        for f in self.audio_files:
            tone = f.split('_')[1].split('.')[0]
            self.tones.append(Tone(
                tone=tone,
                filename=f,
                index=self.audio_files.index(f))
            )

    def get_index_of_tone(self, tone):
        for t in self.tones:
            if tone == t.tone:
                return t.index

    def get_similar_tones(self, tone: str, difficulty: Difficulty):
        index = self.get_index_of_tone(tone)
        if not index:
            print("Wrong tone provided. Try again!")
            exit(code=1)

        random_indexes = []
        for i in range(5):
            random_indexes.append(random.randint(index - difficulty.value, index + difficulty.value))

        return [self.tones[random_index] for random_index in random_indexes]
