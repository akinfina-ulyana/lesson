def __init__(self, hours, minutes, seconds):
    self.hours, self.minutes, self.seconds = hours, minutes, seconds
    self.timestamp = seconds + minutes * 60 + seconds * 60 * 60