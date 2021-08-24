i=1
def search_replace(search_text,replace_text,fileinput,fileoutput):
    fin=open(fileinput,"r")
    fout=open(fileoutput,"w")
    for line in fin:
        fout.write(line.replace(search_text, replace_text))
    fin.close()
    fout.close()

for i in range(1, 4):
    print(i)
    filename_input="C:\\Users\\sachin-windows\\Heloworld\\files\\search_replace_output" + "_"+ str(i) + ".txt"
    filename_output="C:\\Users\\sachin-windows\\Heloworld\\files\\search_replace_output" + "_"+ str(i+1) + ".txt"
    print ("filename:", filename_input, filename_output )
    if i == 1:
        search_replace('create_search','create_replace',filename_input, filename_output)
    elif i == 2:
        search_replace('parallel_search','parallel_replace',filename_input, filename_output)
    elif i ==3:
        search_replace('hint_search','hint_replace',filename_input, filename_output)


