alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def forward(letter):
    signal = alphabet.find(letter)
    return signal


def backward(sig):
    letter = alphabet[sig]
    return letter
