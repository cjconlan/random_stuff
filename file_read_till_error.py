import os, time, pathlib

file = pathlib.Path('testfile')
file.touch()
os.truncate(file, int(100*1e6))
counter = 0

def reader():
    while True:
        d = os.read(f, int(50*1e6))
        if not d: break

while True:
    t = time.gmtime(time.time())
    ts = time.strftime("%Y-%m-%d %H:%M:%S", t)
    try:
        counter += 1
        if (counter % 100) == 0:
            print(ts, counter)
        reader()
    except Exception as err:
        print(err)
        print(ts, counter)
        raise
    time.sleep(1)
    

