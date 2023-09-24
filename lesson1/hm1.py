print("Является ли слово палиндромом?")
UrWord = str(input("Введите слово:"))
OpWord = UrWord[::-1]
if UrWord == OpWord:
  print("True")
else:
  print("False")