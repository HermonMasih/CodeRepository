# Binary String consisting of  a sequence of 1's and 0's representing a english word where
# sequence of 1's represent different alphabets and 0's act as separator between them.

data=input("Enter the Binary String\n").strip()
alpha=list(map(chr, range(65, 91)))
fstr=""
c=0
for i in data:
    if i=='1':
        c=c+1
    else:
        if c>26:
            c=c-26
            fstr=fstr+alpha[c-1]
            c=0
        else:
            fstr=fstr+alpha[c-1]
            c=0

print(f'The Decoded version of {data} is {fstr}')


