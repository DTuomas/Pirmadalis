Pirmas_skaicius = float(input("ivesti pirma skaiciu"))
Antras_skaicius = float(input("ivesti antra skaiciu"))
Matematinis_veiksmas = input("ivesti veiksma")

print("Pirmas skaicius", Pirmas_skaicius)
print("Antras skaicius", Antras_skaicius)
print("Veiksmas", Matematinis_veiksmas)

if(Matematinis_veiksmas == "dalyba"):
    print(Pirmas_skaicius / Antras_skaicius)
if(Matematinis_veiksmas == "daugyba"):
    print(Pirmas_skaicius * Antras_skaicius)
if(Matematinis_veiksmas == "sudetis"):
    print(Pirmas_skaicius + Antras_skaicius)
if(Matematinis_veiksmas == "atimtis"):
    print(Pirmas_skaicius - Antras_skaicius)

    









