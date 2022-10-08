def read_file(filename):
    linelist = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            linelist.append(line.strip())
    return linelist

def convert(lines):
    person = None
    Allen_wc = 0
    Viki_wc = 0
    Allen_sticker = 0
    Viki_sticker = 0
    Allen_p = 0
    Viki_p = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker += 1
            elif s[2] == '圖片':
                Allen_p += 1
            else:
                for m in s[2:]:
                    Allen_wc += len(m)

        elif name == 'Viki':
            if s[2] == '貼圖':
                Viki_sticker += 1
            elif s[2] == '圖片':
                Viki_p += 1
            else:
                for m in s[2:]:
                    Viki_wc += len(m)
    print('Allen 說', Allen_wc, '個字，傳了', Allen_sticker, '張貼圖與', Allen_p, '張照片')
    print('Viki說', Viki_wc, '個字，傳了', Viki_sticker, '張貼圖與', Viki_p, '張照片')        
    

def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')



def main():
    lines = read_file('LINE-Viki.txt') #清單list
    lines = convert(lines)  #覆蓋掉原本上一行lines變數的值
    #write_file('output1.csv', lines) #要產生檔案的檔名 與 被從哪個資料寫入
   

main()

