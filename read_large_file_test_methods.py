import os, time, pathlib

def read_file(file, n=1000) -> tuple:
    # Reads the whole file and returns time taken
    f = os.open(file, os.O_RDONLY)
    rx_len = 0
    t = 0
    while True:
        s = time.time()
        rx = os.read(f, n)
        t += time.time() - s
        if not rx:
            break
        rx_len += len(rx)
    os.close(f)
    return t, rx_len

def read_file2(file, n=1000, flush=False) -> tuple:
    # Faster even with flush
    # Reads the whole file and returns time taken
    with open(file, "rb") as f:
        rx_len = 0
        t = 0
        while True:
            s = time.time()
            if flush:
                f.flush()
            rx = f.read(n)
            t += time.time() - s
            if not rx:
                break
            rx_len += len(rx)
    return t, rx_len

def create_file(test_file="test_file", sizegb=1):
    with open(test_file, "wb") as f:
        for i in range(int(sizegb*1000)):
            w = f.write(os.urandom(int(1e6)))  # 1 MB at a time
        print(os.stat(f.name))

def create_zero_file(test_file="test_file", sizegb=1):
    pathlib.Path(test_file).touch()
    os.truncate(test_file, int(sizegb*1e9))
    print(os.stat(test_file))

data_file = "/tmp/test_file_real_data"
nul_file = "/tmp/test_file_nul_data"

create_file(data_file, 5)  # Create 5 GB file with random rata, slow
create_zero_file(nul_file, 5)  # Truncate/Create 5 GB file with nul rata, fast

duration1, size1 = read_file2(data_file)
duration2, size2 = read_file2(nul_file)
assert size1 == size2, "Read amounts vary!"
pc = round((1 - (duration2 / duration1)) * 100, 1)
print(f"Reading nul data via open() was {pc} % faster")

duration3, size3 = read_file(data_file)
duration4, size4 = read_file(nul_file)
assert size3 == size4, "Read amounts vary!"
pc = round((1 - (duration4 / duration3)) * 100, 1)
print(f"Reading nul via data via os.open() was {pc} % faster")

pc = round((1 - (duration1 / duration3)) * 100, 1)
print(f"Reading real data via open() was {pc} % faster than os.open()")

pc = round((1 - (duration2 / duration4)) * 100, 1)
print(f"Reading nul data via open() was {pc} % faster than os.open()")



