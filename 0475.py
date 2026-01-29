name = "Smit"
print("До функции: " + name)

def name_de(x):
    print("Локальная область видимости: " + x)
    x = x + " Adam"
    print("Попытался менять значение глобальной переменной: " + x)
    
name_de(name)
print("После функции: " + name)