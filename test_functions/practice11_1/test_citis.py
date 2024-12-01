from city_functions import get_formatted_city

def test_city_country():
    formatted_name = get_formatted_city('santiago', 'chile')
    assert formatted_name == 'Santiago, Chile'