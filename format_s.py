#!/usr/bin/env python3

'''
FORMAT S
(see format S.txt)
'''

BYTES_PER_N = 2
ENDIAN = 'big'
STR_ENCODE = 'ascii'


def pack_strings (strings: list):
    '''Pack a list of strings into a single string'''

    # Save the indices and lengths of each string
    indices = [None for _ in strings]
    lengths = [len(x) for x in strings]
    i_strings = enumerate(strings)

    # Pack together the strings
    # Start with the longest because only a longer string can contain a shorter string
    k = lambda e: len(e[1])
    pack = '' 
    longest_first = reversed(sorted(i_strings, key=k))
    for i, s in longest_first:
        find = pack.find(s)
        if find == -1: # not found
            indices[i] = len(pack)
            pack += s
        else:
            indices[i] = find

    return indices, lengths, pack


def read_file (file):
    length = read_num(file)
    idx_len = [(read_num(file), read_num(file)) for i in range(length)]
    packed = str(file.read(), encoding=STR_ENCODE)

    # Unpack
    strings = [unpack_str(i, length, packed) for i, length in idx_len]
    return strings


def write_file (file, strings: list):
    # Pack
    indices, lengths, packed = pack_strings(strings)
    print('packed:', packed)

    # Write the string index table
    write_num(file, len(strings))
    for i, length in zip(indices, lengths):
        write_num(file, i)
        write_num(file, length)
    # Write packed string data
    file.write(bytes(packed, encoding=STR_ENCODE)) 


def unpack_str (index, length, packed):
    return packed[index:index + length]


def read_num (file) -> int:
    data = file.read(BYTES_PER_N)
    return int.from_bytes(data, ENDIAN, signed=False)


def write_num (file, i):
    assert type(i) == int
    return file.write(i.to_bytes(BYTES_PER_N, ENDIAN, signed=False))

