import re

f = open("pg11.txt")
alice_line = f.readlines()
alice_line = [l.rstrip() for l in alice_line]
f.close()

for line in alice_line:
    # if re.search("[A-Za-z]{7}", line): print(line)
    # if re.search("[^aeiouAEIOU0-9\.\?]{4}", line): print(line)
    if re.search(r"\bsing.*", line): print(line)
    if re.search("\-*\.*\d+\.*\d*", line): print(line)
