program zadacha6;
var a, b, c, d, x1, x2: real;
begin
  write('a = ');  
  read(a);
  write('b = ');  
  read(b);
  write('c = ');  
  read(c);
  d:=b*b-4*a*c;
  x1:=(-b + sqrt(d))/(2*a);
  x2:=(-b - sqrt(d))/(2*a);
  writeln('x1 = ', x1:5:2);
  writeln('x2 = ', x2:5:2);
end.