print("Hello world! ☺")

# Integer - celo število

x = 10
y = -10

#operacije int-a
print(x + y)
print(x - y)
print(x / y)
print(x * y)

# Celoštevilsko deljenje

print(x//y)
print(x/y)

# deljenje z ostankom

print(x%2)

# potenciranje z **

# tipi

print(type(x))

# Pretvorba tipa (parse)

x = "12"
x = int(x)
print(x)
print(type(x))
print(int(x))

print("[[255,255,255]] " * 10)


print(0.1 + 0.2 == 0.3) #IEEE754 to bi mogl delat ampak IEEE754...

s = [1,2,3]
print(s[0])

#string - nizi znakov
a = "abc"
b = "def"
print(a+b)

#indeksiranje
print(a[0])

#rezine/slice

#s[od:do:korak]
print(a[0:1])
print(a[::-1]) #obrnjen string

#metode string.capatalize, upper, lower, strip...
#len za dolzino
#f-string

ime = "Anja"

print(f"Pozdravljen {ime}")
