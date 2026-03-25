class InvalidAgeError(Exception):
    pass


def validate_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be less than 0.")
    elif age > 120:
        raise InvalidAgeError("Age cannot be greater than 120.")
    else:
        return "Valid age"


try:
    print(validate_age(25))
except InvalidAgeError as e:
    print("Error:", e)

try:
    print(validate_age(-5))
except InvalidAgeError as e:
    print("Error:", e)

try:
    print(validate_age(150))
except InvalidAgeError as e:
    print("Error:", e)