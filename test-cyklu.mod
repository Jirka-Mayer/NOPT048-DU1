/*
        1 --> 2 --> 3
        ^     |
        |     v
        5 <-- 4
        ^
        |
        6
 */

param n := 10; # prevents solver from freezing if no solution
var x1 >= 0, <= n, integer;
var x2 >= 0, <= n, integer;
var x3 >= 0, <= n, integer;
var x4 >= 0, <= n, integer;
var x5 >= 0, <= n, integer;
var x6 >= 0, <= n, integer;

var b1 >= 0, <= 1, integer;
var b2 >= 0, <= 1, integer;
var b3 >= 0, <= 1, integer;
var b4 >= 0, <= 1, integer;
var b5 >= 0, <= 1, integer;
var b6 >= 0, <= 1, integer;

param M := 200; # first minimize order, then remove edges
minimize obj: x1 + x2 + x3 + x4 + x5 + x6 + M*(b1 + b2 + b3 + b4 + b5 + b6);

param k := 10; # max cycle length
s.t. c1: x1 <= x2 - 1 + k*b1;
s.t. c2: x2 <= x3 - 1 + k*b2;
s.t. c3: x2 <= x4 - 1 + k*b3;
s.t. c4: x4 <= x5 - 1 + k*b4;
s.t. c5: x5 <= x1 - 1 + k*b5;
s.t. c6: x6 <= x5 - 1 + k*b6;

solve;

display x1, x2, x3, x4, x5, x6, obj, b1, b2, b3, b4, b5, b6;

end;



/********************************************************/

/*

param n := 10; # prevents solver from freezing if no solution
var x1 >= 0, <= n, integer;
var x2 >= 0, <= n, integer;
var x3 >= 0, <= n, integer;

var b1 >= 0, <= 1, integer;
var b2 >= 0, <= 1, integer;
var b3 >= 0, <= 1, integer;

minimize obj: x1 + x2 + x3 + 200*(b1 + b2 + b3);

param k := 3; # max cycle length
s.t. c1: x1 <= x2 - 1 + k*b1;
s.t. c2: x2 <= x3 - 1 + k*b2;
s.t. c3: x3 <= x1 - 1 + k*b3;

solve;

display x1, x2, x3, obj, b1, b2, b3;

end;

*/