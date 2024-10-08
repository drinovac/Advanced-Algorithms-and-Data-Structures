person_data = {'Ana': 1995, 'Zoran': 1978, 'Lucija': 2001, 'Anja': 1997}

for key in person_data.keys():
    person_data[key] -= 1

year_age = []
for value in person_data.values():
    year_age.append((value, (2022 - value)))
