from __future__ import print_function
def Queens(MatSize):
    marked = {"cols": set(), "diag_one": set(), "diag_two": set()}
    results = set()
    if n_queen_helper(MatSize, 0, marked, results):
        for i in range(MatSize):
            for j in range(MatSize):
                print("Q" if (i, j) in results else "x", end=' ')
            print()
    else:
        print('No Solution Exists')
    print('*'*100)

def n_queen_helper(n, row, marked, results):
    if row == n:
        return True

    for col in range(n):

        if col in marked['cols'] or \
        (row - col) in marked['diag_one'] or \
        (row + col) in marked['diag_two']:
            continue

        results.add((row, col))
        marked['cols'].add(col)
        marked['diag_one'].add(row - col)
        marked['diag_two'].add(row + col)

        if n_queen_helper(n, row + 1, marked, results):
            return True

        results.remove((row, col))
        marked['cols'].remove(col)
        marked['diag_one'].remove(row - col)
        marked['diag_two'].remove(row + col)

    return False


Queens(input())
