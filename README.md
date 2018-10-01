# CompilerInProlog
A compiler from a simple language to assembly of a stack-based machine. 

Run compiler.sh, type in code to stdin, ctrl+D to close stdin and it'll print out the pretty code and the compiled instructions.

Some examples:

a := 5

Result:
PUSH 5
STORE a

begin
a := 1
b := + a 1
end

Result:

PUSH 1
STORE a
LOAD a
PUSH 1
ADD
STORE b

begin
a := 5
b := 0
while a
begin
a := - a 1
b := * a + a b
end
if b
c := 3

d := b
end

Result:

a := 5
b := 0
while a
        a := - a 1
        b := * a + a b

if b
        c := 3
        d := b

PUSH 5
STORE a
PUSH 0
STORE b
LOAD a
BRZ 12
LOAD a
PUSH 1
SUB
STORE a
LOAD a
LOAD a
LOAD b
ADD
MULT
STORE b
JUMP -12
LOAD b
BRZ 4
PUSH 3
STORE c
JUMP 3
LOAD b
STORE d
