lst = ['moontasir','raya','programming','lubia']
def name(st):
    count = 0
    for i in st:
        if len(i) >= 5:
            count += 1
    return count
print(name(lst))
