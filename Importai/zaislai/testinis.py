import geris

kintamasis = "geras pirmadienio rytas"

def atbulai(stringas):
    return stringas[::-1]

print("mano moduliukas sekmingai importuotas ir veikia")

if __name__ == "__main__":
    print("testuojam", kintamasis)
    print(geris.geras)

