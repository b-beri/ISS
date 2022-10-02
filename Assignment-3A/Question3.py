l = list()
for i in range(10):
    l += [input("Enter Word/String: "), ]

print("Enter 0 for Ascending Sort, 1 for Descending Sort")
choice = bool(int(input("-> ")))
l.sort(reverse=choice, key=lambda s: s.lower())

print("Sorted Words =>")
for i in l:
    print(i)

l+=[input("Enter a new Word/String: "),]
l.sort(reverse=choice, key=lambda s: s.lower())

print("Newly Sorted Words =>")
for i in l:
    print(i)