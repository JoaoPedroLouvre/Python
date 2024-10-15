number = int(input('Tabuada de: \n'))
begin = int(input('De: \n'))
end = int(input('Até: \n'))

x = begin

while x <= end:
    print(f'Tabuada de {number} x {x} = {number * x}')
    x += 1