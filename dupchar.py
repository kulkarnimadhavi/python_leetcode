def dupcharremove(str):
 s=set(str)
 t=""
 for i in str:
     if (i in t):
         pass
     else:
         t=t+i
 print(t)

if __name__ == "__main__":
     dupcharremove ('iiaaamlovelovepython')
     # findstring()

