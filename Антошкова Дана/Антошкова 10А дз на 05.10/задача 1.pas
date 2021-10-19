program zadacha1;
var r, p, s: real;
begin
  write('Введите радиус круга: ');
  read(r);
  writeln('Длина окружности = ', 2*pi*r:3:2);
  writeln('Площадь окружности = ', pi*Sqr(r):3:2);
end.