# Name
# CIS 3330
# CODE 1 - Weather Assistant
# Conversion formula: (Temperature in °F - 32) * .5556
# Note that the message to user should be the following
# "What is the temperature outside: "

def main():
    temperature = float(input("What is the temperature outside: "))
    
    celsius = (temperature - 32) * .5556

    if celsius > 20:
        print("\nWear a hat")
    elif celsius > 10:
        print("\nWear a light jacket")
    else:
        print("\nWear a heavy jacket")


if __name__ == "__main__":
    main()
