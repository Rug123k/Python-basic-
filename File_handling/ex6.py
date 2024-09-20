# copying Binary files
#      media  - Image        }
#               audio        }-=-=-=- Binary
#               Video        }
f = open ("ex6file.png","rb")
data=f.read()

cp=open("ex6file2.png","wb")

cp.write(data)
f.close
cp.close