program zadacha15;
var x1, x2, x3, y1, y2, y3, p, d, s, a, b, c: real;
begin
  write('Ввидите координаты первой точки: ');  
  read(x1, y1);
  write('Введите координаты второй точки: ');
  read(x2, y2);
  write('Введите координаты третьей точки: ');  
  read(x3, y3);
  a:=sqrt(sqr(x2-x1)+sqr(y2-y1));
  b:=sqrt(sqr(x3-x2)+sqr(y3-y2));
  c:=sqrt(sqr(x3-x1)+sqr(y3-y1));
  P:=a+b+c;
  d:=p/2;
  s:=sqrt(d*(d-a)*(d-b)*(d-c));
  writeln('Периметр треугольника = ', p:3:2);
  writeln('Площадь треугольника = ', s:3:2);
end.