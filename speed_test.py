from time import time


def main():
    start = time()
    print(f"\nCounting to {func(1000000000):,}", end=" ")
    end = time() - start

    print (f"took {end:.3f} seconds.\n")


def func(i=0):
    n = 0
    while n < i:
        n += 1
    return n

if __name__ == '__main__':
    main()