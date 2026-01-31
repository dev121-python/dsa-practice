# Hash Table (Chaining Implementation)

This is a simple implementation of a hash table using **separate chaining** for collision handling.

## Structure

- The hash table uses a fixed-size array of buckets.
- Each bucket is a Python list.
- Each entry in a bucket is stored as a `(key, value)` tuple.

```python
self.buckets = [[] for _ in range(10)]
