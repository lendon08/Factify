class A:
    def method_a(self, a, b):
        return a + b


class B:
    def method_b(self, a, b):
        return A().method_a(a, b)


b1 = B()

print(b1.method_b(10, 15))  # 👉️ 25
