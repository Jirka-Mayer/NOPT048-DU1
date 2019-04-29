import re

vertex_count, edge_count = map(
    int,
    re.match(r"WEIGHTED DIGRAPH (\d+) (\d+):", input()).groups()
)

weighted_edges = []
for i in range(edge_count):
    weighted_edges.append(tuple(map(
        int,
        re.match(r"(\d+) --> (\d+) \((\d+)\)", input()).groups()
    )))
edges = [(i, j) for (i, j, _) in weighted_edges]

edges_on_cycles = edges
cycles_by_edges = []

#####################
# search for cycles #
#####################

def cycle_found(cycle):
    if cycle not in cycles_by_edges:
        cycles_by_edges.append(cycle)

vertices = list(range(vertex_count))
for v1 in vertices:
    for v2 in [v for v in vertices if (v1, v) in edges]:
        for v3 in [v for v in vertices if (v2, v) in edges]:
            for v4 in [v for v in vertices if (v3, v) in edges]:
                if v1 == v4:
                    cycle_found(set([(v1, v2), (v2, v3), (v3, v4)]))
                for v5 in [v for v in vertices if (v4, v) in edges]:
                    if v1 == v5:
                        cycle_found(set([(v1, v2), (v2, v3), (v3, v4), (v4, v5)]))

#####################
# build the program #
#####################

template = """
param N := @N; # vertex count
set edges := {@E};

param w{i in 1..N, j in 1..N};
var x{i in 1..N, j in 1..N}, >= 0, <= 1, integer;

minimize obj: sum{(i, j) in edges} (w[i, j] * x[i, j]);

# constraints
@C

solve;

printf "#OUTPUT: %d\\n", obj;
for {(i, j) in edges : x[i, j] >= 1} {
    printf "%d --> %d\\n", i-1,  j-1; # 1-base to 0-base index
}
printf "#OUTPUT END\\n";

data;

param w := @W;

end;
"""

print(template
    .replace("@N", str(vertex_count))
    .replace("@E", ", ".join([
        # 0-base to 1-base index
        "(%d, %d)" % (i+1, j+1)
        for (i, j) in edges_on_cycles
    ]))
    .replace("@C", "\n".join([
        "c%d: %s >= 1;" % (
            i+1,
            # 0-base to 1-base index
            " + ".join(["x[%d, %d]" % (i+1, j+1) for (i, j) in cycle])
        )
        for (i, cycle) in enumerate(cycles_by_edges)
    ]))
    .replace("@W", " ".join([
        # 0-base to 1-base index
        "[%d, %d] %d" % (i+1, j+1, w) for (i, j, w) in weighted_edges
    ]))
)
