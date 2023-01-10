produktai = {
    'elektronika' : {'produktai' : ['diodai', 'tranzistoriai', 'jutikliai', 'davikliai', 'rezistoriai']},
    'apsvietimas' : {'produktai' : ['led_lemputes', 'led_juostos', 'valdikliai', 'halogenines_lemputes', 'prozektoriai']},
    'maitinimas' : {'produktai' : ['maitinimo_saltiniai', 'transformatoriai', 'itampos_keitikliai', 'ikrovikliai', 'energijos_rezervuarai']}
}
for kategorija, data in produktai.items():
    print(kategorija)
    print(data)
while True :
    kategorija = input('iveskite kategorija: elektronika, apsvietimas arba maitinimas')
    if kategorija == "elektronika":
        print('diodai', 'tranzistoriai', 'jutikliai', 'davikliai', 'rezistoriai'),
    if kategorija == "apsvietimas":
        print('led_lemputes', 'led_juostos', 'valdikliai', 'halogenines_lemputes', 'prozektoriai'),
    if kategorija == "maitinimas":
        print('maitinimo_saltiniai', 'transformatoriai', 'itampos_keitikliai', 'ikrovikliai', 'energijos_rezervuarai')