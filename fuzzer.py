import random


class fuzzer:
    def __init__(self, path_to_file, nb_of_mods):
        self.file = open(path_to_file, 'rb')
        self.content = self.file.read()
        self.len = len(self.content)
        self.position = None
        self.byte = None
        self.extension = self.file.split('.')[1]

        self._generator_(nb_of_mods)

    def get_randoms(self):
        position = random.randint(0, self.len)
        byte = bytes([random.randint(1, 255)])
        return (self.position, self.byte)

    def _generator_(self, nb):
        for i in range(nb):
            file = self._create_new_file_(nb)
            position, byte = self.get_randoms()
            old_byte = self.content[position: position + 1]
            new_byte = byte ^ int.from_bytes(old_byte, byteorder='little')
            new_content = self.content[:position] + int.to_bytes(new_byte, byteorder='little') + self.content[(
                position + 1):]
            file.write(new_content)

    def _create_new_file_(self, name):
        new_file = open(name + '.' + self.extension, 'wb')
        return new_file


# EXAMPLE
if __name__ == '__main__':
    fuzzer('image.bmp', 10)
