from Rotor import Rotor
from Reflector import Reflector
import Keyboard
from Plugboard import Plugboard

# TODO : plugboard doesn't seem to work

# rotor and notch information found on https://en.wikipedia.org/wiki/Enigma_rotor_details
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")

A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

plugboard = Plugboard(["AR", "GK", "OX"])


def processSignal(original, rotors, plugs, reflector):
    """
    parameters
    __________
    original : input message string

    rotors : list of up to 5 rotors in order of placement

    plugs : Plugboard object indicating which letters are swapped

    reflector : Reflector object indicating which reflector is present
    """
    output = ""
    for letter in original:
        if letter == " ":
            output += " "
        else:
            x = Keyboard.forward(letter)
            x = plugs.forward(x)
            for rotor in rotors:
                x = rotor.forward(x)
            x = reflector.reflect(x)
            for rotor in reversed(rotors):
                x = rotor.backward(x)
            x = plugs.backward(x)
            x = Keyboard.backward(x)
            output += x
    return output


def main():
    # message = input("Enter your message: ")
    # rotors = input("Enter which rotors you want to use: ")
    # plugs = input("Enter which plugs you want to use: ")
    # reflector = input("Enter which reflector you want to use: ")

    # output = processSignal(message, rotors, plugs, reflector)
    output = processSignal("ABCD", [I, II, III], Plugboard(["AB", "XZ"]), A)
    print("The processed message is: " + output)

    output = processSignal("OHEL", [I, II, III], Plugboard(["AB", "XZ"]), A)
    print("The processed message is: " + output)

    output = processSignal("ABCD", [I, III, II], Plugboard(["AB", "XZ"]), A)
    print("The processed message is: " + output)