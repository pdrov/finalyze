import re


with open(file='test.txt', mode='r') as f:
    text = f.readline()
indx = [i.start() for i in re.finditer('description', text)]
summ = []
for t, i in enumerate(indx):
    j = i + 14
    try:
        while j < indx[t+1]:
            if text[j] != '"':
                with open(file="summ.txt", mode='a') as f:
                    f.write(text[j])
                summ.append(text[j])
            else:
                break
            j += 1
        with open(file="summ.txt", mode='a') as f:
            f.write("\n")
    except Exception as e:
        print(e)
print(summ)
