import power_computation.radiator_power_consumption as rad_pow
import datetime
import system as sys


def main():
    sys_output, temp = sys.system_iterate(datetime.datetime.now(
    ), 24.0, 10.0, 0.5, sys.PowerConsumptionSystemMode.Mode1, 0.0)

    print(sys_output)
    print(temp)


if __name__ == "__main__":
    main()
