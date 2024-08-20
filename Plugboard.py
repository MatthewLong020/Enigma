
class Plugboard:
    """
    Plugboard of the enigma system. Works by swapping signals (letters).
    Example: A becomes Z and Z becomes A.

    Input is provided as a two digit string or a list of 2 digit strings.
    Example: "AB" or ["AB", "CD", "ZP"]
    """

    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.right.find(B)
            self.left = self.left[:pos_A] + A + self.left[pos_A + 1:]
            self.left = self.left[:pos_B] + B + self.left[pos_B + 1:]

    def forward(self, signal):
        letter = self.right[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.right.find(letter)
        return signal
