class Card:

    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def getValue(self, hand_value):
        value = self.value
        if value == "J" or value == "Q" or value == "K":
            return 10
        if value == "A":
            if hand_value + 11 > 21:
                return 1
            else:
                return 11

        return value

    def __str__(self):
        value = self.value
        suite = self.suite

        middle_spaces = "    " if value == 10 else "      "

        card =  "*----------*"+"\n"+ \
                f"| {value}"+ middle_spaces + f"{value} |"+"\n"+ \
                f"| {suite}      {suite} |"+"\n"+ \
                "|          |"+"\n"+ \
                "|          |"+"\n"+ \
                f"| {suite}      {suite} |"+"\n"+ \
                f"| {value}"+ middle_spaces + f"{value} |"+"\n"+ \
                "*----------*"+"\n"

        return card