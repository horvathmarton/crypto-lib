from os import urandom
from string import ascii_lowercase, digits

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from requests import get

KEY = urandom(16)
FLAG = 'crypto{aaaaaaaaaaaaaabbbb}'
ALPHABET = ascii_lowercase + digits + '_{}'
BLOCK_SIZE = 16

def parse_blocks(response: str) -> list[str]:
    return [response[i:i + 2 * BLOCK_SIZE] for i in range(0, len(response), 2 * BLOCK_SIZE)]

def check_result(blocks: list[str]) -> bool:
    if len(blocks) == 4:
        return blocks[0] == blocks[-1]
    elif len(blocks) == 6:
        return blocks[0] == blocks[-2] and blocks[1] == blocks[-1]
    else:
        raise Exception(f'Unknown block amount {len(blocks)}')

def prepare_message(guess: str, flag_length: int = BLOCK_SIZE) -> str:
    flag_padding = (BLOCK_SIZE - (flag_length % BLOCK_SIZE)) * '41' + len(guess) * '42'

    return pad(guess.encode(), BLOCK_SIZE).hex() + flag_padding

def encrypt(plaintext: str) -> str:
    p_bytes = bytes.fromhex(plaintext)

    padded = pad(p_bytes + FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        encrypted = cipher.encrypt(padded)
    except ValueError as e:
        raise

    return encrypted.hex()

def fetch_result(message: str) -> str:
    return get(f'http://aes.cryptohack.org/ecb_oracle/encrypt/{message}/').json()['ciphertext']

def main():
    flag = ''

    while not flag.startswith('crypto{'):
         for letter in ALPHABET:
            prepared_message = prepare_message(letter + flag, 25)
            result = fetch_result(prepared_message)
            blocks = parse_blocks(result)
            is_correct = check_result(blocks)

            if is_correct:
                flag = letter + flag
                print(f'Found: {flag}')
                break

    print(f'Flag: {flag}')

main()
