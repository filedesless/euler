from sol21 import alliquot


def abundant(n):
    return alliquot(n) > n


if __name__ == '__main__':
    assert list(filter(abundant, range(50))) == [
        12, 18, 20, 24, 30, 36, 40, 42, 48]

    candidates = set(range(1, 28124))
    abundants = [i for i in candidates if abundant(i)]
    abundant_sum = {x+y for x in abundants for y in abundants}
    non_abundant_sum = candidates - abundant_sum

    print(len(abundant_sum), list(abundant_sum)[:10])
    print(len(non_abundant_sum), list(non_abundant_sum)[:10])
    print(sum(non_abundant_sum))
