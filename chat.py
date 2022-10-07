def read_file(filename):
    linelist = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            linelist.append(line.strip())
    return linelist

def convert(lines):
    newlist = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person: #如果person有值
            newlist.append(person + ': ' + line)
    return newlist 

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')



def main():
    lines = read_file('input.txt') #清單list
    lines = convert(lines)  #覆蓋掉原本上一行lines變數的值
    write_file('output1.csv', lines) #要產生檔案的檔名 與 被從哪個資料寫入
   

main()

