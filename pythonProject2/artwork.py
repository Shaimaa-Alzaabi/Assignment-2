class Artwork:
    def __init__(self, title, artist, date_of_creation, historical_significance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_significance = historical_significance
        self.location = location

    def __str__(self):
        return f"Artwork: {self.title} by {self.artist}, Created on {self.date_of_creation}"
