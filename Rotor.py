
# TODO: add rotors VI, VII, VIII since they have two notches
# TODO: add rotation of rotors (notch)

class Rotor:

    def __init__(self, rotor, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = rotor
        self.notch = notch

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
