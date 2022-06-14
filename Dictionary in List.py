travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
new_el = {}


def add_new_country(country, vis_num, cities):
    travel_log.append(new_el)
    new_el["country"] = country
    new_el["visits"] = vis_num
    new_el["cities"] = cities


add_new_country(country="Russia", vis_num=2, cities=["Moscow", "Saint Petersburg"])
print(travel_log)
# print(new_el)
