answer = None
output = None
input = None

name = "PerfectFlush-1002"
with open("data/secret/%s.ans" % name) as afile, open("data/secret/%s.out" % name) as ofile:
    answer = [int(x) for x in afile.readline().split()]
    output = [int(x) for x in ofile.readline().split()]

with open("data/secret/%s.in" % name) as ifile:
    n, k = (int(x) for x in ifile.readline().split())
    input = [int(x) for x in ifile.readlines()]

print(input.index(18078))

for a, o in zip(answer, output):
    print(("  " if a == o else "* ") + "%d\t%d" % (a,o))
