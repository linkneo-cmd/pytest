import re
def get_formatted_city(city, country, population = ''):
    full_name = f"{city}, {country}"
    if population:
        full_name = f"{full_name.title()} - population {(re.search(r'population=(\d+)', population)).group(1)}"
    else:
        full_name = full_name.title()
    return full_name