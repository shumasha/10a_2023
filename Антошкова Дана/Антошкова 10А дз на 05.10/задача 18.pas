program zadacha18;
var a:integer;
begin
write ('Введите время в секундах:');
read (a);
writeLn('часы:',a div 3600);
writeLn('минуты:',a mod 60);
writeLn('секунды:',a mod 60);
end.