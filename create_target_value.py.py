##this code creates target value (in machine learning scenario)
##based on each file name entry.

file = []
target = []
flag = 0
tag = []
for a in range(111):
    for d in range(2):
        for p in range(2):
            for c in range(2):
                val = "a" + str(a) + "_d" + str(d) + "_p" + str(p) + "_c" + str(c) + "_color.avi"
                file.append(val)
##print file
if len(file)> 0:
    f = file[0]
  
for f in file:
    for k in f:
        if k == '_':
            break
        if k == 'a':
            continue
        tag.append(k)
    str_tag = ''.join(map(str,tag))   
    target.append(str_tag)
    tag = []
    
##print target

for i in range(len(file)-1):
    print file[i] + " = " + str(target[i])
    

