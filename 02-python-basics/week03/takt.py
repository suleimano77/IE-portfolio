# Takt time calculator: how often one unit must be finished to keep up with orders.

def main():
    input_minutes = float(input("Enter the available working time in minutes: "))
    input_units = int(input("Enter the number of units ordered: "))

    takt_time = input_minutes / input_units
    print(f"Takt time: {round(takt_time, 2)} minutes per unit")

main()
