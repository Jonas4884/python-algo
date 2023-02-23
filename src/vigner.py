class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.alphabet = {alphabet[i]: i for i in range(len(alphabet))}
        self.key = key

    def __str__(self):
        return f"{self.alphabet}\n{self.key}\n{len(self.alphabet)}"

    def text_to_password(self, text):
        text_to_password = []
        idx = 0
        for value in text:
            if idx == len(self.key):
                idx = 0
            text_to_password.append([self.key[idx], value])
            idx += 1
        return text_to_password

    def encode(self, text):
        text_to_encode = self.text_to_password(text)
        encoded_text = ""
        for i in text_to_encode:
            if not i[1] in self.alphabet.keys():
                encoded_text += i[1]
                continue
            res = self.alphabet[i[0]] + self.alphabet[i[1]]
            temp = res if res < len(
                self.alphabet) else res - len(self.alphabet)
            for j in self.alphabet.keys():
                if self.alphabet[j] == temp:
                    encoded_text += j
                    break

        return encoded_text

    def decode(self, text):
        text_to_decode = self.text_to_password(text)
        decoded_text = ""
        for i in text_to_decode:
            if not i[1] in self.alphabet.keys():
                decoded_text += i[1]
                continue
            res = self.alphabet[i[0]] - self.alphabet[i[1]]
            temp = -1 * res if res <= 0 else len(self.alphabet) - res
            for j in self.alphabet.keys():
                if self.alphabet[j] == temp:
                    decoded_text += j
                    break
        return decoded_text