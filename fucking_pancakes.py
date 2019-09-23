
# Using a stupid spatula of length k,
# flip the bits of pancakes k bits at a time,
# until all the stupid fucking bits match

def solve(pancakes, k):

    print(pancakes, k)

def main():
    with open('A-small-practice.in', 'r') as infile:
        for line in infile:
            if len(line.split()) == 2:
                pancakes, n = line.split(' ')
                n = int(n)
                solve(pancakes, n)

main()
