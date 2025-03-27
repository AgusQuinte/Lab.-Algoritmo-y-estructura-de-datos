rios = {
    "amazonas": "brasil",
    "parana": "argentina",
    "nilo": "egipto"
}
for key, value in rios.items():
    print(f"El magnifico rio {key} pasa por {value} \n")

for name in rios.keys():
    print(f"Rio {name.title()}\n")

for pais in rios.values():
    print(f"{pais.title()}")
