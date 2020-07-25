
'''
Given a file and assume that you can only read the file using
a given method read4, implement a method to read n characters.

Method read4:

The API read4 reads 4 consecutive characters from the file,
then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Method read:

By using the read4 method, implement the method read that reads n
characters from the file and store it in the buffer array buf.
Consider that you cannot manipulate the file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

Note: buf[] is destination not source, you will need to write
the results to buf[]


'''


class MyFile():
    def __init__(self, fname, debug=False):
        self.fp = open(fname)
        self.debug = debug

    def read4(self, buf):
        buf.clear()
        chars = self.fp.read(4)
        buf += list(chars)
        return len(buf)

    def seek_backwards(self, n):
        if n < 1:
            return
        pos = self.fp.tell()
        self.fp.seek(pos - n)

    def read(self, buf, n):
        if n < 1:
            buf.clear()
            return 0
        if n == 4:
            return self.read4(buf)
        if n < 4:
            buf2 = []
            n2 = self.read4(buf2)
            buf.clear()
            buf += buf2[:n]
            self.seek_backwards(n2 - n)
            return len(buf)
        if n > 4:
            buf.clear()
            n2 = n
            buf2 = []
            while n2 > 4:
                nn = self.read4(buf2)
                if nn < 1:
                    n2 = 0
                    break
                buf += buf2
                n2 -= nn
            nn = self.read(buf2, n2)
            buf += buf2
            return len(buf)

if __name__ == '__main__':

    import sys
    import random

    buf = []
    x = MyFile(sys.argv[1])

    while True:
        n = x.read(buf, random.choice(list(range(1, 21))))
        if n < 1:
            break
        print(''.join(buf), end='')

# vim: ai sw=4 ts=4 et showmatch
