program zadacha2;
var x1,x2,y1,y2: real;
begin
  write('Введите координаты первой точки: ');
  read(x1, y1);
  write('Введите координаты второй точки: ');
  read(x2, y2);
  writeln('Расстояние между точками = ', sqrt(sqr(x2-x1)+sqr(y2-y1)):3:2);
end.