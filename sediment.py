with open('./rainfalls/rainfall_daegu_2020.txt', 'rt', encoding='UTF8') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line.replace('\n', ''))


if __name__ == "__main__":
    pass

