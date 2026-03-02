'''

CRUD

Padaria

O sistema da padaria deve permitir o acesso ao menu de produtos e promoções, onde o cliente pode selecionar 
os itens desejados e adiciona-los ao pedido. O sistema deve calcular o valor do pedido de acordo com o valor
do produto selecionado. O sistema deve permitir que o cliente possa finalizar o pedido, e escolher entre a
retirada no estabelecimento ou a entrega. E, então, escolher o método de pagamento, onde o cliente possa escolher entre 
dinheiro, pix, ou cartão de crédito ou débito. O sistema deve confirmar se o pedido chegou ao estabelecimento.

'''

print('Padaria Peter Pão - o melhor pão da cidade!🥞🥐🥖')

nome_gentil = input('Qual é o seu nome?: ')

print(f'Olá, {nome_gentil}! Seja bem-vindo(a) à nossa padaria!')

print("1- Fazer cadastro")
print("2- Ver o cardápio")
print("3- Meus pedidos")
print("4- Informações")
print("0- Sair")


acesso_menu = input("\n O que você quer fazer?: ")

while True:

   if acesso_menu == "1":
       print("Fazer cadastro")


       email_cliente = input("Digite o email:")
       endereço_cliente = input("Digite o endereço")
       telefone_cliente = input("Digite o telefone")

       print("Cadastro realizado com sucesso!")
       #Código para fazer cadastro
       break
   
   elif acesso_menu == "2":
       print("Ver o cardápio")

       input("Exibir cardápio")
       print("1 - Salgados")
       print("2 - Doces")
       print("3 - Bebidas")
       print("4 - Promoções")
       #Código para exibir cardápio
       break

   elif acesso_menu == "3":
       print("Meus pedidos")

    
        #Código para exibir meus pedidos
       break

   elif acesso_menu == "4":
       print("Informações")
    
       print("Informações")
       print("Endereço: Rua dos Pães, 123 - Centro")
       print("Telefone: (11) 1234-5678")
       print("Horário de funcionamento: Segunda a sábado, das 6h às 20h")
        #Código para exibir informações
       break
   elif acesso_menu == "0":
       print("Sair")    
       #Código para sair
       break

    #exemplo de indentação correta para o código acima: