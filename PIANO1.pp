program ideone;
var
    sum,N,i,strlen,t,kcount,tScale,temp : longint;
    S : string;
begin
    readln(t);
    while t>0 do
        begin
        readln(S);
        strlen:=Length(S);
        readln(N);
        kcount:=N*12;
        sum:=0;tScale:=0;temp:=0;
        for i:=0 to strlen do
            begin
            if S[i] = 'T' then
                tScale:=tScale + 2;
            if S[i] = 'S' then
                tScale:=tScale +1;
            end;
        i:=tScale;
        while kcount>i do
            begin
                sum:= sum + (kcount - i);
                i:= i+tScale;
            end;
        writeln(sum);
    t:=t-1;
    end;
end. 