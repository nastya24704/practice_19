class MorseMsg:
    """
    A class representing a message in Morse code.
    """

    morse_to_eng: dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z'
    }

    morse_to_ru: dict = {
        '.-': 'А', '-...': 'Б', '.--': 'В', '--.': 'Г', '-..': 'Д',
        '.': 'Е', '...-': 'Ж', '--..': 'З', '..': 'И', '.---': 'Й',
        '-.-': 'К', '.-..': 'Л', '--': 'М', '-.': 'Н', '---': 'О',
        '.--.': 'П', '.-.': 'Р', '...': 'С', '-': 'Т', '..-': 'У',
        '..-.': 'Ф', '....': 'Х', '-.-.': 'Ц', '---.': 'Ч', '----': 'Ш',
        '--.-': 'Щ', '--.--': 'Ъ', '-.--': 'Ы', '-..-': 'Ь', '.-.-': 'Э',
        '..--': 'Ю', '.-.-.': 'Я'
    }

    vowels_eng: set = set('AEIOUY')
    vowels_ru: set = set('АЕЁИОУЫЭЮЯ')

    def __init__(self, morse_string: str) -> None:
        """
        Initialize a Morse code message.

        Args:
            morse_string: String of dots and dashes, letters separated by spaces.
        """
        self.morse_words: list = morse_string.split()

    def eng_decode(self) -> str:
        """
        Decode the message to English letters.

        Returns:
            Decoded English string.
        """
        result: list = []
        for code in self.morse_words:
            if code in self.morse_to_eng:
                result.append(self.morse_to_eng[code])
        return ''.join(result)

    def ru_decode(self) -> str:
        """
        Decode the message to Russian letters.

        Returns:
            Decoded Russian string.
        """
        result: list = []
        for code in self.morse_words:
            if code in self.morse_to_ru:
                result.append(self.morse_to_ru[code])
        return ''.join(result)

    def get_vowels(self, lang: str) -> list:
        """
        Return vowels from the decoded message in order.

        Args:
            lang: 'ru' or 'eng'

        Returns:
            List of vowels.
        """
        if lang == 'eng':
            text = self.eng_decode()
            vowels = self.vowels_eng
        else:
            text = self.ru_decode()
            vowels = self.vowels_ru
        return [ch for ch in text if ch in vowels]

    def get_consonants(self, lang: str) -> list:
        """
        Return consonants from the decoded message in order.

        Args:
            lang: 'ru' or 'eng'

        Returns:
            List of consonants.
        """
        if lang == 'eng':
            text = self.eng_decode()
            vowels = self.vowels_eng
        else:
            text = self.ru_decode()
            vowels = self.vowels_ru
        return [ch for ch in text if ch not in vowels]

    def __str__(self) -> str:
        """
        Return the decoded message in English (by default).
        """
        return self.eng_decode()


msgs = []
msgs.append(MorseMsg('.. .-.. .. -.- . .--. -.-- - .... --- -.'))
msgs.append(MorseMsg('-- --- .-.- .--. .-. --- --. .-. .- -- -- .-'))
for msg in msgs:
    print(msg)
print(msgs[0].eng_decode())
print(msgs[0].get_vowels('eng'))
print(msgs[0].get_consonants('eng'))
print(msgs[1].ru_decode())
print(msgs[1].get_vowels('ru'))
print(msgs[1].get_consonants('ru'))
