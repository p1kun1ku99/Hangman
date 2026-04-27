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
    planet = input(str("What is your destination planet? "))
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

multiply()
