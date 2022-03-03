from __future__ import print_function, division


def most_frequent(s):
    hist = make_histogram(s)
    print(hist)
    t = []
    for x, freq in hist.items():
        t.append((freq, x))

    t.sort(reverse=True)
    res = []
    for freq, x in t:
        res.append(x)
    return res
    

def make_histogram(s):
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist

if __name__ == '__main__':
    string = open('emma.txt').read()
    letter_seq = most_frequent(string)
    print(letter_seq)