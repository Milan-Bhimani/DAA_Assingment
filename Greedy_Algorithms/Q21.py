import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def calculate_frequency(string):
    frequency = {}
    for char in string:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1
    return frequency

def build_heap(frequency):
    heap = []
    for key in frequency:
        node = Node(key, frequency[key])
        heapq.heappush(heap, node)
    return heap

def merge_nodes(heap):
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

def build_codes_helper(root, current_code, codes):
    if root == None:
        return

    if root.char != None:
        codes[root.char] = current_code

    build_codes_helper(root.left, current_code + "0", codes)
    build_codes_helper(root.right, current_code + "1", codes)

def build_codes(root):
    codes = {}
    build_codes_helper(root, "", codes)
    return codes

def print_codes(codes):
    for char in codes:
        print(f"{char}: {codes[char]}")

def huffman_encoding(string):
    frequency = calculate_frequency(string)
    heap = build_heap(frequency)
    merge_nodes(heap)

    root = heap[0]
    codes = build_codes(root)
    print_codes(codes)

string = "abcdef"
huffman_encoding(string)