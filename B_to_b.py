print("Sveicināti baitu -> bitu pārveidošanas programmā!")

x=input("Ievadiet B pakāpi (B=1, kB=3, MB=6, GB=9 utt.): ")
x=int(x)
a=10**x
a=int(a)

q=input("Ievadiet B skaitu: ")
q=int(q)

y=input("Ievadiet b pakāpi (b=1, kb=3, Mb=6, Gb=9 utt.): ")
y=int(y)
p=10**y
p=int(p)


r=(a*q*8)/p
r=float(r)

print("Jūsu rezultāts izvēlētajā baitu pakāpē: ", r)
