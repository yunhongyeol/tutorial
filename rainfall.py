def parse_date(text):
    """
    e.g. '20200112' -> 2020, 1, 12
    """
    year = text[0:4]  # str <- ordered sequence of characters
    month = text[4:6]
    day = text[6:]
    return year, str(int(month)), str(int(day))


def multiply_ten(all_day_rainfall):
    result = []
    for item in all_day_rainfall:
        if len(item) > 0:
            item = str(int(float(item) * 10))
            result.append(item)
        else:
            result.append(item)
    return result


filename = "./rainfalls/rainfall_daegu_2020.txt"

with open(filename, "rt", encoding="UTF8") as f:
    lines = f.readlines()

output_filename = filename.replace(".txt", "") + "_c.txt"
print(output_filename)
with open(output_filename, "w") as f:
    for line in lines[1:]:
        splits = line.split("|")

        # position information
        region_id_pos = 0
        date_pos = 2
        per_hour_rainfalls_pos_start = 3
        per_hour_rainfalls_pos_end = 27

        # data extraction
        region_id = splits[region_id_pos]
        year, month, day = parse_date(splits[date_pos])
        rainfalls = multiply_ten(
            splits[per_hour_rainfalls_pos_start:per_hour_rainfalls_pos_end]
        )
        new_row = [region_id, year, month, day] + rainfalls + ["\n"]

        final = "|".join(new_row)
        f.write(final)


if __name__ == "__main__":
    pass
