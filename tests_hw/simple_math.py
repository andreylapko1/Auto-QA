class SimpleMath:

    def square(self, num):
        return num ** 2

    def cube(self, num):
        return num ** 3



a = [1,2,3,4,5]
b = iter(a)
c = iter(a)
c.__next__()
lg = 0
for num1, num2 in zip(b, c):
    print(num1, num2)
    lg += num2 -num1

print(lg)