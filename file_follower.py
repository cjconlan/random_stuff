#!/usr/bin/env python3

"""
A python implementation of a file follower
Supports multiple files
Supports following files with lines terminated by only ^M (0xD, \r), that may be 
created when logging a terminal
Note: tail -f (--follow) does now work for the above ^M example, hence the reason for createing this.
"""

import threading, pathlib, time

class file_follower():
    def __init__(self, files):
        self.file_list = []
        self.run = False
        self.threads = None
        try:
            if isinstance(files, list):
                err = "Error: File paths must be strings"
                assert(all([isinstance(item, str) for item in files])), err
                for file in files:
                    f = pathlib.Path(file)
                    assert(f.exists()), "Error: File does not exist -> {}".format(file)
                    self.file_list.append(f)
            elif isinstance(files, str):
                f = pathlib.Path(files)
                assert(f.exists()), "Error: File does not exist -> {}".format(files)
                self.file_list.append(f)
                files = [files]
            else:
                assert(0)
        except AssertionError:
            raise
        except:
            raise Exception('must be str or list of str')
        finally:
            self.files = files
 
    def _followf(self, f):
        err = "Error: file must be an instance of pathlib.PosixPath"
        assert(isinstance(f, pathlib.PosixPath)), err
        multiple_files = (len(self.file_list) > 1)
        self.run = True
        self.last_printed = None
        fname = f.name
        last = ''
        while self.run:
            new = f.read_text()
            diff = new.replace(last, '')
            if diff:
                if multiple_files and (self.last_printed != fname):
                    print("--->[{}]".format(fname))
                    self.last_printed = fname
                print(diff.strip())
            last = new
        print('Finished')
 
    def start(self):
        if self.threads:
            print('Already started')
        else:
            self.threads = [threading.Thread(target=self._followf, args=(f,))
                            for f in self.file_list]
            for th in self.threads:
                th.start()
                print('Started {}'.format(th.name))
 
    def stop(self):
        print('stopping')
        self.run = False
        if self.threads:
            for th in self.threads:
                if th.is_alive():
                    th.join()
                    print('Stopped {}'.format(th.name))
            self.threads = None

files = ['/tmp/a.txt', '/tmp/b.txt']

try:
    f = file_follower(files)
    f.start()
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    f.stop() 
