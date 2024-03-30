class Exhibition:
    def __init__(self, title, location, duration):
        self.title = title
        self.location = location
        self.duration = duration
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def __str__(self):
        return f"Exhibition: {self.title}, Location: {self.location}, Duration: {self.duration}"
