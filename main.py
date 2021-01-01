import argparse
import os
import string


class EncodeDecode:

    def __init__(self):
        alphabet = string.printable + string.whitespace
        self.encodeDict = dict()
        self.decodeDict = dict()
        for i, character in enumerate(alphabet):
            self.encodeDict[character] = i
            self.decodeDict[str(i)] = character


    def run(self):
        running = True

        while running:

            task = (input("Would you like to [E]ncode or [D]ecode a message or a [F]ile or [X] to exit? ").upper())[0]
            if task == 'E':
                message = input("Enter the message to encode: \n")
                encoded_message = ""
                for character in message:
                    value = self.encodeDict[character]
                    encoded_message += f"{value} "

                print(encoded_message)

            elif task == 'D':
                message = input("Enter the message to decode: \n").split(" ")
                decoded_message = ""

                for character in message:
                    if character != "":
                        value = self.decodeDict[character]
                        decoded_message += str(value)

                print(decoded_message)

            elif task == 'F':
                file_name = input("Enter the name of the file: ")
                task = input("Do you want to encode or decode?")
                if task == 'E':
                    self.encode_file(file_name)
                if task == 'D':
                    self.decode_file(file_name)

            elif task == 'X':
                running = False

            else:
                print("That is not a valid option")

    def decode_file(self, file_name):
        tmp_file_name = "temporary_file"
        with open(tmp_file_name, "w") as tmp_file:
            with open(file_name, "r") as file:
                for line in file.readlines():
                    characters = line.split(" ")
                    for character in characters:
                        if character.isnumeric():
                            value = self.decodeDict[character]
                            tmp_file.write(f"{value}")
        os.remove(file_name)
        os.rename(tmp_file_name, file_name)
        print(f"Finished decoding file {file_name}")

    def encode_file(self, file_name):
        tmp_file_name = "temporary_file"
        with open(tmp_file_name, "w") as tmp_file:
            with open(file_name, "r") as file:
                for line in file.readlines():
                    for character in line:
                        value = self.encodeDict[character]
                        tmp_file.write(f"{value} ")
                    tmp_file.write("\n")
        os.remove(file_name)
        os.rename(tmp_file_name, file_name)
        print(f"Finished encoding file {file_name}")


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=False, help="file name")
    ap.add_argument("-d", "--decode", dest='decode', action='store_true')
    ap.add_argument("-e", "--encode", dest='decode', action='store_false')
    ap.set_defaults(decode=True)
    args = vars(ap.parse_args())
    encodeDecode = EncodeDecode()
    file_name = args['file']
    if file_name:
        if args['decode']:
            encodeDecode.decode_file(file_name)
        else:
            encodeDecode.encode_file(file_name)
    else:
        EncodeDecode().run()
