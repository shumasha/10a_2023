program zadacha3;
var a, b, c, d: real;
begin
  write('Введите длину ребра куба: ');
  read(a);
  b:= Sqr(a);
  c:= 6 * b;
  d:= a * a * a;
  writeln('Площадь грани куба = ',b);
  writeln('Площадь полной поверхности куба = ',c);
  writeln('Объем куба = ', d);
end.