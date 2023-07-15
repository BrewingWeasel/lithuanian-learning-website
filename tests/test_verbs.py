from verb_endings import get_endings, PREFIXES

total = 0

with open("data/all_verbs", "r") as f:
    for i in f.read().splitlines():
        continue_out = False
        for j in PREFIXES:
            if i.startswith(j):
                continue_out = True
        if continue_out or i.endswith("s"):
            continue
        if get_endings(i) is None:
            print(i)
            total += 1

print(total)
