import struct



def bytes_to_int(bytes: list) -> int:
        result = 0
        for byte in bytes:
            result = (result << 8) + byte
        return result


def get_flac_duration(filename: str) -> float:
    """
    Returns the duration of a FLAC file in seconds
    https://xiph.org/flac/format.html
    """
    with open(filename, 'rb') as f:
        if f.read(4) != b'fLaC':
            raise ValueError('File is not a flac file')
        header = f.read(4)
        while len(header):
            meta = struct.unpack('4B', header)  # 4 unsigned chars
            block_type = meta[0] & 0x7f  # 0111 1111
            size = bytes_to_int(header[1:4])

            if block_type == 0:  # Metadata Streaminfo
                streaminfo_header = f.read(size)
                unpacked = struct.unpack('2H3p3p8B16p', streaminfo_header)
           
                samplerate = bytes_to_int(unpacked[4:7]) >> 4
                sample_bytes = [(unpacked[7] & 0x0F)] + list(unpacked[8:12])
                total_samples = bytes_to_int(sample_bytes)
                duration = float(total_samples) / samplerate

                return duration
            header = f.read(4)
