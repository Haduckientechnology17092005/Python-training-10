from collections import Counter
def shanno_fano(symbols):
    if len(symbols) == 1:
        return {symbols[0][0]: ""}
    total = sum([symbol[1] for symbol in symbols])
    acc = 0
    split_idx = 0
    for i, symbol in enumerate(symbols):
        acc+=symbol[1]
        if acc>=total/2:
            split_idx = i
            break
    left_symbols = symbols[:split_idx+1]
    right_symbols = symbols[split_idx+1:]
    left_codes = shanno_fano(left_symbols)
    right_codes = shanno_fano(right_symbols)
    for key in left_codes:
        left_codes[key] = "0" + left_codes[key]
    for key in right_codes:
        right_codes[key] = "1" + right_codes[key]
    return {**left_codes, **right_codes}
def decode_shanno_fano(code, symbols):
    reversed_symbols = {v: k for k, v in symbols.items()}
    decoded = ""
    buffer = ""
    for bit in code:
        buffer += bit
        if buffer in reversed_symbols:
            decoded += reversed_symbols[buffer]
            buffer = ""
    return decoded
def main():
    message = input("Enter your message: ")
    frequency = Counter(message)
    symbols = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    shanno_fano_codes = shanno_fano(symbols)
    print("Shanno-Fano codes:", shanno_fano_codes)
    encoded = "".join(shanno_fano_codes[code] for code in message)
    print("Encoded message:", encoded)
    decoded = decode_shanno_fano(encoded, shanno_fano_codes)
    print("Decoded message:", decoded)
if __name__ == "__main__":
    main()