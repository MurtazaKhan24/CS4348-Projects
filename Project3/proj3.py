import sys
import os

BLOCK_SIZE = 512
MAGIC_NUMBER = b"4348PRJ3"

def write_header(file_path):
    # Create a 512-byte block
    header = bytearray(BLOCK_SIZE)

    # Write magic number
    header[0:8] = MAGIC_NUMBER

    # Write root ID = 0 (empty tree)
    header[8:16] = (0).to_bytes(8, byteorder='big')

    # Write next block ID = 1 (first node will go here)
    header[16:24] = (1).to_bytes(8, byteorder='big')

    # Write the header block to file
    with open(file_path, 'wb') as f:
        f.write(header)

def create_index_file(index_file):
    if os.path.exists(index_file):
        print("Error: File already exists.")
        return
    write_header(index_file)
    print(f"Index file '{index_file}' created.")

# Entry point for command-line use
if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] != 'create':
        print("Usage: project3 create <index_file>")
    else:
        create_index_file(sys.argv[2])
