import time

print("welcome to ShitOS v1.0!")
print("loading...    ")
print("please wait...")
time.sleep(5)
folders=["system", "programs", "files"]
while True:
 command1 = input("print command: ")
 if command1 == "info" : 
  print(" ...........")
  print(" ShitOS v.1.0")
  print("ShitRTX 4090ti")
  print("Shintel core i5-6500")
 if command1 == "data" : 
   print(" ...........")
   for i in folders:
       print(f"folder: {i}")
   itm = input("select: ")
   if itm == "system" :
     print(" ...........")
     print("file: code")
     print("folder: nothing")
     sysdat = input("select: ")
     if sysdat == "code" :
      print("Shit shit shit shit")
   if itm == "programs" :
    print(" ...........")
    print("pys: calculator")
    print("pys: word compilator")
    print("pys: time")
    promdat = input("select: ")
    if promdat == "calculator" :
     print(" ...........")
     a = input("one: ")
     b = input("two: ")
     try:
         a = float(a)
         b = float(b)
         print(a + b)
     except:
         print("Enter valid numbers!")
    elif promdat == "time" :
     print(" ...........")
     t = time.localtime(time.time())
     print("Current time:", time.asctime(t));
    elif promdat == "word compilator":
        print("Notepad-- v.2.1.3. 'exit' to exit.")
        ext = ""
        file = ""
        while ext != "exit":
            ext = input("~ ")
            file += f"{ext}\n"
        print("OK.")
        print("[r]ead, [s]ave, [p]rint, [i]gnore")
        var = input("what to do with this file? ")
        if var == "r" or var == "i":
            pass
        elif var == "s":
            with open(file.split('\n')[0], "w") as f:
                f.write(file)
        elif var == "p":
            print(f"{file}")
        else:
            pass
 elif command1 == "mkdir":
     folders.append(command[6:])
 elif command1 == "exit":
     exit()
    
