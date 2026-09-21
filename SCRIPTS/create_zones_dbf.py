# create_zones_dbf.py
# Creates a DBF file without external libraries.

import struct

# Number of records you want
num_records = 5

# DBF header constants
version = 3
year = 126   # DBF stores (year - 1900). 2026 → 126.
month = 9
day = 21

# One field descriptor → 32 bytes + 1 terminator
header_length = 33 + 32
record_length = 1 + 6    # delete flag + 6-character numeric field

# Build header
header = bytearray()
header += struct.pack(
    '<BBBBLHH20x',
    version, year, month, day,
    num_records,
    header_length,
    record_length
)

# Field descriptor for ZONEID (numeric, width=6)
field = bytearray(32)
field[0:11] = b'ZONEID\x00\x00\x00\x00\x00'
field[11] = ord('N')      # Type: Numeric
field[12:16] = b'\x00\x00\x00\x00'
field[16] = 6             # Width
field[17] = 0             # Decimal count

# End of field descriptors
terminator = b'\r'

# Create records
records = bytearray()
for i in range(1, num_records + 1):
    rec = bytearray()
    rec.append(0x20)             # not deleted
    rec += f"{i:6d}".encode()    # 6-char right-aligned number
    records += rec

# Write DBF
with open("zones.dbf", "wb") as f:
    f.write(header)
    f.write(field)
    f.write(terminator)
    f.write(records)

print("zones.dbf created successfully.")range