import copy
days = [0, 1, 2, 3, 4, 5, 6]
months = {1:31,
          2:28,
          3:31,
          4:30,
          5:31,
          6:30,
          7:31,
          8:31,
          9:30,
          10:31,
          11:30,
          12:31}

leap = copy.copy(months)
leap[2] = 29
years = [yr for yr in range(1901, 2001)]
day = 0
sundays = 0
for month in months:
    day = (day + months[month]) % 7

for yr in years:
    if yr % 4 == 0:
        for month in leap:
            if day == 6:
                sundays += 1
            day = (day + leap[month]) % 7
    else:
        for month in months:
            if day == 6:
                sundays += 1
            day = (day + months[month]) % 7
print sundays