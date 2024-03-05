l='archana'
it={}
for i in set(l):
    it[i]=l.count(i)
for i,count in it.items():
    print(f"the letter'{i}' occures {count}")

