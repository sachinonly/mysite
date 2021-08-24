def search_replace(search_text,replace_text,i):
    fin = open("C:\\Users\\sachin-windows\\Heloworld\\files\\search_replace_input.txt", "r")
    fout = open("C:\\Users\\sachin-windows\\Heloworld\\files\\search_replace_output.txt", "wt")

    if i == 0:
        fin = open("C:\\Users\\sachin-windows\\Heloworld\\files\\search_replace_input.txt", "r")
    else:
        fin = open("C:\\Users\\sachin-windows\\Heloworld\\files\\search_replace_output.txt", "r")

    for line in fin:
        fout.write(line.replace(search_text, replace_text))
    #fin.close()
    #fout.close()

kfile = open ("C:\\Users\\sachin-windows\\Heloworld\\files\\search_replace.csv","r")
fin = open("C:\\Users\\sachin-windows\\Heloworld\\files\\search_replace_input.txt", "r")
i =0
for kline in kfile:
    k, v = kline.rstrip().split(',',1)
search_replace(k,v,i)