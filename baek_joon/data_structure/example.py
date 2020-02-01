a = []
a.append("a")
print(a)
a.clear()
print(a)
a.append(1)
print(a)

a.insert(0, "first")
print(a)

a.extend(a)
print(a)

a.remove(1)
print(a)
a.pop(0)
print(a)

print(a.index("first"))

a.extend(a)
print(a.count("first"))
a.remove("first")
a.remove("first")

print(a)
for i in range(10):
    a.append(i)
print(a)
a.sort()
print(a)

a.pop()
print(a)

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("dfd")
queue.append("kts")
print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)
