import os

def conv(image_width,image_height,l):
    x1=float(l[0])
    y1=float(l[1])
    x2=float(l[2])
    y2=float(l[3])
    center_x=(x1/image_width)+(abs(x1-x2)/image_width/2)
    center_y=(y1/image_height)+(abs(y1-y2)/image_height/2)
    w=abs(x1-x2)/image_width
    h=abs(y1-y2)/image_height
    return ""+str(center_x)+" "+str(center_y)+" "+str(w)+" "+str(h)
def prepare_labels(p):
    paths=os.listdir(p)
    for path in paths:
        file=open(p+'\\'+path,'r')
        s=file.read()
        s=s.split('\n')
        file.close()
        file=open(p+'\\'+path,'w')
        ss=""
        for i in s:
            if i=='': break
            i=conv(1000,1000,i.split(','))
        
            i='0 '+i+'\n'
            ss=ss+i
        file.write(ss)
        file.close()

        
prepare_labels('TestGroundTruth')