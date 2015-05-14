program ideone;
var
t:integer;
N,i,count,a,b: LongInt;
begin
	readln(t);
	while t > 0 do
		begin
		readln(N);
		count:=0;
		for i:=0 to N-1 do
			begin
			read(a);
			if i = 0 then
				b:=a
			else
				if a <> b then
				
					count:=count+1;
					b:=a;
			end;
	writeln(count);
	t:= t-1;
	end
end. 
