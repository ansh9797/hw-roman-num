class RomanConverter:
    def __init__(self):
        self.num_map = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }

    def int_to_roman(self, number):
        roman_value = ''
        for value in sorted(self.num_map.keys(), reverse=True):
            while number >= value:
                roman_value += self.num_map[value]
                number -= value
        return roman_value

if __name__ == "__main__":
    user_input = int(input("Enter an integer: "))
    converter = RomanConverter()
    print("Roman numeral:", {converter.int_to_roman(user_input)})
