import re

vertex_count, edge_count = map(
    int,
    re.match(r"DIGRAPH (\d+) (\d+):", input()).groups()
)

edges = []
for i in range(edge_count):
    edges.append(map(
        int,
        re.match(r"\s*(\d+)\s*-->\s*(\d+)\s*", input()).groups()
    ))

template = """
param N := @N;

var x{i in 1..N} >= 0, <= N; # upper bound helps if no solution exists
var m >= 0;

minimize obj: m;

cm{i in 1..N}: x[i] <= m;

@C

solve;

printf "#OUTPUT: %d\\n", m;
for {i in 1..N} {
    printf "v_%d: %d\\n", i-1, x[i];
}
printf "#OUTPUT END\\n";

end;
"""

print(template
    .replace("@N", str(vertex_count))
    .replace("@C", "\n".join([
        "c%d: x[%d] <= x[%d] - 1;" % (i+1, j+1, k+1)
        for (i, (j, k)) in enumerate(edges)
    ]))
)
