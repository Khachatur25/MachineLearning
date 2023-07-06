text = input()
indexes = []

for i,a in enumerate(text):
    if a  == ' ':
        indexes.append(i)

for j in indexes:
    print(j)


