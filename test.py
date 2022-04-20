import kea
from ks.decoupeur import Decoupeur

kea.start("""
D on

F print var
    A var
    S
    E print var

V ext 42
T print ext
""")

# while True:
#     code = input("KS $ ")
#     sortie = Decoupeur(code, 0).start()

#     if sortie != 0:
#         parsed = "\n".join([" ".join(k) for k in sortie])
#         print(f"\n{parsed}\n")

#         kea.start(parsed, 0)