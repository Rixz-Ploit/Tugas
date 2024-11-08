#c * 9/5 + 32

def far(x, y) :
     return x * y

def far2(x, y) :
    return x + y

bag = 1.8
bag2 = 9 / 5      
tam = 32

c = float(input("Masukan Suhu : "))

t = far(c, bag)
to = far2(t, tam)

print(f"""

Angka Celcius = {c}
Di Kali {bag2} = {far(c, bag)}
Di Tambah {tam} = {far2(t, tam)}
Celcius Ke Farenheit = {to}

""")

