class Permanent:
    def __init__(self):
        self.artworks = []

    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    def __str__(self):
        return "Permanent Gallery"
