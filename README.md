## Hashdump-specific

A simple hash tool is used to calculate specific hash values. 

####  `hash_algorithm` that allows the user to specify the hashing algorithm to use

```python
def brute_force_hash(*,*,hash_algorithm='*')
```

#### Use `hashlib.new` to dynamically select a hash algorithm. This method makes it possible to support algorithms such as 

#### MD5, SHA-1, SHA-256, etc.

```python
hash_func = hashlib.new(hash_algorithm)
```

####  `update()` method to update the value of the hash object, so that the hash value can be gradually accumulated.

```python
hash_func.update(attempt_str.encode())
attempt_hash = hash_func.hexdigest()
```

