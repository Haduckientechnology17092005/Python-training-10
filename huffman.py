import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def create_huffman_codes(node, prefix="", codebook={}):
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        create_huffman_codes(node.left, prefix + "0", codebook)
        create_huffman_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encode(message):
    frequencies = defaultdict(int)
    for char in message:
        frequencies[char] += 1

    huffman_tree = build_huffman_tree(frequencies)
    huffman_codes = create_huffman_codes(huffman_tree)

    encoded_message = ''.join(huffman_codes[char] for char in message)
    return encoded_message, huffman_codes, huffman_tree

def huffman_decode(encoded_message, huffman_tree):
    decoded_message = ""
    current_node = huffman_tree

    for bit in encoded_message:
        current_node = current_node.left if bit == '0' else current_node.right
        if current_node.char is not None:
            decoded_message += current_node.char
            current_node = huffman_tree

    return decoded_message

def main():
    message = input("Enter your message: ")
    
    # Mã hóa
    encoded_message, huffman_codes, huffman_tree = huffman_encode(message)
    print("Bảng mã Huffman:", huffman_codes)
    print("Thông điệp sau khi mã hóa:", encoded_message)

    # Giải mã
    decoded_message = huffman_decode(encoded_message, huffman_tree)
    print("Thông điệp sau khi giải mã:", decoded_message)

main()
