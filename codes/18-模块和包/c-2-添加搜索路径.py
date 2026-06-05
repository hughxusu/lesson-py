import sys

print(sys.path)
sys.path.insert(0, '/')
print(sys.path)
sys.path.remove('/')
print(sys.path)
