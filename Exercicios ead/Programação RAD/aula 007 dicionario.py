contatos = {} #Criamos as listas com colchetes “[“ e “]” e as tuplas com parênteses “(“ e “)”. Os dicionários são criados com chaves “{“ e “}”.
print(contatos)

#inserindo contatos no dicionario
contatos["felix"] = ["1111-1111"]
print(contatos)

#criando lista e atribuindo o valor a ela, e inserimos na chave brito
tel_brito = ['2222-2222',"3333-3333"] 
contatos["brito"] = tel_brito
print(contatos)
#inserindo mais dados
contatos["Piazza"] = ["4444-4444"]
contatos["Carlos Alberto"] = ["5555-5555"]
tel_clodoaldo = ["6666-6666","7777-7777"]
contatos["clodoaldo"] = tel_clodoaldo
#mostrando o resultado
print(contatos)

#Acessando os Dados no dicionario
print('\nimprimindo o contato do felix: {}'.format(contatos["felix"]))

#alterando o contato do felix
contatos["felix"] = ["9999-9999"]
print('\nalterei o contato do felix: {}'.format(contatos["felix"]))

print(contatos.keys()) # identificar as chaves de um dicionario
print(contatos.values()) # identificar os valores de um dicionario


print("Piazza" in contatos) # veirificar se essa chave pertence ao dicionario

print(contatos.items()) #retorna elementos em forma de tuplas

#copiando um dicionario
jogadores =  contatos.copy()
print(jogadores) #temos um dicionario chamado jogadores

contatos.clear() # apagar elementos do dicionario
print(contatos)

