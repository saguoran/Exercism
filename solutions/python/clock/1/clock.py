class Clock(object):

    def __init__(self, hour, minute):
        # def create instance
        modified_minute = minute % 60
        modified_hour = (hour + minute // 60) % 24
        self.minute = modified_minute
        self.hour = modified_hour

    def __repr__(self):
        return f'{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}'

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        new_minute = self.minute + minutes
        self.minute = new_minute % 60
        self.hour = (self.hour + new_minute // 60) % 24
        return self

    def __sub__(self, minutes):
        new_minute = self.minute - minutes
        self.minute = new_minute % 60
        self.hour = (self.hour - abs(new_minute // 60)) % 24
        return self
