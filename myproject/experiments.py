with open("logfile.txt", "r", encoding='utf-8') as logfile, open("output.txt", "w", encoding="utf-8") as out:
    for line in logfile.readlines():
        delta = []
        for el in line.strip().split(", ")[1:]:
            delta.append(int(el.split(":")[0])*60 + int(el.split(":")[1]))

        if abs(delta[0] - delta[1]) >=60:
            print(line.strip().split(", ")[0], file=out)
