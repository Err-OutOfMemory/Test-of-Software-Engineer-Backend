def AlienConvert(s: str):
    alien_num ={    "A": 1, "B": 5, "Z": 10, "L": 50,
                    "C": 100, "D": 500, "R": 1000
                }
    total = 0

    s = s.replace("AB", "AAAA").replace("AZ", "BAAAA")
    s = s.replace("ZL", "ZZZZ").replace("ZC", "LZZZZ")
    s = s.replace("CD", "CCCC").replace("CR", "DCCCC")

    for x in s:
        total += alien_num[x]

    return total

print(AlienConvert("AAA"))
print(AlienConvert("LBAAA"))
print(AlienConvert("RCRZCAB"))