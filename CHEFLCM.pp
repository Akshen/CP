program ideone;
var
a,b,t,s: longint;
begin
	readln(t);
	while t>0 do
	begin
		s:=0;
		readln(a);
		for b:=1 to a do
		begin
			if(a mod b = 0)then
				s:=s+b;
		end;
		writeln(s);
		t:= t-1;
	end;
end.