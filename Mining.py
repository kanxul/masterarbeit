from hashlib import sha256

def MAX_NONCE(difficulty):
    return int(16**(difficulty+1) )

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

# Mining 
def mine(block_number, transactions, previous_hash, prefix_zeros):
    max_nonce = MAX_NONCE(prefix_zeros)
    print("{}".format(max_nonce))
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE(prefix_zeros)):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)

        if new_hash.startswith(prefix_str):
            time_stamp = time.time()
            print(f"Yay! Successfully mined bitcoins with nonce value {nonce} at time-stamp {time_stamp}")
            return new_hash, nonce
    
    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__ == '__main__':
    transactions = '''Alex->Hape->20
    Mando->Cara->45
    '''
    difficulty = 4
    import time
    start = time.time()
    print("Start Mining")
    new_hash, nonce = mine(5, 
            transactions, 
            'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78',
            difficulty)
    total_time = str((time.time() - start))
    hash_rate = nonce/float(total_time)/1000000
    print(f"Block Hash : {new_hash}")
    print(f"end mining. Mining took: {total_time} secondes and {hash_rate} MH/s")
    

