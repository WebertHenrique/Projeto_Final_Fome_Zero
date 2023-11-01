# 1. Problema de negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards.

Para acompanhar o crescimento desses negócios, o CEO gostaria de ver as seguintes métricas:

## A visão geral:

	1. Quantos restaurantes únicos estão registrados?
	2. Quantos países únicos estão registrados?
	3. Quantas cidades únicas estão registradas?
	4. Qual o total de avaliações feitas?
	5. Qual o total de tipos de culinária registrados?


## A visão dos Países:

	1. Qual o nome do país que possui mais cidades registradas?
	2. Qual o nome do país que possui mais restaurantes registrados?
	3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
	registrados?
	4. Qual o nome do país que possui a maior quantidade de tipos de culinária
	distintos?
	5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
	6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
	entrega?
	7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
	reservas?
	8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
	registrada?
	9. Qual o nome do país que possui, na média, a maior nota média registrada?
	10. Qual o nome do país que possui, na média, a menor nota média registrada?
	11. Qual a média de preço de um prato para dois por país?


## A visão das cidades:

	1. Qual o nome da cidade que possui mais restaurantes registrados?
	2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
	4?
	3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
	2.5?
	4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
	5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
	distintas?
	6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
	reservas?
	7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
	entregas?
	8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
	aceitam pedidos online?

## A visão dos restaurantes:

	1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
	2. Qual o nome do restaurante com a maior nota média?
	3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
	pessoas?
	4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
	média de avaliação?
	5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
	possui a maior média de avaliação?
	6. Os restaurantes que aceitam pedido online são também, na média, os
	restaurantes que mais possuem avaliações registradas?
	7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
	possuem o maior valor médio de um prato para duas pessoas?
	8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
	possuem um valor médio de prato para duas pessoas maior que as churrascarias
	americanas (BBQ)?

## A visão por tipo de culinária:

	1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
	restaurante com a maior média de avaliação?
	2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
	restaurante com a menor média de avaliação?
	3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
	restaurante com a maior média de avaliação?
	4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
	restaurante com a menor média de avaliação?
	5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
	restaurante com a maior média de avaliação?
	6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
	restaurante com a menor média de avaliação?
	7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
	restaurante com a maior média de avaliação?
	8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
	restaurante com a menor média de avaliação?
	9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
	restaurante com a maior média de avaliação?
	10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
	restaurante com a menor média de avaliação?
	11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
	pessoas?
	12. Qual o tipo de culinária que possui a maior nota média?
	13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
	online e fazem entregas?

# 2. Premissas assumidas para a análise

	1. Marketplace foi o modelo de negócio assumido.
	2. Marketplace foi o modelo de negócio assumido.
	3. As principais visões do negócio foram: Visão Geral, Visão Países, Visão Cidades, Visão Restaurantes e Visão Culinária.

# 3. Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem
as 3 principais visões do modelo de negócio da empresa:

	1. Visão geral
	2. Visão países
	3. Visão cidades
	4. Visão Restaurantes e Culinária

Cada visão é representada pelo seguinte conjunto de métricas.

1. Visão geral

	Quantidade de restaurantes, países, cidades cadastradas; 
	Quantidade de diferentes culinárias;
	Quantidade de avaliações feitas na plataforma;
	Mapa com a localização dos restaurantes.

2. Visão países

	Quantidade de restaurantes registrados por país;
	Quantidade de cidades registradas por país;
	Média de avaliação feitas por país;
	Média de preço de um prato pra duas pessoas por país.

3. Visão cidades

	Top 10 cidades com mais restaurantes na base de dados;
	Top 7 cidades com restaurantes com média de avaliação acima de 4;
	Top 7 cidades com restaurantes com média de avaliação abaixo de 2.5;
	Top 10 cidades com mais restaurantes com tipos culinários distintos.

4. Visão Restaurantes e Culinária

	Melhores restaurantes dos principais tipos culinários;
	Top 10 restaurantes
	Top 10 melhores tipos de culinárias
	Top 10 piores tipos de culinárias


# 4. Top 3 Insights de dados

	1. A Índia é o país com a maior quantidade de restaurantes e cidades cadastrados
	2. A Inglaterra possui 4 restaurantes no Top 10 restaurantes mais bem avaliados.
	3. A Inglaterra seguida do Estados Unidos possuem mais restaurantes com tipos de culinárias distintos.

# 5. O produto final do projeto

Painel online, hospedado em um Cloud e disponível para acesso em
qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link: https://projeto-final-fome-zero.streamlit.app

# 6. Conclusão

O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que
exibam essas métricas da melhor forma possível para o CEO.


# 7. Próximo passos

	1. Melhorar o mapa e os gráficos.
	2. Criar novos filtros.
	3. Adicionar novas informações nas visões de negócio.
