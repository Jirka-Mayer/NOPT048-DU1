param N := 3; # vertex count
set edges := {(1, 2), (2, 3), (3, 1)};

param w{i in 1..N, j in 1..N};
var x{i in 1..N, j in 1..N}, >= 0, <= 1, integer;

minimize obj: sum{(i, j) in edges} (w[i, j] * x[i, j]);

# constraints
c1: x[1, 2] + x[2, 3] + x[3, 1] >= 1;

solve;

printf "#OUTPUT: %d\n", obj;
for {(i, j) in edges : x[i, j] >= 1} {
    printf "%d --> %d\n", i-1,  j-1; # 1-base to 0-base index
}
printf "#OUTPUT END\n";

data;

param w := [1, 2] 5 [2, 3] 6 [3, 1] 7;

end;
