from classes.airtravel import *
from pprint import pprint as pp

def main():


    print("types_example")
    types_example()

    a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
    r = a.registration()
    m = a.model()
    s = a.seating_plan()
    print(r)
    print(m)
    print(s)

    f = Flight("BA758", a)

    print(f.aircraft_model())
    pp(f._seating)

    f.allocate_seat("12A", "Ferdeen Mughal")
    
    try:
        f.allocate_seat("12A", "Faron Mughal")
    except ValueError as exp:
        print(exp)

    f.allocate_seat("12B", "Faron Mughal")
    f.allocate_seat("14A", "Callum Mughal")

    pp(f._seating)

    make_flight_example()


def types_example():
    print(type(5))
    print(type("python"))
    print(type([1,2,3]))
    print(type(x * x for x in [2, 4, 6]))

def make_flight_example():
    from classes.airtravel import make_flight, console_card_printer, make_flights

    # Here have access to the flight class even though we have only imported the function make_flight() and console_card_printer()
    # This is becuase of python's dynamic type system can loosely couples code.

    f = make_flight()
    print(f)

    # Reallocate passenger - Move Guido van Rossum closer to Anders Hejlsberg & Bjarne Stroustrup
    pp(f._seating)
    f.relocate_passenger('12A', '15D')
    pp(f._seating)

    print(f.num_available_seat())

    f.make_boarding_cards(console_card_printer)

    # Polymorphism and Duck Typing
    a, b = make_flights()
    print(a.aircraft_model())
    a.make_boarding_cards(console_card_printer)
    print(b.aircraft_model())
    b.make_boarding_cards(console_card_printer) 

    # Inheritence
    y = AirbusA319("G-EZBT")
    print(y.num_seats())
    z = Boeing777("N717AN")
    print(z.num_seats())

if __name__ == '__main__':
    main()