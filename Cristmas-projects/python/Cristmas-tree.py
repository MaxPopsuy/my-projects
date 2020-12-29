import sys

height = int(input("Введите высоту: ")) 
if height < 5:
    error_code = "Incorrect height of tree, min height is >5 or =5"
    sys.exit(error_code)

background_symbol = str(input("Введите символ фона: "))
fir_tree_symbol = str(input("Введите символ ёлки: "))
z = height - 3
x = 1    

for i in range(height, 0, -1):
    print(background_symbol * (i - 1), end="") # print bgsymbol until end
    print(fir_tree_symbol * (((height - i) *2) + 1), end="") # print fir-tree
    print(background_symbol * (i - 1)) # print bgsymbol after fir-tree until end

print("Merry Xmass!") # MERRY XMASS!!! xD




