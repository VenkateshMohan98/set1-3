v = input()
aph =['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v''w','x','y','z'] 
vowels=['a','e','i','o','u']
v = v.casefold()
if v in vowels:
  print("Vowel")
elif v in aph:
  print("Consonant")
else:
  print("invalid")
