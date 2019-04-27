param N := 3;

var x{i in 1..N} >= 0;
var m >= 0;

minimize obj: m;

cm{i in 1..N}: x[i] <= m;

c1: x[1] <= x[2] - 1;
c2: x[2] <= x[3] - 1;

solve;

printf "#OUTPUT: %d\n", m;
for {i in 1..N} {
    printf "v_%d: %d\n", i, x[i];
}
printf "#OUTPUT END\n";

end;
