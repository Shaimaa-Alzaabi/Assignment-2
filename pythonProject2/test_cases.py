from artwork import Artwork
from exhibition import Exhibition
from visitor import Visitor
from permanent import Permanent
from ticket import Ticket
from staff import Staff

def main():
    # Test case for adding new artwork
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Famous portrait", "Room 1")
    print(artwork1)

    # Test case for opening a new exhibition
    exhibition1 = Exhibition("Renaissance Art Exhibition", "Gallery A", "2 weeks")
    exhibition1.add_artwork(artwork1)
    print(exhibition1)

    # Test case for purchasing tickets
    ticket1 = Ticket("Adult", 63, 5)
    ticket2 = Ticket("Child", 0, 0)
    visitor1 = Visitor("Ahmed", 25, "KSA", "Adult", ticket1.price)
    visitor2 = Visitor("Ali", 10, "UAE", "Child", ticket2.price)
    print(visitor1)
    print(visitor2)

    # Test case for displaying payment receipts
    print(ticket1)
    print(ticket2)

    # Test case for opening a new permanent gallery
    permanent_gallery = Permanent()
    permanent_gallery.add_artwork(artwork1)
    print(permanent_gallery)

    # Test case for staff information
    staff1 = Staff("Khadija", "Curator", 5000, "2023-01-15")
    print(staff1)

if __name__ == "__main__":
    main()
