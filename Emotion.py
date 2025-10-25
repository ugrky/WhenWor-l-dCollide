import numpy as np

class Emotion:
    def __init__(self):
        self.angry = np.array([2, 3, 4, 5])
        self.fear = np.array([2, 3, 4, 5])
        self.happy = np.array([2, 3, 4, 5])
        self.sad = np.array([2, 3, 4, 5])
        self.surprise = np.array([2, 3, 4, 5])
        self.neutral = np.array([2, 3, 4, 5])
    
    def reassignEmotion(self, emo_type, new_value):
        if emo_type == "angry":
            self.angry = new_value
        elif emo_type == "fear":
            self.fear = new_value
        elif emo_type == "happy":
            self.happy = new_value
        elif emo_type == "sad":
            self.sad = new_value
        elif emo_type == "surprise":
            self.surprise = new_value
        elif emo_type == "neutral":
            self.neutral = new_value

    def reassignAll(self, angry, fear, happy, sad, surprise, neutral):
        self.angry = angry
        self.fear = fear
        self.happy = happy
        self.sad = sad
        self.surprise = surprise
        self.neutral = neutral

    def returnEmotionValue(self, emo_type):
        if emo_type == "angry":
            return self.angry
        elif emo_type == "fear":
            return self.fear
        elif emo_type == "happy":
            return self.happy
        elif emo_type == "sad":
            return self.sad
        elif emo_type == "surprise":
            return self.surprise
        elif emo_type == "neutral":
            return self.neutral

    def returnAll(self):
        return [self.angry, self.fear, self.happy, self.sad, self.surprise, self.neutral]

# Create the emotions object to store the values:
emotions = Emotion()