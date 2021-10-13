# Format S

**Format s** is a binary data format for storing text strings. The rationale is that sometimes you want to store lots of strings in a file or database efficiently. This data format is probably as compact as it can get without using null-terminated strings, which are costly to skip through. This format uses length encoding, and this data format could conceivable be directly memory-mapped. One example use case is a string translation table.

The proposed file extension is ".str".

## Specification

Psuedo-code for the structure (I will explain this later):

    {
        # header
        width [1] 
        count [width] 
        # header - array of "pointers"
        string\_pointers [count] {
            offset [width] # index into the string data
            length [width] # length of bytes, not character count
        }
        # raw string data bytes
        strings []
    }

The number of strings and then a list of pairs of offsets and lengths into the rest of the data, relative to the beginning of the file. Strings are packed back-to-back, and there are no null terminators because the strings are length encoded in the header.

## TODO

Add a string payload size field

## License

See the file called "LICENSE.txt" for more information.

