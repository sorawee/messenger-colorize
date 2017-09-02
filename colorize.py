import sys
from webcolors import name_to_rgb

if len(sys.argv) != 4:
    print('Usage: python3 colorize.py "<your text>" <color-start> <color-stop>', file=sys.stderr)
    sys.exit(1)

rA, gA, bA = name_to_rgb(sys.argv[2])
rB, gB, bB = name_to_rgb(sys.argv[3])

def get_step(start, stop, i, n):
    return format(start + ((stop - start) * i // n), '02x')

s = sys.argv[1]

buffer = []
for i, c in enumerate(s):
    r = get_step(rA, rB, i, len(s))
    g = get_step(gA, gB, i, len(s))
    b = get_step(bA, bB, i, len(s))
    buffer.append('\\(')
    buffer.append('\\text{{\\color{{#{}{}{}}}{}}}'.format(r, g, b, c))
    buffer.append('\\)')

print(''.join(buffer))
