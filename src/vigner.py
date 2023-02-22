class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = {alphabet[i]: i for i in range(len(alphabet))}
        self.key = key

    def __str__(self):
        return f"{self.alphabet}\n{self.key}\n{len(self.alphabet)}"

    def password_text(self, text):
        password_text = []
        i = 0
        for value in text:
            if i == len(self.key):
                i = 0
            password_text.append([self.key[i], value])
            i += 1
        return password_text

    def encode(self, text):
        zip_pas_and_text = self.password_text(text)
        encode_text = ""
        for i in zip_pas_and_text:
            if not i[1] in self.alphabet.keys():
                encode_text += i[1]
                continue
            p = self.alphabet[i[0]] + self.alphabet[i[1]]
            temp = p if p < len(
                self.alphabet) else p - len(self.alphabet)
            for j in self.alphabet.keys():
                if self.alphabet[j] == temp:
                    encode_text += j
                    break

        return encode_text

    def decode(self, text):
        zip_pas_and_text = self.password_text(text)
        decode_text = ""
        for i in zip_pas_and_text:
            if not i[1] in self.alphabet.keys():
                decode_text += i[1]
                continue
            p = self.alphabet[i[0]] - self.alphabet[i[1]]
            temp = -1 * p if p <= 0 else len(self.alphabet) - p
            for j in self.alphabet.keys():
                if self.alphabet[j] == temp:
                    decode_text += j
                    break
        return decode_text