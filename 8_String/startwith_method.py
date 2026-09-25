s="Beautifull"
print(s.startswith("B"))     
print(s.startswith("Bea"))
print(s.startswith("b"))
print(s.startswith("a",2))
print(s.startswith("au",2,5))
print(s.startswith("au",2,3))
print(s.startswith("au",2,4))

print(s.startswith(("B","k","p","l")))
print(s.startswith(("a","l"),2))