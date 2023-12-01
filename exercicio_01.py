class Site:
    def __init__(self, name, vazamentos):
        self.name = name
        self.vazamentos = vazamentos
        self.pontos = 0

    def calcular_pontos(self):
        for vazamento in self.vazamentos:
            if vazamento == "senha":
                self.pontos += 100
            elif vazamento == "email":
                self.pontos += 15
            elif vazamento == "telefone":
                self.pontos += 70
            elif vazamento == "nome":
                self.pontos += 25

vazamentos_sites = [
    Site("instagram", ["senha", "nome"]),
    Site("twitter", ["nome"]),
    Site("facebook", ["senha", "email", "telefone", "nome"])
]

for site in vazamentos_sites:
    site.calcular_pontos()

vazamentos_sites.sort(key=lambda site: site.pontos, reverse=True)

print("Ranking:")
for i, site in enumerate(vazamentos_sites):
    print(f"{i+1}. {site.name}: {site.pontos} pontos")