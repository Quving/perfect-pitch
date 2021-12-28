from pydub import AudioSegment
from pydub.playback import play

from pitcher import Pitcher, Difficulty

if __name__ == '__main__':
    pitcher = Pitcher()
    tones = pitcher.get_similar_tones('c5', Difficulty.EASY)

    for t in tones:
        song = AudioSegment.from_mp3(t)
        play(song)
