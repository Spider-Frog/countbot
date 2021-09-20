from bot.count import Count


class DecimalCount(Count):
    channel_name = 'count-decimal'

    def convert_to_int(self, number):
        return int(number)
