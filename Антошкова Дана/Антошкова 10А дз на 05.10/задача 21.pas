program zadacha21;
var y,b:integer;
begin
write('Введите поворот часово стрелки в градусах:');
read(y);
b:=y*120;
writeln('часы:',b div 3600);
writeln('минуты:',y mod 3600 div 60);
writeln('секунды:',y mod 3600 mod 60);
end.