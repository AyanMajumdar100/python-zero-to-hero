# 
import sys
data = []
for i in range(10):
    # You will see the byte size jump in chunks, not every single iteration
    print(f"Length: {len(data)} | Size in Memory: {sys.getsizeof(data)} bytes")
    data.append(i)
# OUTPUT : 
# Length: 0 | Size in Memory: 56 bytes
# Length: 1 | Size in Memory: 88 bytes
# Length: 2 | Size in Memory: 88 bytes
# Length: 3 | Size in Memory: 88 bytes
# Length: 4 | Size in Memory: 88 bytes
# Length: 5 | Size in Memory: 120 bytes
# Length: 6 | Size in Memory: 120 bytes
# Length: 7 | Size in Memory: 120 bytes
# Length: 8 | Size in Memory: 120 bytes
# Length: 9 | Size in Memory: 184 bytes