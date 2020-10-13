#!/usr/bin/env python

from struct import Struct

"""
struct thing {
    int a;
    int b;
    float c;
    char[10] d;
}
"""
values = 7, 6, 42.3, b'Guido' # <1>

demo = Struct('iif10s')  # <2>

print("Size of data: {} bytes".format(demo.size)) # <3>

# binary_stream = demo.pack(*values) # <4>
binary_stream = demo.pack(7, 6, 42.3, b'Guido')

print("stream:", binary_stream)

int1, int2, float1, raw_bytes = demo.unpack(binary_stream) # <5>
str1 = raw_bytes.rstrip(b'\x00').decode()  # <6>

print(raw_bytes)
print(str1)
print(int1, int2, float1, str1)
