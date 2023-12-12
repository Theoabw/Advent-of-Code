import hashlib


def mine_adventcoin(secret_key, num_zeros):
    target_prefix = '0' * num_zeros
    number = 1

    while True:
        data = f"{secret_key}{number}".encode('utf-8')
        md5_hash = hashlib.md5(data).hexdigest()

        if md5_hash[:num_zeros] == target_prefix:
            return number

        number += 1

# Replace 'your_secret_key' with your actual secret key
secret_key = 'iwrupvqb'
part1 = mine_adventcoin(secret_key, num_zeros=5)
print(f"The lowest number for part 1 is {part1}")
part2 = mine_adventcoin(secret_key, num_zeros=6)
print(f"The lowest number for part 2 is {part2}")
