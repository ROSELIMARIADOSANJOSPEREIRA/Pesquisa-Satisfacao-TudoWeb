# ============================================================
#   TudoWeb - Pesquisa de Satisfação no Atendimento ao Cliente
# ============================================================

# TOTAL_ENTREVISTADOS definido como 10 para o teste de validação solicitado.
# Para a pesquisa real, alterar para 50.
TOTAL_ENTREVISTADOS = 10 

excelente = 0
ruim = 0

print("INÍCIO DA PESQUISA TUDOWEB")

for i in range(TOTAL_ENTREVISTADOS):
    print(f"\nEntrevistado {i + 1}:")
    
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    
    print("Opinião sobre o atendimento: 1-EXCELENTE, 2-BOM, 3-RUIM")
    opiniao = int(input("Sua opinião: "))

    if opiniao == 1:
        excelente = excelente + 1
    elif opiniao == 3:
        ruim = ruim + 1

print("\n" + "="*30)
print("      RESULTADO FINAL")
print("="*30)
print(f"a) Quantidade de respostas 'EXCELENTE': {excelente}")
print(f"b) Quantidade de respostas 'RUIM': {ruim}")