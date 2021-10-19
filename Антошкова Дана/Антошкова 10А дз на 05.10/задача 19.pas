program zadcha19;
var r:real;
begin
    write('Введите число вида (nnn.ddd): ');
    readln(r);
    writeln('Полученное новое число: ',frac(r)*1000+trunc(r)/1000:3:3);
end.