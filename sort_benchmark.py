import random
import time

N = 1_000_000
MAX_VAL = 65535  # 16-bit integer

def counting_sort(arr, k=MAX_VAL):
    count = [0] * (k + 1)

    for x in arr:
        count[x] += 1

    output = []
    for value, freq in enumerate(count):
        output.extend([value] * freq)

    return output

def radix_sort_16bit(arr):
    output = list(arr)

    for shift in (0, 8):  # 低 8 bits，再高 8 bits
        count = [0] * 256
        temp = [0] * len(output)

        for x in output:
            digit = (x >> shift) & 0xFF
            count[digit] += 1

        for i in range(1, 256):
            count[i] += count[i - 1]

        for x in reversed(output):
            digit = (x >> shift) & 0xFF
            count[digit] -= 1
            temp[count[digit]] = x

        output = temp

    return output

def benchmark(name, func, data):
    start = time.perf_counter()
    result = func(data)
    end = time.perf_counter()
    print(f"{name}: {end - start:.4f} sec")
    return result

def main():
    data = [random.randint(0, MAX_VAL) for _ in range(N)]

    ans1 = benchmark("Python sorted()", sorted, data)
    ans2 = benchmark("Counting Sort", counting_sort, data)
    ans3 = benchmark("Radix Sort", radix_sort_16bit, data)

    assert ans1 == ans2 == ans3
    print("All results are correct.")

if __name__ == "__main__":
    main()
