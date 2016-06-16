def prime_number(n):
   primenumber = [2]
   init  = 3
   count = 1
   while count < n:
      for item in primenumber:
         if init % item == 0:
            break
      else:
         primenumber.append(init)
         init += 2
         count += 1

   return primenumber

print prime_number(3)