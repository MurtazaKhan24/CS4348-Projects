import sys
import os

BLOCK_SIZE = 512
MAGIC_NUMBER = b"4348PRJ3"
MIN_DEGREE = 10
MAX_KEYS = 2 * MIN_DEGREE - 1
MAX_CHILDREN = MAX_KEYS + 1

def read_header(f):
    f.seek(0)
    data = f.read(BLOCK_SIZE)
    if data[0:8] != MAGIC_NUMBER:
        raise Exception("Invalid index file.")
    root_id = int.from_bytes(data[8:16], 'big')
    next_id = int.from_bytes(data[16:24], 'big')
    return root_id, next_id

def write_header(f, root_id, next_id):
    header = bytearray(BLOCK_SIZE)
    header[0:8] = MAGIC_NUMBER
    header[8:16] = root_id.to_bytes(8, 'big')
    header[16:24] = next_id.to_bytes(8, 'big')
    f.seek(0)
    f.write(header)

def empty_node(block_id, parent):
    return {
        "block_id": block_id,
        "parent": parent,
        "num_keys": 0,
        "keys": [0] * MAX_KEYS,
        "values": [0] * MAX_KEYS,
        "children": [0] * MAX_CHILDREN
    }

def write_node(f, node):
    b = bytearray(BLOCK_SIZE)
    offset = 0
    b[offset:offset+8] = node["block_id"].to_bytes(8, 'big'); offset += 8
    b[offset:offset+8] = node["parent"].to_bytes(8, 'big'); offset += 8
    b[offset:offset+8] = node["num_keys"].to_bytes(8, 'big'); offset += 8
    for i in range(MAX_KEYS):
        b[offset:offset+8] = node["keys"][i].to_bytes(8, 'big'); offset += 8
    for i in range(MAX_KEYS):
        b[offset:offset+8] = node["values"][i].to_bytes(8, 'big'); offset += 8
    for i in range(MAX_CHILDREN):
        b[offset:offset+8] = node["children"][i].to_bytes(8, 'big'); offset += 8
    f.seek(node["block_id"] * BLOCK_SIZE)
    f.write(b)

def read_node(f, block_id):
    f.seek(block_id * BLOCK_SIZE)
    data = f.read(BLOCK_SIZE)
    node = {
        "block_id": int.from_bytes(data[0:8], 'big'),
        "parent": int.from_bytes(data[8:16], 'big'),
        "num_keys": int.from_bytes(data[16:24], 'big'),
        "keys": [],
        "values": [],
        "children": []
    }
    offset = 24
    for _ in range(MAX_KEYS):
        node["keys"].append(int.from_bytes(data[offset:offset+8], 'big')); offset += 8
    for _ in range(MAX_KEYS):
        node["values"].append(int.from_bytes(data[offset:offset+8], 'big')); offset += 8
    for _ in range(MAX_CHILDREN):
        node["children"].append(int.from_bytes(data[offset:offset+8], 'big')); offset += 8
    return node

def insert_into_node(node, key, value):
    i = node["num_keys"] - 1
    while i >= 0 and key < node["keys"][i]:
        node["keys"][i+1] = node["keys"][i]
        node["values"][i+1] = node["values"][i]
        i -= 1
    node["keys"][i+1] = key
    node["values"][i+1] = value
    node["num_keys"] += 1

def insert(index_file, key, value):
    with open(index_file, 'r+b') as f:
        root_id, next_id = read_header(f)

        if root_id == 0:
            # Create root node
            root = empty_node(next_id, 0)
            insert_into_node(root, key, value)
            write_node(f, root)
            write_header(f, next_id, next_id + 1)
        else:
            root = read_node(f, root_id)
            if root["num_keys"] >= MAX_KEYS:
                print("Error: Root full. Splitting not implemented yet.")
                return
            insert_into_node(root, key, value)
            write_node(f, root)

def search_btree(f, block_id, key):
    if block_id == 0:
        return None

    node = read_node(f, block_id)

    # Scan keys in node
    i = 0
    while i < node["num_keys"] and key > node["keys"][i]:
        i += 1

    # If key matches
    if i < node["num_keys"] and key == node["keys"][i]:
        return (node["keys"][i], node["values"][i])

    # Recurse to child
    child_block = node["children"][i]
    if child_block == 0:
        return None  # leaf node
    return search_btree(f, child_block, key)

def search(index_file, key):
    with open(index_file, 'rb') as f:
        root_id, _ = read_header(f)
        result = search_btree(f, root_id, key)
        if result:
            print(f"Found: key={result[0]}, value={result[1]}")
        else:
            print("Error: Key not found.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: project3 <command> <args>")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == 'create':
        create_index_file(sys.argv[2])
    elif cmd == 'insert':
        if len(sys.argv) != 5:
            print("Usage: project3 insert <index_file> <key> <value>")
        else:
            try:
                insert(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
                print("Inserted.")
            except Exception as e:
                print("Error:", e)
    elif cmd == 'search':
        if len(sys.argv) != 4:
            print("Usage: project3 search <index_file> <key>")
        else:
            try:
                search(sys.argv[2], int(sys.argv[3]))
            except Exception as e:
                print("Error:", e)


