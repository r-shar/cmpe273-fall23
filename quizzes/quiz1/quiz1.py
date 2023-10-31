from lib import duckdb
from bloomFilter import BloomFilter
import sys

bloomFilter = BloomFilter(sys.maxsize, 100)

def insert_into_bloom_filter():
    [sjsu_id, _] = duckdb.read_csv('students.csv', header=True, sep='|')
    bloomFilter.add(sjsu_id)

    
def run_query(sjsu_id):
    found = bloomFilter.lookup(sjsu_id)
    if found:
        return duckdb.sql("SELECT * FROM 'students.csv' WHERE SJSU_ID = '{sjsu_id}'")
    else:
        return "Key not found, query will not be run."



if __name__ == "__main__":
    insert_into_bloom_filter
    run_query()