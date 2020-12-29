up,sim = int(input("Введите высоту ёлки: ")), input("Введите символ для ёлки: ")
for i in range(-1, up*2+1, 2): print('*'*(up*2-i//2), sim*(i+2) '*'*(up*2-i//2))
