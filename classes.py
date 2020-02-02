from pprint import pprint as pp

def main():
    from classes.airtravel import Flight, Aircraft

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
    from classes.airtravel import make_flight

    # Here have access to the flight class even though we have only imported the function make_flight()
    # This is becuase of python's dynamic type system can loosely couples code.

    f = make_flight()
    print(f)

    # Reallocate passenger - Move Guido van Rossum closer to Anders Hejlsberg & Bjarne Stroustrup
    pp(f._seating)
    f.relocate_passenger('12A', '15D')
    pp(f._seating)

    print(f.num_available_seat())

if __name__ == '__main__':
    main()