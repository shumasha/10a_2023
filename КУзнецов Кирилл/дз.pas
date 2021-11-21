program dkd1;
  var bak,polbak,s,rashod:real;
  begin
  Writeln('Введите обьем бака в литрах');
  read(bak);
  polbak:=bak/2;
  Writeln('Введите расход топлива на 100км');
  read(rashod);
  s:=rashod*polbak;
  write('На половине бака можно проехать - ',s);
  write(' км');
  end.