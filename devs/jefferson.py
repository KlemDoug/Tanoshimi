#####################################################################
#                           VISÃO CLIENTE
#####################################################################

# fila_cozinha = [
#     {
#         "pedido": "0001",
#         "cliente": "João",
#         "mesa": "01",
#         "status": "📥RECEBIDO"
#     },

#     {
#         "pedido": "0002",
#         "cliente": "Maria",
#         "mesa": "02",
#         "status": "👩‍🍳PREPARANDO"
#     },

#     {
#         "pedido": "0003",
#         "cliente": "Carlos",
#         "mesa": "03",
#         "status": "🔔PRONTO"
#     },

#     {
#         "pedido": "0004",
#         "cliente": "Ana",
#         "mesa": "04",
#         "status": "🍜ENTREGUE"
#     },

#     {
#         "pedido": "0005",
#         "cliente": "Pedro",
#         "mesa": "05",
#         "status": "📥RECEBIDO"
#     },

#     {
#         "pedido": "0006",
#         "cliente": "Juliana",
#         "mesa": "06",
#         "status": "👩‍🍳PREPARANDO"
#     },

#     {
#         "pedido": "0007",
#         "cliente": "Rafael",
#         "mesa": "07",
#         "status": "🔔PRONTO"
#     }
# ]


# def consultar_status_pedido(fila):

#     encontrado = False

#     while encontrado == False:

#         numero_pedido = input("\nDigite o número do seu pedido: ")

#         for pedido in fila:

#             if pedido["pedido"] == numero_pedido:

#                 encontrado = True

#                 print("\n==============================")
#                 print("       STATUS DO PEDIDO")
#                 print("==============================")

#                 print("Número do pedido:", pedido["pedido"])
#                 print("Nome do cliente:", pedido["cliente"])
#                 print("Mesa:", pedido["mesa"])
#                 print("Status:", pedido["status"])

#                 if pedido["status"] == "📥RECEBIDO":
#                     print("Seu pedido foi recebido e está aguardando preparo!⏳")

#                 elif pedido["status"] == "👩‍🍳PREPARANDO":
#                     print("Seu pedido está sendo preparado!😎")

#                 elif pedido["status"] == "🔔PRONTO":
#                     print("Boas notícias😊Seu pedido está pronto e será levado até você!😉")

#                 elif pedido["status"] == "🍜ENTREGUE":
#                     print("Seu pedido já foi entregue!✅")

#         if encontrado == False:
#             print("\nNúmero do pedido não encontrado!😕")
#             print("Por favor, tente novamente.")


# consultar_status_pedido(fila_cozinha)
