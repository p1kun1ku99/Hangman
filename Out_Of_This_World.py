"""
    Project: Out of this world
    Author: Isaac Tannenbaum
    Class: The Coder School
    README: Visit another planet and see how much you weigh on that planet
"""
gravity_factors = {
    "Mercury": 0.4155,
    "Venus": 0.8975,
    "Earth": 1.0,
    "Moon": 0.166,
    "Mars": 0.3507,
    "Jupiter": 2.5374,
    "Saturn": 1.0677,
    "Uranus": 0.8947,
    "Neptune": 1.1794,
    "Pluto": 0.0899,
    "Ceres": 0.016,
    "Eris": 0.08,
    "Haumea": 0.044,
    "Makemake": 0.05}

def multiply():
    weight = float(input("What is your current weight? "))
    planet = input(str("What is your destination planet?  Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Ceres, Eris, Haumea, Makemake: "))
    if planet == "Earth":
        print(f"HEY!!! You're on Earth right now!!! But your weight is {weight * gravity_factors['Earth']}")
    elif planet == "Mercury":
        print(f"You're on Mercury! Your new weight is {weight * gravity_factors['Mercury']}")
    elif planet == "Venus":
        print(f"You're on Venus! Your new weight is {weight * gravity_factors['Venus']}")
    elif planet == "Moon":
        print(f"You're on The Moon! Your new weight is {weight * gravity_factors['Moon']}")
    elif planet == "Mars":
        print(f"You're on Mars! Your new weight is {weight * gravity_factors['Mars']}")
    elif planet == "Jupiter":
        print(f"You're on ..............wait for it............Jupiter! Your new weight is {weight * gravity_factors['Jupiter']}")
    elif planet == "Saturn":
        print(f"You're on Saturn! Your new weight is {weight * gravity_factors['Saturn']}")
    elif planet == "Uranus":
        print(f"You're on Uranus! Your new weight is {weight * gravity_factors['Uranus']}")
    elif planet == "Neptune":
        print(f"You're on Neptune! Your new weight is {weight * gravity_factors['Neptune']}")
    elif planet == "Pluto":
        print(f"You're on Pluto! Your new weight is {weight * gravity_factors['Pluto']}")
    elif planet == "Ceres":
        print(f"You're on Ceres! Your new weight is {weight * gravity_factors['Creres']}")
    elif planet == "Eris":
        print(f"You're on Eris! Your new weight is {weight * gravity_factors['Eris']}")
    elif planet == "Haumea":
        print(f"You're on Haumea! Your new weight is {weight * gravity_factors['Haumea']}")
    elif planet == "Makemake":
        print(f"You're on Makemake! Your new weight is {weight * gravity_factors['Makemake']}")
    else:
        print("Dude, thats not a planet. But I guess it might be, and I just don't know. But I don't beleive you lol.")
multiply()
