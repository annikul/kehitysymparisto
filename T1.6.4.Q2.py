def convert_days_to_seconds (days) :
    hours = days * 24
    minutes= hours * 60
    seconds = minutes * 60
    return seconds
print(convert_days_to_seconds(1))