def read_data(filename):
    with open(filename) as f:
        data = {"output": [], "signals": []}
        for line in f.read().splitlines():
            temp = line.split("|")
            data["signals"].append(temp[0].split())
            data["output"].append(temp[-1].split())

    return data


def count_1_4_7_8(data):
    count = 0
    for line in data:
        for entry in line:
            if len(entry) in (2, 3, 4, 7):
                count += 1

    return count


def get_segment_mappings(signals_list):
    mappings = []
    for signals in signals_list:
        mapping = {}
        for signal in signals:
            if len(signal) == 2:
                mapping["1"] = signal
            if len(signal) == 3:
                mapping["7"] = signal
            if len(signal) == 7:
                mapping["8"] = signal
            if len(signal) == 4:
                mapping["4"] = signal

        for signal in signals:
            if len(signal) == 6:
                if 0 not in [c in signal for c in mapping["4"]]:
                    mapping["9"] = signal
                elif 0 not in [c in signal for c in mapping["7"]]:
                    mapping["0"] = signal
                else:
                    mapping["6"] = signal

        for signal in signals:
            if len(signal) == 5:
                if 0 not in [c in mapping["6"] for c in signal]:
                    mapping["5"] = signal
                elif 0 not in [c in signal for c in mapping["7"]]:
                    mapping["3"] = signal
                else:
                    mapping["2"] = signal
        mappings.append(mapping)
    return mappings


def get_outputs(outputs, mappings):
    nums = []
    for output, mapping in zip(outputs, mappings):
        num = ""
        for output_val in output:
            for i in range(len(mapping.keys())):
                if (0 not in [c in mapping[str(i)] for c in output_val]) and (len(mapping[str(i)]) == len(output_val)):
                    num += str(i)

        nums.append(int(num))

    return nums


def main():
    data = read_data("input.txt")
    print(count_1_4_7_8(data["output"]))
    mappings = get_segment_mappings(data["signals"])
    outputs = get_outputs(data["output"], mappings)
    print(sum(outputs))


if __name__ == "__main__":
    main()
