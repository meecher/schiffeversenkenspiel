
matchfield_visual = [[0]*10 for i in range (10)]
#stringconv = [str(int) for int in matchfield_visual]
#stringconv2 = [str(int) for int in stringconv]
#stringli = ''.join(stringconv2)

for row in matchfield_visual:
    string_ints = [str(int) for  int in row]
    stringli = ' '.join(string_ints)
    print(stringli)

