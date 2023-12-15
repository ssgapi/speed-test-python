from time import time


def main():
    n = 1_000_000_000
    start = time()
    print(f"\nCounting to {count(n):,}", end=" ")
    end = time() - start

    print(f"Counting to took {end:.3f} seconds.\n")


def count(i=0):
    j = 0
    while j < i:
        j += 1
    return j


if __name__ == "__main__":
    main()
