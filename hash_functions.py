import hashlib

def simple_hash_function(s: str, n: int):
    return int(sum([ord(char) for char in s])) % (10 ** n)
    
def complex_hash_function(s: str, n: int):
    return int(hashlib.sha1(s.encode("utf-8")).hexdigest(), 16) % (10 ** n)

def generate(func, digits):
    def wrapper(s):
        return func(s, digits)
    return wrapper

if __name__ == "__main__":
    digits = 7
    sample = 'hello world'
    hash_function = generate(complex_hash_function, digits)
    print(f"{sample} -> {hash_function('hello world')}")

