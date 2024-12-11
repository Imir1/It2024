d = int(input())
x = int(input())
a = (365 - (75 / (d*d*d)) / (3 * (d*d) - d)) * 5
b = ((412 - (125 / (d*d*d))) / (2 * (d*d) - d)) * 4
print(((a + b) * x) // 1)
print(a)
print(b)
