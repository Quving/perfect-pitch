import os
import random
from enum import Enum
from os import walk

from pydub import AudioSegment
from pydub.playback import play


class Difficulty(Enum):
    EASY = 15
    MEDIUM = 10
    HARD = 5


class Pitcher():

    def __init__(self):
        audiofile_path = 'audiofiles'
        filenames = next(walk(audiofile_path), (None, None, []))[2]
        filenames = list(filter(lambda c: c.endswith('mp3'), filenames))
        filenames.sort()

        self.audiofiles = [os.path.join(audiofile_path, filename) for filename in filenames]

    def get_index_of_tone(self, key):
        for f in self.audiofiles:
            tone = f.split('_')[1].split('.')[0]
            if tone == key:
                return self.audiofiles.index(f)

    def get_similar_tones(self, tone: str, difficulty: Difficulty):
        index = self.get_index_of_tone(tone)
        if not index:
            print("Wrong tone provided. Try again!")
            return

        random_indexes = []
        for i in range(5):
            random_indexes.append(random.randint(index - difficulty.value, index + difficulty.value))

        return [self.audiofiles[random_index] for random_index in random_indexes]


if __name__ == '__main__':
    pitcher = Pitcher()
    tones = pitcher.get_similar_tones('c5', Difficulty.EASY)

    for t in tones:
        song = AudioSegment.from_mp3(t)
        play(song)
