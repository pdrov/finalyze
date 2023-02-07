import re


def parse(data):
    indx = [i.start() for i in re.finditer('description', data)]
    summ = []
    for t, i in enumerate(indx):
        j = i + 14
        try:
            while j < indx[t+1]:
                if data[j] != '"':
                    summ.append(data[j])
                else:
                    break
                j += 1

        except Exception as e:
            print(e)
        summ.append("\n")

    return ''.join(summ)

