"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    return record[1]
    
def convert_coordinate(coordinate):
    coordinate_formatted = ()
    for char in coordinate:
        coordinate_formatted += tuple(char)
    return coordinate_formatted


def compare_records(azara_record, rui_record):
    azara_formatted = ()
    for char in azara_record[1]:
        azara_formatted += tuple(char)
    if azara_formatted == rui_record[1]:
        return True
    return False

def create_record(azara_record, rui_record):
    azara_formatted = ()
    for char in azara_record[1]:
        azara_formatted += tuple(char)
    if azara_formatted == rui_record[1]:
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group):
    cleaned_up = []
    for item in combined_record_group:
        clean = (item[0], item[2], item[3], item[4])
        cleaned_up.append(str(clean))
    return "\n".join(cleaned_up) + "\n"
    