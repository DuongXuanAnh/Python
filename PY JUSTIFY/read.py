import sys

print(sys.argv[1])



while True:
    c = sys.stdin.read(1)
    if not c:
        break
    print(c)