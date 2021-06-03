import sys


def get_data_from_file(filename):
    with open(filename, "r") as file:
        file_data = file.readlines()
        for i in range(len(file_data)):
            file_data[i] = list(map(int, file_data[i].split()))
    return file_data


def write_arr_2d_to_file(filename, arr_2d):
    with open(filename, "w") as file:
        for line in arr_2d:
            arr_2d = " ".join(map(str, line)) + "\n"
            file.writelines(arr_2d)


def swap(arr_2d, first_idx, second_idx):
    arr_2d[first_idx], arr_2d[second_idx] = arr_2d[second_idx], arr_2d[first_idx]


def is_non_decreasing_sequence(line):
    prev_el = line[0]
    if len(line) > 1:
        for i in range(len(line)):
            if prev_el > line[i]:
                return False
    return True


def raise_non_decreasing_lines(data):
    to_idx = 0
    for i in range(len(data)):
        if is_non_decreasing_sequence(data[i]):
            swap(data, to_idx, i)
            to_idx += 1


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_data = get_data_from_file(sys.argv[1])
        raise_non_decreasing_lines(file_data)
        write_arr_2d_to_file(sys.argv[2], file_data)
    else:
        file_data = get_data_from_file(input("Enter input file: "))
        raise_non_decreasing_lines(file_data)
        write_arr_2d_to_file(input("Enter output file: "), file_data)
