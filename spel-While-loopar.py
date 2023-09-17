#While-loopar
#att skriva meningen så många gånger du vill.
i = 0
end = 20
while i<end:
    print("Hello world")
    i = i+1

#Kontinuerliga frågor tills du bestämmer dig för att sluta.
ans = ""
while ans != "quit":
    ans = input("vad vill du göra? skriv quit för att avsluta")
print("--------------------------------------")
    
#Main-loop för Menyalternativ.
run = True
while run:
    print("vad vill du göra?")
    print("1. Spela golf")
    print("2. Spela dator")
    print("3. Bygg lego")
    print("0. Avsluta")
#print("----------------")
    
#Read input from user
    ans = input("Var god välj: ")
    if not ans.isnumeric():
        print("Tyvärr förstod jag inte vad du ville.")
        print("Ge ett värde mellan 0 till 3")
    elif int(ans) == 0:
        run = False
print("----------------")

#Räknelsett
a = 0
a = a + 1
a += 1
a += 6
a%=5
a**=3
a = a ** 30
