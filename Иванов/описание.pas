
function sr(n: integer): real;
var i, k, t: integer;
begin
  while n > 0 do
  begin
    k := n mod 10;
    i := i + k;
    n := n div 10;
    t := t + 1;
  end;
  sr := i / t;
end;

//var b: real;
var y:real;
begin
y:=sr;
  writeln(b);
end.
