def e_primo(n):
    index = 1
    primo = 0

    while(index<=n):
        if(n%index==0):
            primo += 1
        index += 1

    if(primo==2):
        return True
    else:
        return False

print(e_primo(1))
# False
print(e_primo(2))
# True