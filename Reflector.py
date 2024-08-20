class Reflector:

    def __init__(self, rotor):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = rotor

    def reflect(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal
