program zadacha7;
var a, b, c, s: real;
begin
  write('a = ');  
  read(a);
  write('b = ');  
  read(b);
  write('угол альфа = ');  
  read(c);
  c:=(c*pi)/180;
  s:=(1/2)*(sqr(b)-sqr(a))*tan(c);
  writeln('Площадь трапеции = ', s:3:2);
end.