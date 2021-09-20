from bot.count import Count


class BinaryCount(Count):
    channel_name = 'count-binary'

    def convert_to_int(self, number):
        return int(number.replace(' ', ''), 2)

    def get_current(self):
        return f'{self.current:08b}'
