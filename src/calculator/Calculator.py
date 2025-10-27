
class Calculator:
    _instance = None
    numbers_map = {
        # English words
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10,

        # German words
        "null": 0, "eins": 1, "zwei": 2, "drei": 3, "vier": 4,
        "fünf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
        "zehn": 10,

        # Spanish words
        "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
        "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
        "diez": 10,

        # Russian words (transliterated)
        "nol": 0, "odin": 1, "dva": 2, "tri": 3, "chetyre": 4,
        "pyat": 5, "shest": 6, "sem": 7, "vosem": 8, "devyat": 9,
        "desyat": 10,

        # Russian words (Cyrillic)
        "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4,
        "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
        "десять": 10,

        # Chinese (Simplified)
        "零": 0, "一": 1, "二": 2, "三": 3, "四": 4,
        "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
        "十": 10,

        # Roman numerals
        "i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5,
        "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10,

        # Numeric strings
        "0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
        "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10
    }


    def getNumber(self, s):
        if isinstance(s, (int, float)):
            return s

        if not isinstance(s, str):
            raise ValueError(f"Unsupported type for number conversion: {type(s)}")

        s = s.strip()

        try:
            return int(s)
        except ValueError:
            pass

        try:
            return float(s)
        except ValueError:
            pass

        val = self.numbers_map.get(s.lower())
        if val is not None:
            return val
        raise ValueError(f"Cannot interpret {s!r} as a number")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, a, b):
        return self.getNumber(a) + self.getNumber(b)

    def sub(self, a, b):
        return self.getNumber(a) - self.getNumber(b)

    def mul(self, a, b):
        return self.getNumber(a) * self.getNumber(b)

    def div(self, a, b):
        if self.getNumber(b) == 0:
            raise ValueError("Cannot divide by zero.")
        return self.getNumber(a) / self.getNumber(b)
    
    def factorize(self,n):
        n = self.getNumber(n)
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors