from abc import ABC, abstractmethod
class FlightBooker():
    def book(self, city: str):
        print(f"Voo reservado com sucesso para {city}")
    
class HotelBooker():
    def book(self, city: str):
        print(f"hotel reservado com sucesso para {city}")

class TourGuideService():
    def book(self, city: str):
        print(f"Passeio reservado com sucesso para {city}")

class ITravelFacede(ABC):
    @abstractmethod
    def book_trip(self, city: str):
        pass

class TravelFacede(ITravelFacede):
    def __init__(self, flight: FlightBooker, hotel: HotelBooker, tour: TourGuideService):
        self.flight = flight
        self.hotel = hotel
        self.tour = tour

    
    def book_trip(self, city: str):
        self.flight.book(city)
        self.hotel.book(city)
        self.tour.book(city)
        
if __name__ == "__main__":
    travel_booker = TravelFacede(FlightBooker(), HotelBooker(), TourGuideService())
    travel_booker.book_trip("Paris")

