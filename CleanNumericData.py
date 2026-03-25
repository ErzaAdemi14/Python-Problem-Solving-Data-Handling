def clean_numeric_data(values):
    cleaned_values = []

    for value in values:
        try:
            number = int(value)
            cleaned_values.append(number)
        except ValueError:
            continue

    return cleaned_values


values = ["5", "10", "x", "15", "NaN", "20"]

result = clean_numeric_data(values)
print(result)