a = 5
b = 10
x = True
y = False

print((x or y) and (a < b))         ## = (True) && (True) = True
print((x or y) and not (a < b))     ## = (True) && (!True) = (True) && (False) = False