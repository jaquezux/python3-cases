
# Criando classe Filme
class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao


# Criando classe Série
class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas

# Criando objetos
bacurau = Filme("bacurau", 2019, 131)
chihiro = Filme("spirited away", 2001, 125)
watchmen = Filme("watchmen", 2009, 163)
girls = Serie("girls", 2012, 6)
vis = Serie("vis a vis", 2015, 4)

# Imprimindo
print (f'Nome: {bacurau.nome} - Ano: {bacurau.ano} - Duração: {bacurau.duracao} min')
print (f'Nome: {chihiro.nome} - Ano: {chihiro.ano} - Duração: {chihiro.duracao} min')
print (f'Nome: {watchmen.nome} - Ano: {watchmen.ano} - Duração: {watchmen.duracao} min')
print (f'Nome: {girls.nome} - Ano: {girls.ano} - Temporadas: {girls.temporadas}')
print (f'Nome: {vis.nome} - Ano: {vis.ano} - Temporadas: {vis.temporadas}')