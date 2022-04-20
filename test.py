import kea

print(kea.version)

kea.start("""
D off
V var 40
V var2 2
C var var + var2
A var
""")