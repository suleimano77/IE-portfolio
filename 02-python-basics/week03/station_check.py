# Station check: compares a station's cycle time to takt time and says
# whether the station can keep up with orders.


def main():
    takt = float(input("Takt time (minutes per unit): "))
    cycle = float(input("Station cycle time (minutes per unit): "))
    print(status(cycle, takt))


def status(cycle, takt):
  
    if cycle > takt:
        return "Bottleneck: this station can't keep up"
    elif cycle >= 0.9 * takt:
        return "Tight: under 10% spare time"
    else:
        return "OK: room to spare"


main()
