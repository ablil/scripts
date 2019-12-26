#!/usr/bin/env python3

colors = [
    0,
    1,
    2,
    3,
    4,
    5,
    7,
    8,
    9,
    21,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    52,
    90,
    91,
    92,
    93,
    94,
    95,
    96,
    97,
    100,
    101,
    102,
    103,
    104,
    105,
    106,
    107,
]

end = "\33[0m"

for number in colors:
    color = "\33[{}m".format(number)
    print("{} {} Color {}".format(number, color, end))
