import time
from pprint import pprint

import vlc

from pitcher import Pitcher, Difficulty, Tone


class TrainingSessions:
    def __init__(self):
        self.pitcher = Pitcher()
        self.session = {}

    def request_tone(self) -> Tone:
        while True:
            x = input("[INPUT] What tone do you want to try to identify? (e.g. 'c6'):\n -> ")
            if x in [tone.tone for tone in self.pitcher.tones]:
                for tone in self.pitcher.tones:
                    if tone.tone == x:
                        return tone

            print("Your request was not valid. Please try again!")

    def request_feedback(self):
        available_feedback = ["1", "2", "3", "4"]
        while True:
            feedback = input("[INPUT] What do you think?\n"
                             "1 = too low, 2 = correct, 3 = too high, 4 = play again:\n -> ")
            if feedback in available_feedback:
                return feedback

            print("Your feedback was not valid. Please try again!")

    def start(self):
        tone_to_test = self.request_tone()
        similar_tones = self.pitcher.get_similar_tones(tone=tone_to_test.tone, difficulty=Difficulty.MEDIUM)

        self.session[tone_to_test.tone] = {}
        for tone in similar_tones:
            print("< Tone will be played >")
            time.sleep(1)
            player = vlc.MediaPlayer(tone.filename)
            player.play()

            feedback = self.request_feedback()

            if feedback == "4":
                time.sleep(1)
                player = vlc.MediaPlayer(tone.filename)
                player.play()
                feedback = self.request_feedback()

            difference = tone.index - tone_to_test.index
            result = 'false'

            if feedback == "1" and difference < 0:
                result = 'true'
            elif feedback == "2" and difference == 0:
                result = 'true'
            elif feedback == "3" and difference > 0:
                result = 'true'

            feedback_dict = {
                "1": "too low",
                "2": "correct",
                "3": "too high"
            }
            result = {
                'result': result,
                'feedback': feedback_dict[str(feedback)],
                'difference': difference
            }

            self.session[tone_to_test.tone][tone.tone] = result
        print("Session finished!")

        pprint(self.session)


if __name__ == '__main__':
    ts = TrainingSessions()
    ts.start()
