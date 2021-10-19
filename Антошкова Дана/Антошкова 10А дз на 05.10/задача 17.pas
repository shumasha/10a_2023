program zadacha17;
var n: integer; r, p,s: real;
begin
    writeln('Введите  радиус окружности: ');
    readln(r);
    write('Введите число углов: ');
    read(n);
    p:=2*r*n*(sin(pi / n) / cos(pi / n));
    s:= r*r*n*(sin(pi / n) / cos(pi / n));
    writeln('Периметр = ', p:3:2);
    writeln('Площадь = ',s :3:2);
end.