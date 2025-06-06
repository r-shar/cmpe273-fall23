# Implement a BloomFilter to intercept SELECT and INSERT operations of [DuckDB](https://duckdb.org/docs/api/python/data_ingestion) to imporove performance.
import hashlib
import math

class BloomFilter:
    def __init__(self, size, num_hashes, salt=None):
        self.size = size
        self.num_hashes = num_hashes
        self.salt = salt or ''
        self.bit_array = [0] * size

    def add(self, element):
        for i in range(self.num_hashes):
            digest = hashlib.sha1((self.salt + str(element) + str(i)).encode('utf-8')).hexdigest()
            index = int(digest, 16) % self.size
            self.bit_array[index] = 1

    def lookup(self, element):
        for i in range(self.num_hashes):
            digest = hashlib.sha1((self.salt + str(element) + str(i)).encode('utf-8')).hexdigest()
            index = int(digest, 16) % self.size
            if self.bit_array[index] == 0:
                return False
        
        return True

### Requirement

'''
* You can assume data comes from input.csv file and it has the following format in the file:
SJSU_ID,Name
11111111,"John Smith"

### Example:
1. Your BloomFilter should return true and then let the query executes. 
SELECT * FROM 'students.csv' WHERE SJSU_ID = '11111111'

2. Your BloomFilter should return false and then not let the query executes. 
SELECT * FROM 'students.csv' WHERE SJSU_ID = '2222222222'
'''
