# - Atividade de Fixação 1

#     - Vincular com o github (código deve estar no repositório sem o venv ou outros arquivos de configuração);
        
#         EXTRA (200XP): Os dados devem vir de algum arquivo externo.

import numpy as np

#Array bidimensional

debuff = np.array([[-10, -12, -14, -16],
             [-20, -22, -24, -26],
             [-30, -32, -34, -36],
             [-40, -42, -44, -46]])

# a_random = np.array(np.random.rand(4, 4))
# print(a_random)

print(f'Array bidimensional (debuff):\n {debuff}\n')
# print(f'Dimensão: {a.ndim}')
# print(f'Shape: {a.shape}\n')

#Dados estatísticos com axis

dano_solaire = [150, 80, 250, 40]
dano_artorias = [200, 180, 220, 250]
dano_ornstein_smough = [160, 180, 280, 220]
dano_gwyn = [180, 150, 200, 300]

matriz_danos = np.array([dano_solaire, dano_artorias, dano_ornstein_smough, dano_gwyn])

print('Dados estatísticos com Axis:\n')
print(f'Ataque dos personagens: \n{matriz_danos}')

#Axis=0:
atk_comb = matriz_danos.mean(axis=0)
print(f'\nAtaques combinados (axis=0): \n{atk_comb}')

#Axis=1
atk_rate = matriz_danos.mean(axis=1)
print(f'\nMédia de dano por personagem (axis=1): \n{atk_rate}')

#Sem Axis
big_dmg = matriz_danos.sum()
print(f'\nDano total desse combate (sem axis): \n{big_dmg}')

#Transposta da matriz
t_damage = matriz_danos.T

#Operação com transposta
atk_debuffed = np.add(t_damage, debuff)

print(f'\nMatriz transposta dos danos: \n{t_damage}\n')
print(f'\nAtaques debuffados (operação com transpose): \n{atk_debuffed}\n')

#Produto escalar
solaire = np.array(dano_solaire)
potions = np.array([1, 2, 3, 4])
hyper_atk = np.dot(solaire, potions)
print(f'\nSuper ataque (produto escalar): \n{hyper_atk}')

produto_escalar = np.dot(matriz_danos, debuff)
print(f'\nProduto escalar: \n{produto_escalar}')

#Filtro
filtro = matriz_danos > 200 
crit_atk = matriz_danos[filtro]
print(f'\nAtaques críticos: \n{crit_atk}')

#Operação aritmética
apl_debuff = np.add(matriz_danos, debuff)
print(f'\nAtaques debuffados (operação aritmética de soma): \n{apl_debuff}')

crystal_mw = np.array([1000])
buff_cmw = np.add(matriz_danos, crystal_mw)
print(f'\nAtaques buffados (operação aritmética de soma): \n{buff_cmw}')

#Duelo
rats = np.array([10000, 10000, 10000, 10000])
duel = np.subtract(rats, buff_cmw)
print(f'\nDuelo contra rato (operação aritmética de subtração): \n{duel}')

#https://github.com/StefhaniAlkin/Fixacao01_TPY