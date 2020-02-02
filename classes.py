from classes.airtravel import *

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

def types_example():
    print(type(5))
    print(type("python"))
    print(type([1,2,3]))
    print(type(x * x for x in [2, 4, 6]))

if __name__ == '__main__':
    main()