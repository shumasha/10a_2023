program zadacha29;
var a,b,c:real;
begin
  write('Введите сторону треугольника (a)');
  read(a);
  write('Введите сторону треугольника (b)');
  read(b);
  write('Введите сторону треугольника (c)');
  read(c);
  writeln('Угол альфа = ',ArcCos((sqr(b)+sqr(c)-sqr(a))/(2*b*c)));
  writeln('Угол бета = ',ArcCos((sqr(a)+sqr(c)-sqr(b))/2*a*c));
  writeln('Угол гамма = ',ArcCos((sqr(a)+sqr(b)-sqr(c))/2*a*b)); 
  writeln('Периметр = ',a+b+c);
  writeln
end.