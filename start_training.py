from pprint import pprint

import vlc

from pitcher import Pitcher, Difficulty


class TrainingSessions:
    def __init__(self):
        self.pitcher = Pitcher()
        self.session = {}

    def request_tone(self):
        while True:
            x = input("[INPUT] What tone do you want to try to identify? (e.g. 'c6'):\n -> ")
            if x in self.pitcher.order:
                return x

            print("Your request was not valid. Please try again!")

    def request_feedback(self):
        available_feedback = ['h', 'l', 'c', 'a']
        while True:
            feedback = input("[INPUT] What do you think?\n"
                             "h = too high, l = too low, c = correct, a = play again:\n -> ")
            if feedback in available_feedback:
                return feedback

            print("Your feedback was not valid. Please try again!")

    def start(self):
        tone_to_test = self.request_tone()
        similar_tones = self.pitcher.get_similar_tones(tone=tone_to_test, difficulty=Difficulty.MEDIUM)

        self.session[tone_to_test] = {}
        for s in similar_tones:
            print("Test", s)
            player = vlc.MediaPlayer(s)
            player.play()

            feedback = self.request_feedback()
            if feedback == 'a':
                player.play()
                feedback = self.request_feedback()
            self.session[tone_to_test][s] = feedback
        print("Session finished!")

        pprint(self.session)


if __name__ == '__main__':
    ts = TrainingSessions()
    ts.start()
