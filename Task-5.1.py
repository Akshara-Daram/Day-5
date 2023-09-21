stringg=input("Enter an email: ")
if '@' in stringg:
   parts=stringg.split('@')
   if len(parts)==2:
      parts=local_name,domain
      if domain=='Yahoo'in stringg or domain=='google'in stringg or domain=='outlook'in stringg:
         if stringg.endswith('.com'):
           print("Email is valid")
         else:
           print("Email is invalid")
      else:
         print("Email is invalid")
else:
      print("Email is invalid")
    


  












  

    














