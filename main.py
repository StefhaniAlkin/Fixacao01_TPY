# - Atividade de Fixação 1
        
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
print(f'\nAtaques críticos: \n{filtro}')
crit_atk = matriz_danos[filtro]
print(f'\n\nOs ataques críticos foram: {crit_atk}')

#Operação aritmética
apl_debuff = np.add(matriz_danos, debuff)
print(f'\nAtaques debuffados (operação aritmética de soma): \n{apl_debuff}')

crystal_mw = np.array([1000])
buff_cmw = np.add(matriz_danos, crystal_mw)
print(f'\nAtaques buffados (operação aritmética de soma): \n{buff_cmw}')

#Duelo - teste extra
rats = np.array([10000, 10000, 10000, 10000])
duel = np.subtract(rats, buff_cmw)
print(f'\nDuelo contra rato (operação aritmética de subtração): \n{duel}')

#https://github.com/StefhaniAlkin/Fixacao01_TPY
################################################
#Execuções com um arquivo externo
################################################

print("\n###############################")
print("Execuções com arquivos externos")
print("###############################\n")

#Abrindo os arquivos
npcs = np.genfromtxt('npcs.txt', delimiter=',', dtype='int64')
debuff = np.genfromtxt('debuff.txt', delimiter=',', dtype='int64')
pot = np.genfromtxt('potions.txt', delimiter=',', dtype='int64')

#Convertendo para array e dando reshape
npcs_array = np.array(npcs)
print(f'\nArray de Personagens: \n{npcs_array}')

npcs_array_reshaped = np.array(npcs_array).reshape((4,4))
print(f'\nArray reshaped de Personagens: \n{npcs_array_reshaped}')

debuff_array = np.array(debuff)
print(f'\nArray de Debuffs: \n{debuff_array}')

debuff_array_reshaped = np.array(debuff_array).reshape((4,4))
print(f'\nArray reshaped de Debuffs: \n{debuff_array_reshaped}')

pot_array = np.array(pot)
print(f'\nArray de Poções: \n{pot_array}')



#Axis=0:
atk_comb_2 = npcs_array_reshaped.mean(axis=0)
print(f'\nAtaques combinados (axis=0): \n{atk_comb_2}')

#Axis=1
atk_rate_2 = npcs_array_reshaped.mean(axis=1)
print(f'\nMédia de dano por personagem (axis=1): \n{atk_rate_2}')

#Sem Axis
big_dmg_2 = npcs_array_reshaped.sum()
print(f'\nDano total desse combate (sem axis): \n{big_dmg_2}')

#Transposta da matriz
t_damage_2 = npcs_array_reshaped.T
print(f'\nMatriz transposta dos danos: \n{t_damage_2}\n')

#Operação com transposta
atk_debuffed_2 = np.add(t_damage_2, debuff_array_reshaped)
print(f'\nAtaques debuffados (operação com transpose): \n{atk_debuffed_2}\n')

#Produto escalar
solaire_2 = np.array(npcs_array_reshaped[:,0])
hyper_atk_2 = np.dot(solaire_2, pot_array)
print(f'\nSuper ataque (produto escalar): \n{hyper_atk_2}')

produto_escalar_2 = np.dot(npcs_array_reshaped, debuff_array_reshaped)
print(f'\nProduto escalar: \n{produto_escalar_2}')

#Filtro
filtro_2 = npcs_array_reshaped > 200
print(f'\nAtaques que critaram: \n{filtro_2}')
crit_atk_2 = npcs_array_reshaped[filtro_2]
print(f'\nOs ataques que critaram foram: {crit_atk_2}')

#Operação aritmética
apl_debuff_2 = np.add(npcs_array_reshaped, debuff_array_reshaped)
print(f'\nAtaques debuffados (operação aritmética de soma): \n{apl_debuff_2}')


