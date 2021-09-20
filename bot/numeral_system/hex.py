from bot.count import Count


class HexCount(Count):
    channel_name = 'count-hex'

    def convert_to_int(self, number):
        return int(number.replace(' ', ''), 16)

    def get_current(self):
        return f'{self.current:X}'
