import os
import random

VinDigitPositionMultiplier = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
VinDigitValues = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'J': 1,
                  'K': 2, 'L': 3, 'M': 4, 'N': 5, 'P': 7, 'R': 9, 'S': 2, 'T': 3, 'U': 4, 'V': 5,
                  'W': 6, 'X': 7, 'Y': 8, 'Z': 9, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                  '7': 7, '8': 8, '9': 9, '0': 0}


class VinYear:
    def __init__(self, first8, year):
        self.first8 = first8
        self.year = year

    def __repr__(self):
        return "First8: %s - Year: %s" % (self.first8, self.year)


def get_random_vin():
    vin_year = get_random_vin_start()
    char = get_random_vin_char()

    v = "%s%s%s" % (vin_year.first8, char, vin_year.year)
    for i in range(7):
        v += get_random_vin_char()

    check_char = get_check_sum_char(v)
    v = "%s%s%s" % (v[0:8], check_char, v[9:])
    return v


def get_check_sum_char(vin):
    # generate the check sum
    check_sum_total = 0

    if (len(vin) < 17):
        print("Invalid Length: %s" % len(vin))
        return -1

    for i in range(len(vin)):
        if (VinDigitValues.get(vin[i], "-1") != "-1"):
            check_sum_total += int(VinDigitValues[vin[i]]) * VinDigitPositionMultiplier[i]
        else:
            # Characters not in the VinDigitValues list are not valid VIN characters - return false (invalid)
            print("Illegal Character: %s" % vin[i])
            return -1

    remain = check_sum_total % 11
    if remain == 10:
        remain = 'X'

    return remain


def get_random_vin_char():
    i = int(random.random() * len(VinDigitValues))
    return list(VinDigitValues.keys())[i]


def get_random_vin_start():
    # 137DA903       T
    # 137FA833       3
    vin_file = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "VinPrefixes.txt"))
    count = 0

    # Get random Manufaturer and Model
    line_to_read = int(random.random() * 62178)

    try:
        while (count <= line_to_read):
            line = vin_file.readline()
            count += 1
    finally:
        vin_file.close()

    fields = line.split()
    return VinYear(fields[0].strip(), fields[1].strip())
