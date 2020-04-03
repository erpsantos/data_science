# Pos-Datascience
# Observação, estava usando o atlas e o mesmo possui limitações relacionas a clausula where quando utilizado para testes

# Exercicios de MongoDB

# Exercício 1- Aquecendo com os pets

1. Adicione outro Peixe e um Hamster com nome Frodo
- db.pets.insert({name:"Frodo",species:"Peixe"})
  WriteResult({ "nInserted" : 1 })

- db.pets.insert({name:"Frodo",species:"Hamster"})
  WriteResult({ "nInserted" : 1 })

2. Faça uma contagem dos pets na coleção
- db.pets.find({}).count()
  8 Registros

3. Retorne apenas um elemento o método prático possível
- db.pets.findOne({})
 {
        "_id" : ObjectId("5e8741ab0541618f856c69ef"),
        "name" : "Mike",
        "species" : "Hamster"
 }

4. Identifique o ID para o Gato Kilha.
- db.pets.find({name:'Kilha', species:'Gato'}, {_id: 1})
  { "_id" : ObjectId("5e8741ac0541618f856c69f1") }

5. Faça uma busca pelo ID e traga o Hamster Mike
- db.pets.find({"_id" : ObjectId("5e8741ab0541618f856c69ef")})
  { "_id" : ObjectId("5e8741ab0541618f856c69ef"), "name" : "Mike", "species" : "Hamster" }

6. Use o find para trazer todos os Hamsters
- db.pets.find({species:'Hamster'})
  { "_id" : ObjectId("5e8741ab0541618f856c69ef"), "name" : "Mike", "species" : "Hamster" }
  { "_id" : ObjectId("5e8742160541618f856c69f6"), "name" : "Frodo", "species" : "Hamster" }

7. Use o find para listar todos os pets com nome Mike
- db.pets.find({name:'Mike'})
  { "_id" : ObjectId("5e8741ab0541618f856c69ef"), "name" : "Mike", "species" : "Hamster" }
  { "_id" : ObjectId("5e8741ad0541618f856c69f2"), "name" : "Mike", "species" : "Cachorro" }

8. Liste apenas o documento que é um Cachorro chamado Mike
- db.pets.find({name:'Mike', species: 'Cachorro'})
  { "_id" : ObjectId("5e8741ad0541618f856c69f2"), "name" : "Mike", "species" : "Cachorro" }


# Exercício 2 – Mama mia!

1. Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode usar um count para indicar a quantidade.
- db.italians.find({age:99}).count()
  0

2. Identifique quantas pessoas são elegíveis atendimento prioritário (pessoas com mais de 65 anos)
- db.italians.find({age: {"$gt":65}}).count()
  1748
  
3. Identifique todos os jovens (pessoas entre 12 a 18 anos).
- db.italians.find({age: {"$gte":12, "$lte":18}})
  { "_id" : ObjectId("5e87567c9550aecd6dad001d"), "firstname" : "Martina", "surname" : "Battaglia", "username" : "user103", "age" : 15, "email" : "Martina.Battaglia@yahoo.com", "bloodType" : "B-", "id_num" : "826588158863", "registerDate" : ISODate("2009-11-12T04:05:00.050Z"), "ticketNumber" : 7958, "jobs" : [ "Ciência da Computação", "Serviço Social" ], "favFruits" : [ "Kiwi", "Mamão" ], "movies" : [ { "title" : "Gladiador (2000)", "rating" : 2.32 } ], "cat" : { "name" : "Alberto", "age" : 3 } }
  { "_id" : ObjectId("5e87567c9550aecd6dad001e"), "firstname" : "Matteo", "surname" : "D’Angelo", "username" : "user104", "age" : 12, "email" : "Matteo.D’Angelo@hotmail.com", "bloodType" : "A-", "id_num" : "831844762038", "registerDate" : ISODate("2019-08-23T05:42:35.492Z"), "ticketNumber" : 3021, "jobs" : [ "Engenharia Florestal" ], "favFruits" : [ "Laranja", "Goiaba", "Banana" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 4.22 } ], "father" : { "firstname" : "Emanuela", "surname" : "D’Angelo", "age" : 46 } }
  { "_id" : ObjectId("5e87567d9550aecd6dad0026"), "firstname" : "Massimo", "surname" : "Bernardi", "username" : "user112", "age" : 16, "email" : "Massimo.Bernardi@hotmail.com", "bloodType" : "A-", "id_num" : "343016831365", "registerDate" : ISODate("2009-09-08T01:56:33.944Z"), "ticketNumber" : 9504, "jobs" : [ "Aquicultura" ], "favFruits" : [ "Maçã", "Laranja", "Banana" ], "movies" : [ { "title" : "O Resgate do Soldado Ryan (1998)", "rating" : 0.24 }, { "title" : "Um Sonho de Liberdade (1994)", "rating" : 2.31 }, { "title" : "Matrix (1999)", "rating" : 0.27 }, { "title" : "Vingadores: Ultimato (2019)", "rating" : 4.49 } ], "cat" : { "name" : "Elisabetta", "age" : 17 } }
  (Muitos mais registros - colei os primeiros três resultados)

4. Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas não tem nenhum dos dois
- db.italians.find({dog: {$exists: true}}).count()
  4092
  
- db.italians.find({cat: {$exists: true}}).count()
  6015
  
- db.italians.find({cat: {$exists: false}, dog: {$exists: false}}).count()
  2292
  
5. Liste/Conte todas as pessoas acima de 60 anos que tenham gato 
- db.italians.find({age: {'$gt': 60}, cat: {$exists: true}}).count()
  1441
  
6. Liste/Conte todos os jovens com cachorro
- db.italians.find({age: {'$gte': 12, '$lte': 18}, dog: {$exists: true}}).count()
  361
  
#7. Utilizando o $where, liste todas as pessoas que tem gato e cachorro
- db.italians.find({$where: "this.dog && this.cat"})
Error: error: {
	"ok" : 0,
	"errmsg" : "querying oplog with an ns other than a string is not supported in this atlas tier",
	"code" : 8000,
	"codeName" : "AtlasError"
}
(O comando acredito que esteja ok, mas o atlas possui uma limitação em sua versão free (https://jira.mongodb.org/browse/DOCS-10049))

#8. Liste todas as pessoas mais novas que seus respectivos gatos.
- db.italians.find({$where: "this.cat && this.age < this.cat.age"})
Error: error: {
	"ok" : 0,
	"errmsg" : "querying oplog with an ns other than a string is not supported in this atlas tier",
	"code" : 8000,
	"codeName" : "AtlasError"
}
(O comando acredito que esteja ok, mas o atlas possui uma limitação em sua versão free (https://jira.mongodb.org/browse/DOCS-10049))

#9. Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou cachorro)
- db.italians.find({$where: "(this.dog && this.firstname == this.dog.name) || (this.cat && this.firstname == this.cat.name)"})
Error: error: {
	"ok" : 0,
	"errmsg" : "querying oplog with an ns other than a string is not supported in this atlas tier",
	"code" : 8000,
	"codeName" : "AtlasError"
}
(O comando acredito que esteja ok, mas o atlas possui uma limitação em sua versão free (https://jira.mongodb.org/browse/DOCS-10049))

10. Projete apenas o nome e sobrenome das pessoas com tipo de sangue de fator RH negativo
- db.italians.find({bloodType: /-/}, {firstname: true, surname: true})
{ "_id" : ObjectId("5e87567b9550aecd6dad001a"), "firstname" : "Gianluca", "surname" : "Ferrara" }
{ "_id" : ObjectId("5e87567c9550aecd6dad001d"), "firstname" : "Martina", "surname" : "Battaglia" }
{ "_id" : ObjectId("5e87567c9550aecd6dad001e"), "firstname" : "Matteo", "surname" : "D’Angelo" }
{ "_id" : ObjectId("5e87567c9550aecd6dad001f"), "firstname" : "Angela", "surname" : "Vitali" }
{ "_id" : ObjectId("5e87567c9550aecd6dad0020"), "firstname" : "Serena", "surname" : "Carbone" }
{ "_id" : ObjectId("5e87567d9550aecd6dad0022"), "firstname" : "Manuela", "surname" : "Grassi" }
{ "_id" : ObjectId("5e87567d9550aecd6dad0023"), "firstname" : "Alessia", "surname" : "Monti" }
{ "_id" : ObjectId("5e87567d9550aecd6dad0026"), "firstname" : "Massimo", "surname" : "Bernardi" }
{ "_id" : ObjectId("5e87567e9550aecd6dad002a"), "firstname" : "Stefania", "surname" : "Caruso" }
{ "_id" : ObjectId("5e87567e9550aecd6dad002c"), "firstname" : "Tiziana", "surname" : "Martinelli" }
{ "_id" : ObjectId("5e87567f9550aecd6dad002e"), "firstname" : "Tiziana", "surname" : "Negri" }
{ "_id" : ObjectId("5e87567f9550aecd6dad0030"), "firstname" : "Gianluca", "surname" : "Coppola" }
{ "_id" : ObjectId("5e87567f9550aecd6dad0032"), "firstname" : "Marco", "surname" : "Ferrara" }
{ "_id" : ObjectId("5e8756809550aecd6dad0034"), "firstname" : "Teresa", "surname" : "Giordano" }
{ "_id" : ObjectId("5e8756809550aecd6dad0035"), "firstname" : "Elisa", "surname" : "Serra" }
{ "_id" : ObjectId("5e8756809550aecd6dad0036"), "firstname" : "Mirko", "surname" : "Greco" }
{ "_id" : ObjectId("5e8756809550aecd6dad0037"), "firstname" : "Laura", "surname" : "Bruno" }
{ "_id" : ObjectId("5e8756809550aecd6dad0038"), "firstname" : "Raffaele", "surname" : "Benedetti" }
{ "_id" : ObjectId("5e8756819550aecd6dad0039"), "firstname" : "Alessio", "surname" : "Costa" }
{ "_id" : ObjectId("5e8756819550aecd6dad003a"), "firstname" : "Barbara", "surname" : "Bianco" }

11. Projete apenas os animais dos italianos. Devem ser listados os animais com nome e idade. Não mostre o identificado do mongo (ObjectId)
- db.italians.find({}, {_id: false, cat: true, dog: true})
{ "dog" : { "name" : "Emanuela", "age" : 17 } }
{ "cat" : { "name" : "Paola", "age" : 2 } }
{  }
(Muitos mais registros - listei os três primeiros)

12. Quais são as 5 pessoas mais velhas com sobrenome Rossi?
- db.italians.find({surname: 'Rossi'}).sort({age:-1}).limit(5)
{ "_id" : ObjectId("5e87584f9550aecd6dad0af0"), "firstname" : "Daniela", "surname" : "Rossi", "username" : "user2874", "age" : 79, "email" : "Daniela.Rossi@outlook.com", "bloodType" : "O+", "id_num" : "864253666334", "registerDate" : ISODate("2013-08-13T10:15:07.028Z"), "ticketNumber" : 4438, "jobs" : [ "História da Arte" ], "favFruits" : [ "Uva", "Mamão", "Pêssego" ], "movies" : [ { "title" : "Batman: O Cavaleiro das Trevas (2008)", "rating" : 0.42 }, { "title" : "Guerra nas Estrelas (1977)", "rating" : 3.34 }, { "title" : "Seven: Os Sete Crimes Capitais (1995)", "rating" : 3.53 }, { "title" : "Harakiri (1962)", "rating" : 1.86 } ], "cat" : { "name" : "Alessandra", "age" : 4 } }
{ "_id" : ObjectId("5e8758979550aecd6dad0ca4"), "firstname" : "Patrizia", "surname" : "Rossi", "username" : "user3310", "age" : 79, "email" : "Patrizia.Rossi@uol.com.br", "bloodType" : "AB+", "id_num" : "710686522313", "registerDate" : ISODate("2019-05-22T01:38:20.679Z"), "ticketNumber" : 2598, "jobs" : [ "Sistemas Embarcados", "Relações Públicas" ], "favFruits" : [ "Tangerina", "Kiwi" ], "movies" : [ { "title" : "Coringa (2019)", "rating" : 3.3 }, { "title" : "À Espera de um Milagre (1999)", "rating" : 0.78 } ], "father" : { "firstname" : "Carlo", "surname" : "Rossi", "age" : 97 }, "cat" : { "name" : "Veronica", "age" : 8 } }
{ "_id" : ObjectId("5e8759179550aecd6dad0f97"), "firstname" : "Angelo", "surname" : "Rossi", "username" : "user4065", "age" : 78, "email" : "Angelo.Rossi@hotmail.com", "bloodType" : "O-", "id_num" : "656654140283", "registerDate" : ISODate("2013-06-03T07:53:59.548Z"), "ticketNumber" : 2581, "jobs" : [ "História", "Psicopedagogia" ], "favFruits" : [ "Mamão" ], "movies" : [ { "title" : "O Resgate do Soldado Ryan (1998)", "rating" : 0.42 }, { "title" : "A Vida é Bela (1997)", "rating" : 3.62 }, { "title" : "Vingadores: Ultimato (2019)", "rating" : 4.95 }, { "title" : "Vingadores: Ultimato (2019)", "rating" : 1.27 } ] }
{ "_id" : ObjectId("5e8759b19550aecd6dad1330"), "firstname" : "Enrico", "surname" : "Rossi", "username" : "user4986", "age" : 78, "email" : "Enrico.Rossi@live.com", "bloodType" : "O+", "id_num" : "752145352221", "registerDate" : ISODate("2016-06-08T02:10:51.099Z"), "ticketNumber" : 3594, "jobs" : [ "Biomedicina", "Artes e Design" ], "favFruits" : [ "Melancia", "Melancia" ], "movies" : [ { "title" : "12 Homens e uma Sentença (1957)", "rating" : 0.06 }, { "title" : "O Senhor dos Anéis: As Duas Torres (2002)", "rating" : 4.56 }, { "title" : "A Vida é Bela (1997)", "rating" : 2.83 } ] }
{ "_id" : ObjectId("5e8756ea9550aecd6dad02a6"), "firstname" : "Teresa", "surname" : "Rossi", "username" : "user752", "age" : 77, "email" : "Teresa.Rossi@yahoo.com", "bloodType" : "O-", "id_num" : "008062361524", "registerDate" : ISODate("2019-07-11T01:54:53.519Z"), "ticketNumber" : 3207, "jobs" : [ "Engenharia Industrial Madeireira", "Silvicultura" ], "favFruits" : [ "Mamão", "Maçã", "Mamão" ], "movies" : [ { "title" : "1917 (2019)", "rating" : 4.4 }, { "title" : "A Viagem de Chihiro (2001)", "rating" : 4.67 }, { "title" : "O Senhor dos Anéis: As Duas Torres (2002)", "rating" : 3.44 }, { "title" : "A Vida é Bela (1997)", "rating" : 4.88 }, { "title" : "Intocáveis (2011)", "rating" : 0.4 } ], "cat" : { "name" : "Stefania", "age" : 16 } }

13. Crie um italiano que tenha um leão como animal de estimação. Associe um nome e idade ao bichano
- db.italians.insert({firstname: "Antonio", lion: {name: "Simba", age: 8}})
  WriteResult({ "nInserted" : 1 })

#14. Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.
- db.italians.remove({_id: ObjectId("5e7a5366b9ae8f804196449e")})
Error: error: {
	"ok" : 0,
	"errmsg" : "querying oplog with an ns other than a string is not supported in this atlas tier",
	"code" : 8000,
	"codeName" : "AtlasError"
}
(O comando acredito que esteja ok, mas o atlas possui uma limitação em sua versão free (https://jira.mongodb.org/browse/DOCS-10049))

#15. Passou um ano. Atualize a idade de todos os italianos e dos bichanos em 1.
- db.italians.update({}, {"$inc": {"age":1}}, {multi: true})
  WriteResult({ "nMatched" : 10001, "nUpserted" : 0, "nModified" : 10001 }) 
- db.italians.update({$where: "this.cat"}, {"$inc": {"cat.age":1}}, {multi: true})
- db.italians.update({$where: "this.dog"}, {"$inc": {"dog.age":1}}, {multi: true})
Error: error: {
	"ok" : 0,
	"errmsg" : "querying oplog with an ns other than a string is not supported in this atlas tier",
	"code" : 8000,
	"codeName" : "AtlasError"
}
(O comando acredito que esteja ok, mas o atlas possui uma limitação em sua versão free (https://jira.mongodb.org/browse/DOCS-10049))

16. O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas somente com gatos e de 66 anos. Remova esses italianos.
- db.italians.remove({age: 66, $where: "this.cat"})
  WriteResult({ "nRemoved" : 77 })

17. Utilizando o framework agregate, liste apenas as pessoas com nomes iguais a sua respectiva mãe e que tenha gato ou cachorro.
- db.italians.aggregate([{$match: { mother: {$exists: 1} }}, {$project: { firstname: 1, mother: 1, isEqual: { $cmp: ["$firstname", "$mother.firstname"]} }}, {$match: {"isEqual": 0}}])
{ "_id" : ObjectId("5e8756909550aecd6dad0092"), "firstname" : "Cristina", "mother" : { "firstname" : "Cristina", "surname" : "Montanari", "age" : 72 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e8757969550aecd6dad069d"), "firstname" : "Lucia", "mother" : { "firstname" : "Lucia", "surname" : "Cattaneo", "age" : 74 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e8758399550aecd6dad0a6d"), "firstname" : "Riccardo", "mother" : { "firstname" : "Riccardo", "surname" : "Lombardi", "age" : 61 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e8759289550aecd6dad0ff8"), "firstname" : "Mattia", "mother" : { "firstname" : "Mattia", "surname" : "Fiore", "age" : 81 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e87597c9550aecd6dad11f0"), "firstname" : "Marco", "mother" : { "firstname" : "Marco", "surname" : "Donati", "age" : 94 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e8759a29550aecd6dad12d6"), "firstname" : "Federico", "mother" : { "firstname" : "Federico", "surname" : "Gatti", "age" : 77 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e875a159550aecd6dad1587"), "firstname" : "Cristian", "mother" : { "firstname" : "Cristian", "surname" : "Bruno", "age" : 56 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e875b2f9550aecd6dad1c29"), "firstname" : "Sara", "mother" : { "firstname" : "Sara", "surname" : "De Rosa", "age" : 62 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e875ba89550aecd6dad1f00"), "firstname" : "Pasquale", "mother" : { "firstname" : "Pasquale", "surname" : "Parisi", "age" : 27 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e875c3b9550aecd6dad2261"), "firstname" : "Mattia", "mother" : { "firstname" : "Mattia", "surname" : "Valentini", "age" : 75 }, "isEqual" : 0 }
{ "_id" : ObjectId("5e875c849550aecd6dad23d3"), "firstname" : "Emanuela", "mother" : { "firstname" : "Emanuela", "surname" : "Neri", "age" : 38 }, "isEqual" : 0 }

18. Utilizando aggregate framework, faça uma lista de nomes única de nomes. Faça isso usando apenas o primeiro nome
- db.italians.aggregate({$group: {_id: "$firstname"}})
{ "_id" : "Giovanna" }
{ "_id" : "Davide" }
{ "_id" : "Paola" }
(Muitos registros - Listando os 3 primeiros)

19. Agora faça a mesma lista do item acima, considerando nome completo.
- db.italians.aggregate({$group: {_id: {name:"$firstname", surname: "$surname"}}})
{ "_id" : { "name" : "Enrico", "surname" : "Bianchi" } }
{ "_id" : { "name" : "Federica", "surname" : "Ruggiero" } }
{ "_id" : { "name" : "Pasquale", "surname" : "Esposito" } }
(Muitos registros - Listando os 3 primeiros)

#20. Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato, mais de 20 e menos de 60 anos.
- db.italians.find({age: {$gt: 20, $lt: 60}, favFruits: {$all: ["Banana", "Maçã"]}, $where: "this.cat" || "this.dog"})
Error: error: {
	"ok" : 0,
	"errmsg" : "querying oplog with an ns other than a string is not supported in this atlas tier",
	"code" : 8000,
	"codeName" : "AtlasError"
}
(O comando acredito que esteja ok, mas o atlas possui uma limitação em sua versão free (https://jira.mongodb.org/browse/DOCS-10049))

# Exercício 3 - Stockbrokers

1. Liste as ações com profit acima de 0.5 (limite a 10 o resultado)
- db.stocks.find({"Profit Margin": {$gt: 0.5}}).limit(10)
{ "_id" : ObjectId("52853800bb1177ca391c180f"), "Ticker" : "AB", "Profit Margin" : 0.896, "Institutional Ownership" : 0.368, "EPS growth past 5 years" : -0.348, "Total Debt/Equity" : 0, "Return on Assets" : 0.086, "Sector" : "Financial", "P/S" : 13.25, "Change from Open" : 0.0047, "Performance (YTD)" : 0.3227, "Performance (Week)" : -0.0302, "Insider Transactions" : 0.5973, "P/B" : 1.4, "EPS growth quarter over quarter" : 2.391, "Payout Ratio" : 1.75, "Performance (Quarter)" : 0.0929, "Forward P/E" : 12.58, "P/E" : 15.82, "200-Day Simple Moving Average" : 0.0159, "Shares Outstanding" : 92.26, "Earnings Date" : ISODate("2013-10-24T12:30:00Z"), "52-Week High" : -0.1859, "Change" : -0.0009, "Analyst Recom" : 3, "Volatility (Week)" : 0.0264, "Country" : "USA", "Return on Equity" : 0.087, "50-Day Low" : 0.123, "Price" : 21.5, "50-Day High" : -0.0574, "Return on Investment" : 0.033, "Shares Float" : 86.66, "Dividend Yield" : 0.0743, "EPS growth next 5 years" : 0.08, "Industry" : "Asset Management", "Beta" : 1.63, "Operating Margin" : 1, "EPS (ttm)" : 1.36, "PEG" : 1.98, "Float Short" : 0.0253, "52-Week Low" : 0.4687, "Average True Range" : 0.59, "EPS growth next year" : 0.0654, "Sales growth past 5 years" : -0.298, "Company" : "AllianceBernstein Holding L.P.", "Gap" : -0.0056, "Relative Volume" : 0.63, "Volatility (Month)" : 0.0298, "Market Cap" : 1985.39, "Volume" : 199677, "Short Ratio" : 6.3, "Performance (Half Year)" : -0.1159, "Relative Strength Index (14)" : 50.05, "Insider Ownership" : 0.002, "20-Day Simple Moving Average" : -0.007, "Performance (Month)" : 0.0847, "P/Free Cash Flow" : 93.21, "Institutional Transactions" : 0.0818, "Performance (Year)" : 0.3884, "LT Debt/Equity" : 0, "Average Volume" : 348.08, "EPS growth this year" : 1.567, "50-Day Simple Moving Average" : 0.0458 }
{ "_id" : ObjectId("52853801bb1177ca391c1895"), "Ticker" : "AGNC", "Profit Margin" : 0.972, "Institutional Ownership" : 0.481, "EPS growth past 5 years" : -0.0107, "Total Debt/Equity" : 8.56, "Return on Assets" : 0.022, "Sector" : "Financial", "P/S" : 3.77, "Change from Open" : 0.0102, "Performance (YTD)" : -0.1652, "Performance (Week)" : -0.017, "Insider Transactions" : 0.4931, "P/B" : 0.86, "EPS growth quarter over quarter" : -8.2, "Payout Ratio" : 0.79, "Performance (Quarter)" : -0.0083, "Forward P/E" : 7.64, "P/E" : 3.68, "200-Day Simple Moving Average" : -0.1282, "Shares Outstanding" : 390.6, "Earnings Date" : ISODate("2013-10-28T20:30:00Z"), "52-Week High" : -0.2938, "P/Cash" : 3.93, "Change" : 0.0131, "Analyst Recom" : 2.6, "Volatility (Week)" : 0.0268, "Country" : "USA", "Return on Equity" : 0.205, "50-Day Low" : 0.0695, "Price" : 21.71, "50-Day High" : -0.1066, "Return on Investment" : 0.015, "Shares Float" : 383.97, "Dividend Yield" : 0.1493, "EPS growth next 5 years" : 0.035, "Industry" : "REIT - Residential", "Beta" : 0.51, "Sales growth quarter over quarter" : 0.073, "Operating Margin" : 0.67, "EPS (ttm)" : 5.82, "PEG" : 1.05, "Float Short" : 0.0311, "52-Week Low" : 0.1117, "Average True Range" : 0.52, "EPS growth next year" : -0.3603, "Company" : "American Capital Agency Corp.", "Gap" : 0.0028, "Relative Volume" : 0.71, "Volatility (Month)" : 0.02, "Market Cap" : 8370.56, "Volume" : 4576064, "Gross Margin" : 0.746, "Short Ratio" : 1.69, "Performance (Half Year)" : -0.2136, "Relative Strength Index (14)" : 43.53, "Insider Ownership" : 0.003, "20-Day Simple Moving Average" : -0.0318, "Performance (Month)" : -0.042, "Institutional Transactions" : 0.0077, "Performance (Year)" : -0.1503, "LT Debt/Equity" : 0, "Average Volume" : 7072.83, "EPS growth this year" : -0.169, "50-Day Simple Moving Average" : -0.0376 }
{ "_id" : ObjectId("52853801bb1177ca391c1950"), "Ticker" : "ARCC", "Profit Margin" : 0.654, "Institutional Ownership" : 0.513, "EPS growth past 5 years" : 0.105, "Total Debt/Equity" : 0.59, "Return on Assets" : 0.08, "Sector" : "Financial", "P/S" : 5.87, "Change from Open" : 0.0105, "Performance (YTD)" : 0.0805, "Performance (Week)" : 0.0023, "P/B" : 1.08, "EPS growth quarter over quarter" : 0.22, "Payout Ratio" : 0.714, "Performance (Quarter)" : 0.0548, "Forward P/E" : 10.69, "P/E" : 8.32, "200-Day Simple Moving Average" : 0.046, "Shares Outstanding" : 266.17, "Earnings Date" : ISODate("2013-11-05T13:30:00Z"), "52-Week High" : -0.0014, "P/Cash" : 46.93, "Change" : 0.0082, "Analyst Recom" : 2, "Volatility (Week)" : 0.0129, "Country" : "USA", "Return on Equity" : 0.13, "50-Day Low" : 0.0527, "Price" : 17.86, "50-Day High" : -0.0014, "Return on Investment" : 0.056, "Shares Float" : 279.11, "Dividend Yield" : 0.0858, "EPS growth next 5 years" : 0.08, "Industry" : "Diversified Investments", "Beta" : 1.62, "Sales growth quarter over quarter" : 0.16, "Operating Margin" : 0.485, "EPS (ttm)" : 2.13, "PEG" : 1.04, "Float Short" : 0.0146, "52-Week Low" : 0.2192, "Average True Range" : 0.21, "EPS growth next year" : 0.0209, "Sales growth past 5 years" : 0.317, "Company" : "Ares Capital Corporation", "Gap" : -0.0023, "Relative Volume" : 0.68, "Volatility (Month)" : 0.0109, "Market Cap" : 4716.6, "Volume" : 938330, "Gross Margin" : 0.528, "Short Ratio" : 2.68, "Performance (Half Year)" : 0.0267, "Relative Strength Index (14)" : 61.2, "20-Day Simple Moving Average" : 0.0211, "Performance (Month)" : 0.0381, "Institutional Transactions" : 0.0183, "Performance (Year)" : 0.1574, "LT Debt/Equity" : 0, "Average Volume" : 1522.64, "EPS growth this year" : 0.417, "50-Day Simple Moving Average" : 0.0272 }
{ "_id" : ObjectId("52853801bb1177ca391c195a"), "Ticker" : "ARI", "Profit Margin" : 0.576, "Institutional Ownership" : 0.631, "EPS growth past 5 years" : 0.1829, "Total Debt/Equity" : 0.28, "Return on Assets" : 0.046, "Sector" : "Financial", "P/S" : 9.35, "Change from Open" : 0.0214, "Performance (YTD)" : 0.0803, "Performance (Week)" : -0.0055, "Insider Transactions" : -0.0353, "P/B" : 0.89, "EPS growth quarter over quarter" : -0.413, "Payout Ratio" : 1.159, "Performance (Quarter)" : 0.0861, "Forward P/E" : 9.57, "P/E" : 11.88, "200-Day Simple Moving Average" : 0.0497, "Shares Outstanding" : 37.37, "Earnings Date" : ISODate("2013-11-04T21:30:00Z"), "52-Week High" : -0.0404, "P/Cash" : 3.88, "Change" : 0.024, "Analyst Recom" : 2.1, "Volatility (Week)" : 0.0135, "Country" : "USA", "Return on Equity" : 0.064, "50-Day Low" : 0.1598, "Price" : 16.67, "50-Day High" : 0.0109, "Return on Investment" : 0.044, "Shares Float" : 36.7, "Dividend Yield" : 0.0983, "EPS growth next 5 years" : 0.025, "Industry" : "REIT - Diversified", "Beta" : 0.55, "Sales growth quarter over quarter" : 0.309, "Operating Margin" : 0.682, "EPS (ttm)" : 1.37, "PEG" : 4.75, "Float Short" : 0.0182, "52-Week Low" : 0.2179, "Average True Range" : 0.24, "EPS growth next year" : 0.1739, "Company" : "Apollo Commercial Real Estate Finance, Inc.", "Gap" : 0.0025, "Relative Volume" : 1.48, "Volatility (Month)" : 0.0152, "Market Cap" : 608.45, "Volume" : 299352, "Gross Margin" : 0.919, "Short Ratio" : 3.01, "Performance (Half Year)" : -0.0502, "Relative Strength Index (14)" : 68.71, "Insider Ownership" : 0.004, "20-Day Simple Moving Average" : 0.0331, "Performance (Month)" : 0.0376, "P/Free Cash Flow" : 126.76, "Institutional Transactions" : 0.0318, "Performance (Year)" : 0.1259, "LT Debt/Equity" : 0.28, "Average Volume" : 222.35, "EPS growth this year" : 0.193, "50-Day Simple Moving Average" : 0.0673 }
{ "_id" : ObjectId("52853801bb1177ca391c1968"), "Ticker" : "ARR", "Profit Margin" : 0.848, "Institutional Ownership" : 0.318, "EPS growth past 5 years" : 0.813, "Total Debt/Equity" : 8.92, "Return on Assets" : 0.031, "Sector" : "Financial", "P/S" : 1.7, "Change from Open" : 0.0223, "Performance (YTD)" : -0.2821, "Performance (Week)" : -0.0025, "Insider Transactions" : 0.2313, "P/B" : 0.68, "Payout Ratio" : 0.474, "Performance (Quarter)" : -0.0195, "Forward P/E" : 6.79, "P/E" : 1.88, "200-Day Simple Moving Average" : -0.1454, "Shares Outstanding" : 372.59, "Earnings Date" : ISODate("2013-10-28T04:00:00Z"), "52-Week High" : -0.3453, "P/Cash" : 1.87, "Change" : 0.0249, "Analyst Recom" : 2.6, "Volatility (Week)" : 0.024, "Country" : "USA", "Return on Equity" : 0.308, "50-Day Low" : 0.0728, "Price" : 4.12, "50-Day High" : -0.0678, "Return on Investment" : 0.011, "Shares Float" : 366.32, "Dividend Yield" : 0.1493, "EPS growth next 5 years" : -0.049, "Industry" : "REIT - Residential", "Beta" : 0.3, "Operating Margin" : 0.858, "EPS (ttm)" : 2.14, "Float Short" : 0.0415, "52-Week Low" : 0.1495, "Average True Range" : 0.09, "EPS growth next year" : -0.0878, "Company" : "ARMOUR Residential REIT, Inc.", "Gap" : 0.0025, "Relative Volume" : 1.37, "Volatility (Month)" : 0.0218, "Market Cap" : 1497.82, "Volume" : 6608855, "Short Ratio" : 2.87, "Performance (Half Year)" : -0.2651, "Relative Strength Index (14)" : 51.26, "Insider Ownership" : 0.002, "20-Day Simple Moving Average" : -0.0024, "Performance (Month)" : -0.0099, "P/Free Cash Flow" : 10.46, "Institutional Transactions" : 0.0016, "Performance (Year)" : -0.286, "LT Debt/Equity" : 0, "Average Volume" : 5299, "EPS growth this year" : 7.533, "50-Day Simple Moving Average" : 0.0048 }
{ "_id" : ObjectId("52853801bb1177ca391c1998"), "Ticker" : "ATHL", "Profit Margin" : 0.732, "Institutional Ownership" : 0.753, "EPS growth past 5 years" : 0, "Total Debt/Equity" : 1.81, "Current Ratio" : 0.5, "Return on Assets" : 0.218, "Sector" : "Basic Materials", "P/S" : 10.42, "Change from Open" : 0.0088, "Performance (YTD)" : 0.1851, "Performance (Week)" : 0.1049, "Quick Ratio" : 0.5, "Insider Transactions" : -0.2682, "P/B" : 7.24, "EPS growth quarter over quarter" : -0.566, "Payout Ratio" : 0, "Performance (Quarter)" : 0.2007, "Forward P/E" : 27.38, "P/E" : 28.16, "200-Day Simple Moving Average" : 0.0877, "Shares Outstanding" : 66.34, "Earnings Date" : ISODate("2013-11-11T21:30:00Z"), "52-Week High" : -0.0439, "P/Cash" : 866.67, "Change" : 0.0126, "Analyst Recom" : 2.3, "Volatility (Week)" : 0.0678, "Country" : "USA", "Return on Equity" : 0.528, "50-Day Low" : 0.2479, "Price" : 33.07, "50-Day High" : -0.0439, "Return on Investment" : 0.08, "Shares Float" : 76.13, "EPS growth next 5 years" : 0.5, "Industry" : "Independent Oil & Gas", "Sales growth quarter over quarter" : 0.964, "Operating Margin" : 0.394, "EPS (ttm)" : 1.16, "PEG" : 0.56, "Float Short" : 0.0046, "52-Week Low" : 0.3097, "Average True Range" : 1.53, "EPS growth next year" : 0.6013, "Company" : "Athlon Energy Inc.", "Gap" : 0.0037, "Relative Volume" : 0.59, "Volatility (Month)" : 0.0464, "Market Cap" : 2166.66, "Volume" : 177265, "Gross Margin" : 0.791, "Short Ratio" : 1.07, "Relative Strength Index (14)" : 56.58, "Insider Ownership" : 0.09, "20-Day Simple Moving Average" : 0.0373, "Performance (Month)" : 0.0102, "LT Debt/Equity" : 1.81, "Average Volume" : 330.36, "EPS growth this year" : 0, "50-Day Simple Moving Average" : 0.0476 }
{ "_id" : ObjectId("52853801bb1177ca391c19f6"), "Ticker" : "AYR", "Profit Margin" : 0.548, "Institutional Ownership" : 0.745, "EPS growth past 5 years" : -0.228, "Total Debt/Equity" : 2.08, "Return on Assets" : 0.066, "Sector" : "Services", "P/S" : 1.92, "Change from Open" : 0.0058, "Performance (YTD)" : 0.5577, "Performance (Week)" : -0.0032, "Insider Transactions" : -0.0052, "P/B" : 0.83, "EPS growth quarter over quarter" : -0.656, "Payout Ratio" : 0.123, "Performance (Quarter)" : 0.1566, "Forward P/E" : 10.45, "P/E" : 126.07, "200-Day Simple Moving Average" : 0.2063, "Shares Outstanding" : 70.35, "Earnings Date" : ISODate("2013-10-31T12:30:00Z"), "52-Week High" : -0.0257, "P/Cash" : 5.58, "Change" : 0.0042, "Analyst Recom" : 2.6, "Volatility (Week)" : 0.0202, "Country" : "USA", "Return on Equity" : 0.257, "50-Day Low" : 0.1304, "Price" : 18.99, "50-Day High" : -0.0257, "Return on Investment" : 0.007, "Shares Float" : 64.67, "Dividend Yield" : 0.0349, "EPS growth next 5 years" : 0.292, "Industry" : "Rental & Leasing Services", "Beta" : 2.07, "Sales growth quarter over quarter" : -0.016, "Operating Margin" : 0.457, "EPS (ttm)" : 0.15, "PEG" : 4.32, "Float Short" : 0.0327, "52-Week Low" : 0.8106, "Average True Range" : 0.37, "EPS growth next year" : 0.4873, "Sales growth past 5 years" : 0.125, "Company" : "Aircastle LTD", "Gap" : -0.0016, "Relative Volume" : 0.39, "Volatility (Month)" : 0.0193, "Market Cap" : 1330.3, "Volume" : 200382, "Short Ratio" : 3.78, "Performance (Half Year)" : 0.2295, "Relative Strength Index (14)" : 58.67, "Insider Ownership" : 0.008, "20-Day Simple Moving Average" : 0.0054, "Performance (Month)" : 0.0849, "P/Free Cash Flow" : 3.39, "Institutional Transactions" : -0.0268, "Performance (Year)" : 0.7493, "LT Debt/Equity" : 2.08, "Average Volume" : 559.42, "EPS growth this year" : -0.72, "50-Day Simple Moving Average" : 0.0545 }
{ "_id" : ObjectId("52853801bb1177ca391c1a97"), "Ticker" : "BK", "Profit Margin" : 0.63, "Institutional Ownership" : 0.826, "EPS growth past 5 years" : -0.03, "Total Debt/Equity" : 0.53, "Return on Assets" : 0.006, "Sector" : "Financial", "P/S" : 11.32, "Change from Open" : -0.0015, "Performance (YTD)" : 0.3095, "Performance (Week)" : 0.0195, "Insider Transactions" : -0.1546, "P/B" : 1.07, "EPS growth quarter over quarter" : 0.344, "Payout Ratio" : 0.304, "Performance (Quarter)" : 0.0898, "Forward P/E" : 13.19, "P/E" : 18.03, "200-Day Simple Moving Average" : 0.127, "Shares Outstanding" : 1148.72, "Earnings Date" : ISODate("2013-10-16T12:30:00Z"), "52-Week High" : -0.0069, "P/Cash" : 0.22, "Change" : 0.003, "Analyst Recom" : 2.7, "Volatility (Week)" : 0.0216, "Country" : "USA", "Return on Equity" : 0.06, "50-Day Low" : 0.1255, "Price" : 33.1, "50-Day High" : -0.0069, "Return on Investment" : 0.042, "Shares Float" : 1146.23, "Dividend Yield" : 0.0182, "EPS growth next 5 years" : 0.066, "Industry" : "Asset Management", "Beta" : 1.16, "Sales growth quarter over quarter" : -0.025, "EPS (ttm)" : 1.83, "PEG" : 2.73, "Float Short" : 0.0125, "52-Week Low" : 0.4512, "Average True Range" : 0.54, "EPS growth next year" : 0.096, "Sales growth past 5 years" : -0.092, "Company" : "The Bank of New York Mellon Corporation", "Gap" : 0.0045, "Relative Volume" : 0.61, "Volatility (Month)" : 0.0155, "Market Cap" : 37907.89, "Volume" : 2578576, "Short Ratio" : 3.1, "Performance (Half Year)" : 0.1156, "Relative Strength Index (14)" : 63.27, "Insider Ownership" : 0.001, "20-Day Simple Moving Average" : 0.032, "Performance (Month)" : 0.0749, "Institutional Transactions" : 0.0015, "Performance (Year)" : 0.4019, "LT Debt/Equity" : 0.53, "Average Volume" : 4611.68, "EPS growth this year" : 0, "50-Day Simple Moving Average" : 0.0626 }
{ "_id" : ObjectId("52853801bb1177ca391c1abd"), "Ticker" : "BLX", "Profit Margin" : 0.588, "Institutional Ownership" : 0.281, "EPS growth past 5 years" : 0.045, "Total Debt/Equity" : 3.73, "Return on Assets" : 0.017, "Sector" : "Financial", "P/S" : 5.22, "Change from Open" : 0.0103, "Performance (YTD)" : 0.2812, "Performance (Week)" : -0.0131, "P/B" : 1.19, "EPS growth quarter over quarter" : -0.506, "Payout Ratio" : 0.372, "Performance (Quarter)" : 0.0597, "Forward P/E" : 9.32, "P/E" : 13.01, "200-Day Simple Moving Average" : 0.1134, "Shares Outstanding" : 38.22, "Earnings Date" : ISODate("2013-10-16T12:30:00Z"), "52-Week High" : -0.0161, "P/Cash" : 1.71, "Change" : 0.0095, "Analyst Recom" : 1.7, "Volatility (Week)" : 0.023, "Country" : "Panama", "Return on Equity" : 0.137, "50-Day Low" : 0.1075, "Price" : 26.54, "50-Day High" : -0.0161, "Return on Investment" : 0.027, "Shares Float" : 29.25, "Dividend Yield" : 0.0456, "EPS growth next 5 years" : 0.0698, "Industry" : "Foreign Money Center Banks", "Beta" : 1.19, "Sales growth quarter over quarter" : 0, "Operating Margin" : 0.809, "EPS (ttm)" : 2.02, "PEG" : 1.86, "Float Short" : 0.0296, "52-Week Low" : 0.366, "Average True Range" : 0.49, "EPS growth next year" : 0.2192, "Sales growth past 5 years" : -0.062, "Company" : "Banco Latinoamericano de Comercio Exterior, S.A", "Gap" : -0.0008, "Relative Volume" : 1.05, "Volatility (Month)" : 0.0205, "Market Cap" : 1004.75, "Volume" : 102478, "Short Ratio" : 8.07, "Performance (Half Year)" : 0.1597, "Relative Strength Index (14)" : 60.34, "Insider Ownership" : 0.0706, "20-Day Simple Moving Average" : 0.0098, "Performance (Month)" : 0.0554, "P/Free Cash Flow" : 56.77, "Institutional Transactions" : 0.0149, "Performance (Year)" : 0.2983, "LT Debt/Equity" : 1.91, "Average Volume" : 107.45, "EPS growth this year" : 0.098, "50-Day Simple Moving Average" : 0.0498 }
{ "_id" : ObjectId("52853801bb1177ca391c1af0"), "Ticker" : "BPO", "Profit Margin" : 0.503, "Institutional Ownership" : 0.958, "EPS growth past 5 years" : 0.354, "Total Debt/Equity" : 1.15, "Current Ratio" : 1, "Return on Assets" : 0.043, "Sector" : "Financial", "P/S" : 4.04, "Change from Open" : 0.001, "Performance (YTD)" : 0.1519, "Performance (Week)" : -0.0052, "Quick Ratio" : 1, "P/B" : 0.9, "EPS growth quarter over quarter" : -0.415, "Payout Ratio" : 0.235, "Performance (Quarter)" : 0.1825, "Forward P/E" : 18.74, "P/E" : 8.65, "200-Day Simple Moving Average" : 0.1124, "Shares Outstanding" : 505, "Earnings Date" : ISODate("2011-02-11T13:30:00Z"), "52-Week High" : -0.022, "P/Cash" : 22.13, "Change" : 0.0021, "Analyst Recom" : 3.1, "Volatility (Week)" : 0.0127, "Country" : "USA", "Return on Equity" : 0.115, "50-Day Low" : 0.1976, "Price" : 19.15, "50-Day High" : -0.022, "Return on Investment" : 0.015, "Shares Float" : 504.86, "Dividend Yield" : 0.0293, "EPS growth next 5 years" : 0.0735, "Industry" : "Property Management", "Beta" : 1.64, "Sales growth quarter over quarter" : 0.01, "Operating Margin" : 0.552, "EPS (ttm)" : 2.21, "PEG" : 1.18, "Float Short" : 0.0062, "52-Week Low" : 0.2728, "Average True Range" : 0.23, "EPS growth next year" : -0.105, "Sales growth past 5 years" : -0.043, "Company" : "Brookfield Properties Corporation", "Gap" : 0.001, "Relative Volume" : 0.17, "Volatility (Month)" : 0.0112, "Market Cap" : 9650.55, "Volume" : 249482, "Gross Margin" : 0.621, "Short Ratio" : 1.9, "Performance (Half Year)" : 0.0269, "Relative Strength Index (14)" : 62.08, "Insider Ownership" : 0.4972, "20-Day Simple Moving Average" : 0.012, "Performance (Month)" : 0.0154, "Institutional Transactions" : -0.004, "Performance (Year)" : 0.2482, "LT Debt/Equity" : 1.15, "Average Volume" : 1650.73, "EPS growth this year" : -0.212, "50-Day Simple Moving Average" : 0.0538 }

2. Liste as ações com perdas (limite a 10 novamente)
- db.stocks.find({"Profit Margin": {$lt: 0}}).limit(10)
{ "_id" : ObjectId("52853800bb1177ca391c1806"), "Ticker" : "AAOI", "Profit Margin" : -0.023, "Institutional Ownership" : 0.114, "EPS growth past 5 years" : 0, "Current Ratio" : 1.5, "Return on Assets" : -0.048, "Sector" : "Technology", "P/S" : 2.3, "Change from Open" : -0.0215, "Performance (YTD)" : 0.2671, "Performance (Week)" : -0.0381, "Quick Ratio" : 0.9, "EPS growth quarter over quarter" : -1, "Forward P/E" : 12.77, "200-Day Simple Moving Average" : 0.0654, "Shares Outstanding" : 12.6, "52-Week High" : -0.0904, "P/Cash" : 16.23, "Change" : -0.0269, "Analyst Recom" : 1.8, "Volatility (Week)" : 0.0377, "Country" : "USA", "Return on Equity" : 0.043, "50-Day Low" : 0.3539, "Price" : 12.28, "50-Day High" : -0.0904, "Return on Investment" : -0.004, "Shares Float" : 11.46, "Industry" : "Semiconductor - Integrated Circuits", "Sales growth quarter over quarter" : 0.256, "Operating Margin" : -0.007, "EPS (ttm)" : -0.13, "Float Short" : 0.0011, "52-Week Low" : 0.3539, "Average True Range" : 0.63, "EPS growth next year" : 38.52, "Company" : "Applied Optoelectronics, Inc.", "Gap" : -0.0055, "Relative Volume" : 0.12, "Volatility (Month)" : 0.0608, "Market Cap" : 159.06, "Volume" : 12203, "Gross Margin" : 0.292, "Short Ratio" : 0.12, "Insider Ownership" : 0.021, "20-Day Simple Moving Average" : -0.0251, "Performance (Month)" : 0.2397, "Average Volume" : 110.95, "EPS growth this year" : 0.833, "50-Day Simple Moving Average" : 0.0654 }
{ "_id" : ObjectId("52853800bb1177ca391c180c"), "Ticker" : "AAV", "Profit Margin" : -0.232, "Institutional Ownership" : 0.58, "EPS growth past 5 years" : -0.265, "Total Debt/Equity" : 0.32, "Current Ratio" : 0.8, "Return on Assets" : -0.032, "Sector" : "Basic Materials", "P/S" : 2.64, "Change from Open" : 0.0286, "Performance (YTD)" : 0.1914, "Performance (Week)" : 0.0158, "Quick Ratio" : 0.8, "P/B" : 0.63, "EPS growth quarter over quarter" : 1.556, "Performance (Quarter)" : 0.0349, "200-Day Simple Moving Average" : 0.0569, "Shares Outstanding" : 168.38, "Earnings Date" : ISODate("2011-03-16T04:00:00Z"), "52-Week High" : -0.1242, "Change" : 0.0233, "Analyst Recom" : 2.7, "Volatility (Week)" : 0.0381, "Country" : "Canada", "Return on Equity" : -0.055, "50-Day Low" : 0.1127, "Price" : 3.95, "50-Day High" : -0.0436, "Return on Investment" : -0.068, "Shares Float" : 167.07, "Industry" : "Oil & Gas Drilling & Exploration", "Beta" : 2.05, "Sales growth quarter over quarter" : 0.399, "Operating Margin" : 0.102, "EPS (ttm)" : -0.34, "Float Short" : 0.0008, "52-Week Low" : 0.4158, "Average True Range" : 0.12, "EPS growth next year" : -0.667, "Sales growth past 5 years" : -0.121, "Company" : "Advantage Oil & Gas Ltd.", "Gap" : -0.0052, "Relative Volume" : 0.85, "Volatility (Month)" : 0.0303, "Market Cap" : 649.96, "Volume" : 116750, "Gross Margin" : 0.682, "Short Ratio" : 0.89, "Performance (Half Year)" : 0.0078, "Relative Strength Index (14)" : 52.62, "Insider Ownership" : 0.0025, "20-Day Simple Moving Average" : -0.0001, "Performance (Month)" : 0.0158, "Institutional Transactions" : 0.0402, "Performance (Year)" : 0.1386, "LT Debt/Equity" : 0.32, "Average Volume" : 149.81, "EPS growth this year" : 0.42, "50-Day Simple Moving Average" : 0.023 }
{ "_id" : ObjectId("52853800bb1177ca391c1815"), "Ticker" : "ABCD", "Profit Margin" : -0.645, "Institutional Ownership" : 0.186, "EPS growth past 5 years" : -0.195, "Current Ratio" : 1.4, "Return on Assets" : -0.416, "Sector" : "Services", "P/S" : 0.41, "Change from Open" : 0, "Performance (YTD)" : 0.2072, "Performance (Week)" : 0.0229, "Quick Ratio" : 1.2, "Insider Transactions" : -0.0267, "EPS growth quarter over quarter" : 1.022, "Performance (Quarter)" : -0.0496, "200-Day Simple Moving Average" : 0.0446, "Shares Outstanding" : 47.36, "Earnings Date" : ISODate("2013-11-07T21:30:00Z"), "52-Week High" : -0.2757, "P/Cash" : 1.37, "Change" : 0, "Analyst Recom" : 2, "Volatility (Week)" : 0.0737, "Country" : "USA", "Return on Equity" : 3.596, "50-Day Low" : 0.072, "Price" : 1.34, "50-Day High" : -0.2299, "Return on Investment" : -0.876, "Shares Float" : 15.11, "Industry" : "Education & Training Services", "Beta" : 1.7, "Sales growth quarter over quarter" : 0.059, "Operating Margin" : 0.048, "EPS (ttm)" : -2.06, "Float Short" : 0.0007, "52-Week Low" : 0.5952, "Average True Range" : 0.09, "Sales growth past 5 years" : 0.084, "Company" : "Cambium Learning Group, Inc.", "Gap" : 0, "Relative Volume" : 0.04, "Volatility (Month)" : 0.0584, "Market Cap" : 63.46, "Volume" : 1600, "Gross Margin" : 0.552, "Short Ratio" : 0.21, "Performance (Half Year)" : 0.1356, "Relative Strength Index (14)" : 48.07, "Insider Ownership" : 0.003, "20-Day Simple Moving Average" : 0.0037, "Performance (Month)" : -0.0074, "P/Free Cash Flow" : 2.47, "Institutional Transactions" : -0.095, "Performance (Year)" : 0.6543, "Average Volume" : 48.58, "EPS growth this year" : -1.533, "50-Day Simple Moving Average" : -0.064 }
{ "_id" : ObjectId("52853800bb1177ca391c1817"), "Ticker" : "ABFS", "Profit Margin" : -0.005, "Institutional Ownership" : 0.921, "EPS growth past 5 years" : -0.164, "Total Debt/Equity" : 0.31, "Current Ratio" : 1.3, "Return on Assets" : -0.01, "Sector" : "Services", "P/S" : 0.37, "Change from Open" : -0.006, "Performance (YTD)" : 2.3474, "Performance (Week)" : 0.1949, "Quick Ratio" : 1.3, "Insider Transactions" : 0.1293, "P/B" : 1.69, "EPS growth quarter over quarter" : -0.591, "Performance (Quarter)" : 0.3813, "Forward P/E" : 18.66, "200-Day Simple Moving Average" : 0.6449, "Shares Outstanding" : 25.69, "Earnings Date" : ISODate("2013-11-11T13:30:00Z"), "52-Week High" : -0.0166, "P/Cash" : 6.87, "Change" : -0.0082, "Analyst Recom" : 2.8, "Volatility (Week)" : 0.0625, "Country" : "USA", "Return on Equity" : -0.022, "50-Day Low" : 0.474, "Price" : 31.44, "50-Day High" : -0.0166, "Return on Investment" : -0.008, "Shares Float" : 24.3, "Dividend Yield" : 0.0038, "EPS growth next 5 years" : 0.1, "Industry" : "Trucking", "Beta" : 1.91, "Sales growth quarter over quarter" : 0.13, "Operating Margin" : -0.006, "EPS (ttm)" : -0.4, "Float Short" : 0.1176, "52-Week Low" : 3.9271, "Average True Range" : 1.58, "EPS growth next year" : 7.0142, "Sales growth past 5 years" : 0.024, "Company" : "Arkansas Best Corporation", "Gap" : -0.0022, "Relative Volume" : 0.73, "Volatility (Month)" : 0.0537, "Market Cap" : 814.5, "Volume" : 351906, "Gross Margin" : 0.212, "Short Ratio" : 5.44, "Performance (Half Year)" : 0.8592, "Relative Strength Index (14)" : 67.77, "Insider Ownership" : 0.034, "20-Day Simple Moving Average" : 0.1304, "Performance (Month)" : 0.3319, "P/Free Cash Flow" : 13.67, "Institutional Transactions" : 0.0328, "Performance (Year)" : 3.4336, "LT Debt/Equity" : 0.2, "Average Volume" : 525.42, "EPS growth this year" : -2.348, "50-Day Simple Moving Average" : 0.1974 }
{ "_id" : ObjectId("52853800bb1177ca391c181b"), "Ticker" : "ABMC", "Profit Margin" : -0.0966, "Institutional Ownership" : 0.12, "EPS growth past 5 years" : 0, "Total Debt/Equity" : 0.63, "Current Ratio" : 1.74, "Return on Assets" : -0.1194, "Sector" : "Healthcare", "P/S" : 0.34, "Change from Open" : 0, "Performance (YTD)" : 0.3077, "Performance (Week)" : 0.1333, "Quick Ratio" : 0.57, "P/B" : 1, "EPS growth quarter over quarter" : -2.4252, "Performance (Quarter)" : 0, "200-Day Simple Moving Average" : 0.0413, "Shares Outstanding" : 21.74, "Earnings Date" : ISODate("2013-11-11T05:00:00Z"), "52-Week High" : -0.3929, "P/Cash" : 6.26, "Change" : 0, "Volatility (Week)" : 0.0695, "Country" : "USA", "Return on Equity" : -0.2455, "50-Day Low" : 1.4286, "Price" : 0.17, "50-Day High" : -0.0556, "Return on Investment" : -0.1961, "Shares Float" : 18.7, "Industry" : "Diagnostic Substances", "Beta" : 1.71, "Sales growth quarter over quarter" : -0.1896, "Operating Margin" : -0.0734, "EPS (ttm)" : -0.05, "Float Short" : 0.0003, "52-Week Low" : 1.4286, "Average True Range" : 0.02, "Sales growth past 5 years" : 0.0028, "Company" : "American Bio Medica Corp.", "Gap" : 0, "Relative Volume" : 0.04, "Volatility (Month)" : 0.0517, "Market Cap" : 3.7, "Volume" : 0, "Gross Margin" : 0.3916, "Short Ratio" : 0.43, "Performance (Half Year)" : 0.0625, "Relative Strength Index (14)" : 56.93, "Insider Ownership" : 0.14, "20-Day Simple Moving Average" : 0.1039, "Performance (Month)" : 0.2143, "Institutional Transactions" : -0.1183, "Performance (Year)" : -0.0556, "LT Debt/Equity" : 0.2, "Average Volume" : 13.73, "EPS growth this year" : 0.1416, "50-Day Simple Moving Average" : 0.1502 }
{ "_id" : ObjectId("52853800bb1177ca391c1821"), "Ticker" : "ABX", "Profit Margin" : -0.769, "Institutional Ownership" : 0.739, "EPS growth past 5 years" : -0.206, "Total Debt/Equity" : 1.13, "Current Ratio" : 1.8, "Return on Assets" : -0.241, "Sector" : "Basic Materials", "P/S" : 1.32, "Change from Open" : -0.0019, "Performance (YTD)" : -0.4728, "Performance (Week)" : -0.0131, "Quick Ratio" : 1, "P/B" : 1.33, "EPS growth quarter over quarter" : -0.727, "Performance (Quarter)" : -0.084, "Forward P/E" : 8.19, "200-Day Simple Moving Average" : -0.1368, "Shares Outstanding" : 1001, "Earnings Date" : ISODate("2011-02-17T13:30:00Z"), "52-Week High" : -0.4877, "P/Cash" : 7.94, "Change" : 0.0014, "Analyst Recom" : 2.6, "Volatility (Week)" : 0.0202, "Country" : "Canada", "Return on Equity" : -0.592, "50-Day Low" : 0.0581, "Price" : 18.13, "50-Day High" : -0.121, "Return on Investment" : -0.017, "Shares Float" : 997.93, "Dividend Yield" : 0.011, "EPS growth next 5 years" : 0.02, "Industry" : "Gold", "Beta" : 0.46, "Sales growth quarter over quarter" : -0.122, "Operating Margin" : 0.366, "EPS (ttm)" : -10.08, "Float Short" : 0.0118, "52-Week Low" : 0.3525, "Average True Range" : 0.57, "EPS growth next year" : -0.16, "Sales growth past 5 years" : 0.193, "Company" : "Barrick Gold Corporation", "Gap" : 0.0033, "Relative Volume" : 1.09, "Volatility (Month)" : 0.0277, "Market Cap" : 18118.1, "Volume" : 17478164, "Gross Margin" : 0.444, "Short Ratio" : 0.67, "Performance (Half Year)" : -0.0479, "Relative Strength Index (14)" : 41.96, "20-Day Simple Moving Average" : -0.0436, "Performance (Month)" : 0.018, "Institutional Transactions" : 0.0315, "Performance (Year)" : -0.474, "LT Debt/Equity" : 1.07, "Average Volume" : 17602.98, "EPS growth this year" : -1.147, "50-Day Simple Moving Average" : -0.0239 }
{ "_id" : ObjectId("52853800bb1177ca391c1826"), "Ticker" : "ACCL", "Profit Margin" : -0.014, "Institutional Ownership" : 0.911, "EPS growth past 5 years" : -0.421, "Total Debt/Equity" : 0, "Current Ratio" : 1.4, "Return on Assets" : -0.006, "Sector" : "Technology", "P/S" : 3.13, "Change from Open" : 0.0011, "Performance (YTD)" : 0.0331, "Performance (Week)" : 0.0108, "Quick Ratio" : 1.4, "Insider Transactions" : -0.1768, "P/B" : 2.1, "Performance (Quarter)" : 0.0331, "Forward P/E" : 24.35, "200-Day Simple Moving Average" : 0.0112, "Shares Outstanding" : 55.66, "Earnings Date" : ISODate("2013-10-30T20:30:00Z"), "52-Week High" : -0.071, "P/Cash" : 4.14, "Change" : -0.0064, "Analyst Recom" : 2.3, "Volatility (Week)" : 0.0189, "Country" : "USA", "Return on Equity" : -0.01, "50-Day Low" : 0.0322, "Price" : 9.29, "50-Day High" : -0.071, "Return on Investment" : -0.086, "Shares Float" : 55.4, "EPS growth next 5 years" : 0.2, "Industry" : "Application Software", "Beta" : 0.84, "Sales growth quarter over quarter" : 0.01, "Operating Margin" : -0.091, "EPS (ttm)" : -0.05, "Float Short" : 0.0179, "52-Week Low" : 0.1987, "Average True Range" : 0.21, "EPS growth next year" : 0.1294, "Sales growth past 5 years" : 0.153, "Company" : "Accelrys Inc.", "Gap" : -0.0075, "Relative Volume" : 0.31, "Volatility (Month)" : 0.0236, "Market Cap" : 520.42, "Volume" : 33912, "Gross Margin" : 0.679, "Short Ratio" : 8.32, "Performance (Half Year)" : 0.0872, "Relative Strength Index (14)" : 45.52, "Insider Ownership" : 0.0092, "20-Day Simple Moving Average" : -0.018, "Performance (Month)" : -0.0032, "Institutional Transactions" : 0.0133, "Performance (Year)" : 0.0747, "LT Debt/Equity" : 0, "Average Volume" : 118.95, "EPS growth this year" : -7.333, "50-Day Simple Moving Average" : -0.0226 }
{ "_id" : ObjectId("52853800bb1177ca391c182b"), "Ticker" : "ACFC", "Profit Margin" : -0.18, "Institutional Ownership" : 0.079, "EPS growth past 5 years" : -0.524, "Total Debt/Equity" : 0, "Return on Assets" : -0.007, "Sector" : "Financial", "P/S" : 0.27, "Change from Open" : 0, "Performance (YTD)" : 0.6667, "Performance (Week)" : -0.1184, "P/B" : 0.27, "EPS growth quarter over quarter" : 0.483, "Performance (Quarter)" : -0.1321, "200-Day Simple Moving Average" : -0.2118, "Shares Outstanding" : 2.5, "Earnings Date" : ISODate("2013-11-04T05:00:00Z"), "52-Week High" : -0.4956, "P/Cash" : 0.1, "Change" : 0.0358, "Analyst Recom" : 3, "Volatility (Week)" : 0.0508, "Country" : "USA", "Return on Equity" : -0.147, "50-Day Low" : 0.081, "Price" : 3.47, "50-Day High" : -0.2078, "Return on Investment" : 0.161, "Shares Float" : 1.72, "Industry" : "Regional - Southeast Banks", "Beta" : 0.83, "Sales growth quarter over quarter" : -0.14, "Operating Margin" : -0.18, "EPS (ttm)" : -2.22, "Float Short" : 0.0085, "52-Week Low" : 1.3767, "Average True Range" : 0.12, "Sales growth past 5 years" : -0.096, "Company" : "Atlantic Coast Financial Corporation", "Gap" : 0.0358, "Relative Volume" : 0, "Volatility (Month)" : 0.0228, "Market Cap" : 8.39, "Volume" : 0, "Short Ratio" : 6.07, "Performance (Half Year)" : -0.3667, "Relative Strength Index (14)" : 40.71, "Insider Ownership" : 0.001, "20-Day Simple Moving Average" : -0.0742, "Performance (Month)" : -0.1138, "Institutional Transactions" : -4.3825, "Performance (Year)" : 0.7539, "LT Debt/Equity" : 0, "Average Volume" : 2.41, "EPS growth this year" : 0.354, "50-Day Simple Moving Average" : -0.0993 }
{ "_id" : ObjectId("52853800bb1177ca391c182f"), "Ticker" : "ACH", "Profit Margin" : -0.051, "Institutional Ownership" : 0.02, "EPS growth past 5 years" : -0.227, "Total Debt/Equity" : 2.84, "Current Ratio" : 0.7, "Return on Assets" : -0.039, "Sector" : "Basic Materials", "P/S" : 0.19, "Change from Open" : -0.0032, "Performance (YTD)" : -0.2645, "Performance (Week)" : -0.0437, "Quick Ratio" : 0.7, "P/B" : 0.67, "EPS growth quarter over quarter" : 0.711, "Performance (Quarter)" : 0.0057, "200-Day Simple Moving Average" : -0.0544, "Shares Outstanding" : 540.98, "Earnings Date" : ISODate("2011-03-02T05:00:00Z"), "52-Week High" : -0.3369, "P/Cash" : 2.77, "Change" : 0.0059, "Analyst Recom" : 5, "Volatility (Week)" : 0.015, "Country" : "China", "Return on Equity" : -0.172, "50-Day Low" : 0.0176, "Price" : 8.81, "50-Day High" : -0.1117, "Return on Investment" : -0.029, "Shares Float" : 156.18, "Industry" : "Aluminum", "Beta" : 1.9, "Sales growth quarter over quarter" : 0.065, "Operating Margin" : -0.021, "EPS (ttm)" : -1.76, "Float Short" : 0.02, "52-Week Low" : 0.2154, "Average True Range" : 0.2, "EPS growth next year" : 0.487, "Sales growth past 5 years" : 0.119, "Company" : "Aluminum Corporation Of China Limited", "Gap" : 0.0091, "Relative Volume" : 1.05, "Volatility (Month)" : 0.0183, "Market Cap" : 4738.98, "Volume" : 78010, "Gross Margin" : 0.005, "Short Ratio" : 38.23, "Performance (Half Year)" : -0.124, "Relative Strength Index (14)" : 38.92, "20-Day Simple Moving Average" : -0.0477, "Performance (Month)" : -0.0405, "Institutional Transactions" : -0.0063, "Performance (Year)" : -0.1577, "LT Debt/Equity" : 1.19, "Average Volume" : 81.57, "EPS growth this year" : 0.839, "50-Day Simple Moving Average" : -0.0421 }
{ "_id" : ObjectId("52853800bb1177ca391c1832"), "Ticker" : "ACI", "Profit Margin" : -0.173, "Institutional Ownership" : 0.662, "EPS growth past 5 years" : -0.361, "Total Debt/Equity" : 1.97, "Current Ratio" : 3.5, "Return on Assets" : -0.058, "Sector" : "Basic Materials", "P/S" : 0.28, "Change from Open" : -0.0372, "Performance (YTD)" : -0.4019, "Performance (Week)" : -0.0183, "Quick Ratio" : 3, "Insider Transactions" : 0.0178, "P/B" : 0.35, "EPS growth quarter over quarter" : -5.455, "Performance (Quarter)" : -0.0549, "200-Day Simple Moving Average" : -0.1177, "Shares Outstanding" : 212.11, "Earnings Date" : ISODate("2013-10-29T12:30:00Z"), "52-Week High" : -0.4702, "P/Cash" : 0.66, "Change" : -0.0372, "Analyst Recom" : 2.8, "Volatility (Week)" : 0.0516, "Country" : "USA", "Return on Equity" : -0.207, "50-Day Low" : 0.104, "Price" : 4.14, "50-Day High" : -0.2114, "Return on Investment" : -0.047, "Shares Float" : 209.56, "Dividend Yield" : 0.0279, "EPS growth next 5 years" : 0.05, "Industry" : "Industrial Metals & Minerals", "Beta" : 1.61, "Sales growth quarter over quarter" : -0.272, "Operating Margin" : -0.04, "EPS (ttm)" : -3.16, "Float Short" : 0.1772, "52-Week Low" : 0.1997, "Average True Range" : 0.23, "EPS growth next year" : 0.143, "Sales growth past 5 years" : 0.115, "Company" : "Arch Coal Inc.", "Gap" : 0, "Relative Volume" : 0.66, "Volatility (Month)" : 0.0546, "Market Cap" : 912.08, "Volume" : 5417562, "Gross Margin" : 0.141, "Short Ratio" : 4.12, "Performance (Half Year)" : -0.1224, "Relative Strength Index (14)" : 43.64, "Insider Ownership" : 0.0054, "20-Day Simple Moving Average" : -0.0171, "Performance (Month)" : 0.0437, "Institutional Transactions" : 0.0024, "Performance (Year)" : -0.3741, "LT Debt/Equity" : 1.97, "Average Volume" : 9000.5, "EPS growth this year" : -5.378, "50-Day Simple Moving Average" : -0.0482 }

3. Liste as 10 ações mais rentáveis
- db.stocks.find({}).sort({"Profit Margin":-1}).limit(10)
{ "_id" : ObjectId("52853801bb1177ca391c1af3"), "Ticker" : "BPT", "Profit Margin" : 0.994, "Institutional Ownership" : 0.098, "EPS growth past 5 years" : 0.025, "Total Debt/Equity" : 0, "Sector" : "Basic Materials", "P/S" : 8.81, "Change from Open" : 0.0125, "Performance (YTD)" : 0.2758, "Performance (Week)" : -0.018, "P/B" : 2620, "EPS growth quarter over quarter" : -0.087, "Payout Ratio" : 1.001, "Performance (Quarter)" : -0.0556, "P/E" : 8.87, "200-Day Simple Moving Average" : -0.0305, "Shares Outstanding" : 21.4, "Earnings Date" : ISODate("2013-11-11T05:00:00Z"), "52-Week High" : -0.159, "P/Cash" : 1682.04, "Change" : 0.0064, "Volatility (Week)" : 0.0151, "Country" : "USA", "50-Day Low" : 0.0136, "Price" : 79.1, "50-Day High" : -0.0973, "Shares Float" : 21.4, "Dividend Yield" : 0.1103, "Industry" : "Oil & Gas Refining & Marketing", "Beta" : 0.77, "Sales growth quarter over quarter" : -0.086, "Operating Margin" : 0.994, "EPS (ttm)" : 8.86, "Float Short" : 0.0173, "52-Week Low" : 0.3422, "Average True Range" : 1.37, "Sales growth past 5 years" : 0.024, "Company" : "BP Prudhoe Bay Royalty Trust", "Gap" : -0.0061, "Relative Volume" : 0.93, "Volatility (Month)" : 0.016, "Market Cap" : 1682.04, "Volume" : 71575, "Short Ratio" : 4.41, "Performance (Half Year)" : 0.0022, "Relative Strength Index (14)" : 38.01, "20-Day Simple Moving Average" : -0.0318, "Performance (Month)" : -0.079, "Institutional Transactions" : -0.0057, "Performance (Year)" : 0.1837, "LT Debt/Equity" : 0, "Average Volume" : 84.15, "EPS growth this year" : -0.012, "50-Day Simple Moving Average" : -0.0496 }
{ "_id" : ObjectId("52853802bb1177ca391c1b69"), "Ticker" : "CACB", "Profit Margin" : 0.994, "Institutional Ownership" : 0.547, "EPS growth past 5 years" : -0.584, "Total Debt/Equity" : 0, "Return on Assets" : 0.039, "Sector" : "Financial", "P/S" : 4.66, "Change from Open" : -0.0137, "Performance (YTD)" : -0.1869, "Performance (Week)" : 0.0079, "Insider Transactions" : 1.0755, "P/B" : 1.28, "EPS growth quarter over quarter" : 25.422, "Payout Ratio" : 0, "Performance (Quarter)" : -0.1314, "Forward P/E" : 42.42, "P/E" : 4.71, "200-Day Simple Moving Average" : -0.1709, "Shares Outstanding" : 47.17, "Earnings Date" : ISODate("2013-11-13T21:30:00Z"), "52-Week High" : -0.2994, "P/Cash" : 2.26, "Change" : -0.0118, "Analyst Recom" : 3, "Volatility (Week)" : 0.0353, "Country" : "USA", "Return on Equity" : 0.336, "50-Day Low" : 0.006, "Price" : 5.03, "50-Day High" : -0.2066, "Return on Investment" : 0.346, "Shares Float" : 40.67, "EPS growth next 5 years" : 0.05, "Industry" : "Regional - Pacific Banks", "Beta" : 2.34, "Sales growth quarter over quarter" : -0.101, "Operating Margin" : 0.027, "EPS (ttm)" : 1.08, "PEG" : 0.94, "Float Short" : 0.0088, "52-Week Low" : 0.0817, "Average True Range" : 0.19, "EPS growth next year" : -0.8904, "Sales growth past 5 years" : -0.203, "Company" : "Cascade Bancorp", "Gap" : 0.002, "Relative Volume" : 1.35, "Volatility (Month)" : 0.0399, "Market Cap" : 240.11, "Volume" : 21432, "Short Ratio" : 20.55, "Performance (Half Year)" : -0.1239, "Relative Strength Index (14)" : 29.61, "Insider Ownership" : 0.009, "20-Day Simple Moving Average" : -0.0729, "Performance (Month)" : -0.1039, "Institutional Transactions" : 0.0004, "Performance (Year)" : 0.0241, "LT Debt/Equity" : 0, "Average Volume" : 17.39, "EPS growth this year" : 1.12, "50-Day Simple Moving Average" : -0.116 }
{ "_id" : ObjectId("5285380bbb1177ca391c2c3c"), "Ticker" : "ROYT", "Profit Margin" : 0.99, "Institutional Ownership" : 0.696, "EPS growth past 5 years" : 0, "Total Debt/Equity" : 0, "Return on Assets" : 0.255, "Sector" : "Basic Materials", "P/S" : 7.62, "Change from Open" : 0, "Performance (YTD)" : -0.1408, "Performance (Week)" : -0.0447, "Insider Transactions" : -0.5437, "P/B" : 2.03, "EPS growth quarter over quarter" : 1.75, "Payout Ratio" : 0.338, "Performance (Quarter)" : -0.2202, "Forward P/E" : 7.92, "P/E" : 7.68, "200-Day Simple Moving Average" : -0.1864, "Shares Outstanding" : 38.58, "52-Week High" : -0.243, "Change" : 0.0037, "Analyst Recom" : 2.4, "Volatility (Week)" : 0.0174, "Country" : "USA", "Return on Equity" : 0.255, "50-Day Low" : 0.0088, "Price" : 13.72, "50-Day High" : -0.243, "Return on Investment" : 0.15, "Shares Float" : 38.58, "Dividend Yield" : 0.1295, "EPS growth next 5 years" : 0.126, "Industry" : "Independent Oil & Gas", "Sales growth quarter over quarter" : 1.6, "Operating Margin" : 0.99, "EPS (ttm)" : 1.78, "PEG" : 0.61, "Float Short" : 0.0042, "52-Week Low" : 0.0088, "Average True Range" : 0.3, "EPS growth next year" : -0.0655, "Company" : "Pacific Coast Oil Trust", "Gap" : 0.0037, "Relative Volume" : 0.75, "Volatility (Month)" : 0.0201, "Market Cap" : 527.43, "Volume" : 262050, "Short Ratio" : 0.42, "Performance (Half Year)" : -0.1978, "Relative Strength Index (14)" : 20.73, "Insider Ownership" : 0.5205, "20-Day Simple Moving Average" : -0.0644, "Performance (Month)" : -0.1237, "Institutional Transactions" : 0.0154, "Performance (Year)" : -0.1141, "LT Debt/Equity" : 0, "Average Volume" : 388.63, "EPS growth this year" : 0.745, "50-Day Simple Moving Average" : -0.1265 }
{ "_id" : ObjectId("52853808bb1177ca391c281b"), "Ticker" : "NDRO", "Profit Margin" : 0.986, "Institutional Ownership" : 0.532, "EPS growth past 5 years" : 0, "Total Debt/Equity" : 0, "Return on Assets" : 0.078, "Sector" : "Basic Materials", "P/S" : 8.11, "Change from Open" : 0, "Performance (YTD)" : -0.2111, "Performance (Week)" : -0.0369, "Insider Transactions" : -0.3613, "P/B" : 0.67, "EPS growth quarter over quarter" : -0.378, "Payout Ratio" : 0.313, "Performance (Quarter)" : -0.1716, "Forward P/E" : 7.53, "P/E" : 8.23, "200-Day Simple Moving Average" : -0.1708, "Shares Outstanding" : 33, "Earnings Date" : ISODate("2013-11-11T05:00:00Z"), "52-Week High" : -0.2732, "Change" : -0.0073, "Analyst Recom" : 2.3, "Volatility (Week)" : 0.0224, "Country" : "USA", "Return on Equity" : 0.078, "50-Day Low" : 0.0437, "Price" : 12.17, "50-Day High" : -0.2028, "Return on Investment" : 0.091, "Shares Float" : 33, "Dividend Yield" : 0.1476, "EPS growth next 5 years" : -0.061, "Industry" : "Independent Oil & Gas", "Sales growth quarter over quarter" : -0.388, "Operating Margin" : 0.986, "EPS (ttm)" : 1.49, "Float Short" : 0.0011, "52-Week Low" : 0.0437, "Average True Range" : 0.26, "EPS growth next year" : 0.1097, "Company" : "Enduro Royalty Trust", "Gap" : -0.0073, "Relative Volume" : 1.43, "Volatility (Month)" : 0.0205, "Market Cap" : 404.58, "Volume" : 406061, "Short Ratio" : 0.12, "Performance (Half Year)" : -0.2106, "Relative Strength Index (14)" : 33.3, "Insider Ownership" : 0.6, "20-Day Simple Moving Average" : -0.0471, "Performance (Month)" : 0.0381, "Institutional Transactions" : 0.1111, "Performance (Year)" : -0.1987, "LT Debt/Equity" : 0, "Average Volume" : 311.39, "EPS growth this year" : 4.677, "50-Day Simple Moving Average" : -0.0824 }
{ "_id" : ObjectId("5285380fbb1177ca391c318e"), "Ticker" : "WHZ", "Profit Margin" : 0.982, "Institutional Ownership" : 0.199, "EPS growth past 5 years" : 0, "Total Debt/Equity" : 0, "Return on Assets" : 0.321, "Sector" : "Basic Materials", "P/S" : 4.79, "Change from Open" : -0.0042, "Performance (YTD)" : 0.0782, "Performance (Week)" : 0.0369, "P/B" : 1.67, "EPS growth quarter over quarter" : -0.337, "Payout Ratio" : 1.003, "Performance (Quarter)" : 0.0955, "P/E" : 4.88, "200-Day Simple Moving Average" : 0.0993, "Shares Outstanding" : 18.4, "52-Week High" : -0.0668, "P/Cash" : 1319.28, "Change" : -0.0042, "Analyst Recom" : 3, "Volatility (Week)" : 0.0183, "Country" : "USA", "Return on Equity" : 0.321, "50-Day Low" : 0.12, "Price" : 14.28, "50-Day High" : -0.0138, "Return on Investment" : 0.28, "Shares Float" : 18.4, "Dividend Yield" : 0.2064, "Industry" : "Independent Oil & Gas", "Sales growth quarter over quarter" : -0.343, "Operating Margin" : 0.982, "EPS (ttm)" : 2.94, "Float Short" : 0.004, "52-Week Low" : 0.2081, "Average True Range" : 0.26, "Company" : "Whiting USA Trust II", "Gap" : 0, "Relative Volume" : 2.18, "Volatility (Month)" : 0.0194, "Market Cap" : 263.86, "Volume" : 244298, "Short Ratio" : 0.6, "Performance (Half Year)" : 0.1282, "Relative Strength Index (14)" : 68.85, "20-Day Simple Moving Average" : 0.0301, "Performance (Month)" : 0.0864, "Institutional Transactions" : 0.0834, "Performance (Year)" : -0.0311, "LT Debt/Equity" : 0, "Average Volume" : 123.73, "50-Day Simple Moving Average" : 0.0734 }
{ "_id" : ObjectId("52853808bb1177ca391c27bd"), "Ticker" : "MVO", "Profit Margin" : 0.976, "Institutional Ownership" : 0.048, "EPS growth past 5 years" : 0.044, "Total Debt/Equity" : 0, "Return on Assets" : 1.258, "Sector" : "Basic Materials", "P/S" : 8.25, "Change from Open" : 0.0176, "Performance (YTD)" : 0.2883, "Performance (Week)" : -0.0007, "P/B" : 11.04, "EPS growth quarter over quarter" : -0.147, "Payout Ratio" : 1, "Performance (Quarter)" : 0.0678, "P/E" : 8.43, "200-Day Simple Moving Average" : 0.0422, "Shares Outstanding" : 11.5, "Earnings Date" : ISODate("2013-11-11T05:00:00Z"), "52-Week High" : -0.0998, "Change" : 0.0131, "Analyst Recom" : 4, "Volatility (Week)" : 0.0108, "Country" : "USA", "Return on Equity" : 1.258, "50-Day Low" : 0.0765, "Price" : 27.75, "50-Day High" : -0.0611, "Return on Investment" : 1.355, "Shares Float" : 8.63, "Dividend Yield" : 0.1431, "EPS growth next 5 years" : 0.07, "Industry" : "Oil & Gas Drilling & Exploration", "Beta" : 0.45, "Sales growth quarter over quarter" : -0.143, "Operating Margin" : 0.979, "EPS (ttm)" : 3.25, "PEG" : 1.2, "Float Short" : 0.0123, "52-Week Low" : 0.3994, "Average True Range" : 0.54, "Sales growth past 5 years" : 0.043, "Company" : "MV Oil Trust", "Gap" : -0.0044, "Relative Volume" : 0.36, "Volatility (Month)" : 0.0202, "Market Cap" : 314.98, "Volume" : 14403, "Short Ratio" : 2.44, "Performance (Half Year)" : 0.0367, "Relative Strength Index (14)" : 55.11, "Insider Ownership" : 0.25, "20-Day Simple Moving Average" : 0.0181, "Performance (Month)" : 0.0092, "Institutional Transactions" : -0.0054, "Performance (Year)" : 0.2008, "LT Debt/Equity" : 0, "Average Volume" : 43.54, "EPS growth this year" : 0.029, "50-Day Simple Moving Average" : 0.0058 }
{ "_id" : ObjectId("52853801bb1177ca391c1895"), "Ticker" : "AGNC", "Profit Margin" : 0.972, "Institutional Ownership" : 0.481, "EPS growth past 5 years" : -0.0107, "Total Debt/Equity" : 8.56, "Return on Assets" : 0.022, "Sector" : "Financial", "P/S" : 3.77, "Change from Open" : 0.0102, "Performance (YTD)" : -0.1652, "Performance (Week)" : -0.017, "Insider Transactions" : 0.4931, "P/B" : 0.86, "EPS growth quarter over quarter" : -8.2, "Payout Ratio" : 0.79, "Performance (Quarter)" : -0.0083, "Forward P/E" : 7.64, "P/E" : 3.68, "200-Day Simple Moving Average" : -0.1282, "Shares Outstanding" : 390.6, "Earnings Date" : ISODate("2013-10-28T20:30:00Z"), "52-Week High" : -0.2938, "P/Cash" : 3.93, "Change" : 0.0131, "Analyst Recom" : 2.6, "Volatility (Week)" : 0.0268, "Country" : "USA", "Return on Equity" : 0.205, "50-Day Low" : 0.0695, "Price" : 21.71, "50-Day High" : -0.1066, "Return on Investment" : 0.015, "Shares Float" : 383.97, "Dividend Yield" : 0.1493, "EPS growth next 5 years" : 0.035, "Industry" : "REIT - Residential", "Beta" : 0.51, "Sales growth quarter over quarter" : 0.073, "Operating Margin" : 0.67, "EPS (ttm)" : 5.82, "PEG" : 1.05, "Float Short" : 0.0311, "52-Week Low" : 0.1117, "Average True Range" : 0.52, "EPS growth next year" : -0.3603, "Company" : "American Capital Agency Corp.", "Gap" : 0.0028, "Relative Volume" : 0.71, "Volatility (Month)" : 0.02, "Market Cap" : 8370.56, "Volume" : 4576064, "Gross Margin" : 0.746, "Short Ratio" : 1.69, "Performance (Half Year)" : -0.2136, "Relative Strength Index (14)" : 43.53, "Insider Ownership" : 0.003, "20-Day Simple Moving Average" : -0.0318, "Performance (Month)" : -0.042, "Institutional Transactions" : 0.0077, "Performance (Year)" : -0.1503, "LT Debt/Equity" : 0, "Average Volume" : 7072.83, "EPS growth this year" : -0.169, "50-Day Simple Moving Average" : -0.0376 }
{ "_id" : ObjectId("5285380ebb1177ca391c3101"), "Ticker" : "VOC", "Profit Margin" : 0.971, "Institutional Ownership" : 0.161, "EPS growth past 5 years" : 0, "Total Debt/Equity" : 0, "Return on Assets" : 0.253, "Sector" : "Basic Materials", "P/S" : 9.03, "Change from Open" : -0.0129, "Performance (YTD)" : 0.4186, "Performance (Week)" : 0.0103, "P/B" : 2.44, "EPS growth quarter over quarter" : -0.304, "Payout Ratio" : 1, "Performance (Quarter)" : 0.1116, "P/E" : 9.3, "200-Day Simple Moving Average" : 0.2104, "Shares Outstanding" : 17, "52-Week High" : -0.0417, "P/Cash" : 948.6, "Change" : 0.0024, "Analyst Recom" : 3, "Volatility (Week)" : 0.0289, "Country" : "USA", "Return on Equity" : 0.253, "50-Day Low" : 0.1106, "Price" : 16.78, "50-Day High" : -0.0417, "Return on Investment" : 0.304, "Shares Float" : 12.75, "Dividend Yield" : 0.1266, "Industry" : "Independent Oil & Gas", "Sales growth quarter over quarter" : -0.286, "Operating Margin" : 0.971, "EPS (ttm)" : 1.8, "Float Short" : 0.006, "52-Week Low" : 0.529, "Average True Range" : 0.47, "Company" : "VOC Energy Trust", "Gap" : 0.0155, "Relative Volume" : 0.47, "Volatility (Month)" : 0.0292, "Market Cap" : 284.58, "Volume" : 32718, "Short Ratio" : 0.98, "Performance (Half Year)" : 0.2847, "Relative Strength Index (14)" : 54.66, "Insider Ownership" : 0.3505, "20-Day Simple Moving Average" : 0.009, "Performance (Month)" : 0.0582, "Institutional Transactions" : -0.0349, "Performance (Year)" : 0.3892, "LT Debt/Equity" : 0, "Average Volume" : 77.47, "EPS growth this year" : 0.542, "50-Day Simple Moving Average" : 0.0418 }
{ "_id" : ObjectId("52853807bb1177ca391c279a"), "Ticker" : "MTR", "Profit Margin" : 0.97, "Institutional Ownership" : 0.024, "EPS growth past 5 years" : -0.217, "Total Debt/Equity" : 0, "Return on Assets" : 0.518, "Sector" : "Financial", "P/S" : 12.1, "Change from Open" : -0.0038, "Performance (YTD)" : 0.1833, "Performance (Week)" : -0.0241, "P/B" : 7.82, "EPS growth quarter over quarter" : -0.255, "Payout Ratio" : 0.997, "Performance (Quarter)" : 0.0156, "P/E" : 12.68, "200-Day Simple Moving Average" : -0.0568, "Shares Outstanding" : 1.86, "Earnings Date" : ISODate("2013-11-11T05:00:00Z"), "52-Week High" : -0.1539, "P/Cash" : 23.5, "Change" : -0.0135, "Volatility (Week)" : 0.018, "Country" : "USA", "Return on Equity" : 0.593, "50-Day Low" : 0.0168, "Price" : 21.14, "50-Day High" : -0.1062, "Return on Investment" : 0.655, "Shares Float" : 1.86, "Dividend Yield" : 0.0845, "Industry" : "Diversified Investments", "Beta" : 0.93, "Sales growth quarter over quarter" : -0.222, "Operating Margin" : 0.939, "EPS (ttm)" : 1.69, "Float Short" : 0.0004, "52-Week Low" : 0.2026, "Average True Range" : 0.53, "Sales growth past 5 years" : -0.208, "Company" : "Mesa Royalty Trust", "Gap" : -0.0098, "Relative Volume" : 1.14, "Volatility (Month)" : 0.0226, "Market Cap" : 39.95, "Volume" : 4150, "Short Ratio" : 0.2, "Performance (Half Year)" : -0.1221, "Relative Strength Index (14)" : 34.54, "Insider Ownership" : 0.0385, "20-Day Simple Moving Average" : -0.0408, "Performance (Month)" : -0.0294, "Institutional Transactions" : -0.4527, "Performance (Year)" : 0.0418, "LT Debt/Equity" : 0, "Average Volume" : 3.97, "EPS growth this year" : -0.348, "50-Day Simple Moving Average" : -0.0539 }
{ "_id" : ObjectId("52853809bb1177ca391c2946"), "Ticker" : "OLP", "Profit Margin" : 0.97, "Institutional Ownership" : 0.481, "EPS growth past 5 years" : 0.008, "Total Debt/Equity" : 0.91, "Return on Assets" : 0.072, "Sector" : "Financial", "P/S" : 8.28, "Change from Open" : 0.0072, "Performance (YTD)" : 0.0398, "Performance (Week)" : -0.0156, "Insider Transactions" : 0.0039, "P/B" : 1.2, "EPS growth quarter over quarter" : 1.261, "Payout Ratio" : 0.456, "Performance (Quarter)" : -0.0804, "Forward P/E" : 10.48, "P/E" : 22.12, "200-Day Simple Moving Average" : -0.0742, "Shares Outstanding" : 14.84, "Earnings Date" : ISODate("2013-05-06T04:00:00Z"), "52-Week High" : -0.2453, "P/Cash" : 7.31, "Change" : 0.0077, "Analyst Recom" : 3, "Volatility (Week)" : 0.0166, "Country" : "USA", "Return on Equity" : 0.146, "50-Day Low" : 0.027, "Price" : 20.28, "50-Day High" : -0.1166, "Return on Investment" : 0.051, "Shares Float" : 13.88, "Dividend Yield" : 0.0695, "EPS growth next 5 years" : 0.111, "Industry" : "REIT - Diversified", "Beta" : 2.2, "Sales growth quarter over quarter" : 0.099, "Operating Margin" : 0.537, "EPS (ttm)" : 0.91, "PEG" : 1.99, "Float Short" : 0.0126, "52-Week Low" : 0.2285, "Average True Range" : 0.45, "EPS growth next year" : 0.171, "Sales growth past 5 years" : 0.06, "Company" : "One Liberty Properties Inc.", "Gap" : 0.0005, "Relative Volume" : 0.2, "Volatility (Month)" : 0.023, "Market Cap" : 298.81, "Volume" : 6907, "Gross Margin" : 0.983, "Short Ratio" : 4.64, "Performance (Half Year)" : -0.2219, "Relative Strength Index (14)" : 37.17, "Insider Ownership" : 0.158, "20-Day Simple Moving Average" : -0.0315, "Performance (Month)" : -0.0455, "Institutional Transactions" : 0.0003, "Performance (Year)" : 0.1663, "LT Debt/Equity" : 0.91, "Average Volume" : 37.56, "EPS growth this year" : -0.013, "50-Day Simple Moving Average" : -0.0356 }

4. Qual foi o setor mais rentável?
- db.stocks.aggregate([{$group: {_id: "$Sector", profit: {$avg: "$Profit Margin"}}}, {$sort: {profit: -1}}, {$limit: 1}])
{ "_id" : "Financial", "profit" : 0.16467639311043566 }

5. Ordene as ações pelo profit e usando um cursor, liste as ações.
- var myCursor = db.stocks.find({}).sort({"Profit Margin": -1});
  (executou)
  
- while (myCursor.hasNext()) { print(tojson(myCursor.next())); }
{
        "_id" : ObjectId("52853801bb1177ca391c1af3"),
        "Ticker" : "BPT",
        "Profit Margin" : 0.994,
        "Institutional Ownership" : 0.098,
        "EPS growth past 5 years" : 0.025,
        "Total Debt/Equity" : 0,
        "Sector" : "Basic Materials",
        "P/S" : 8.81,
        "Change from Open" : 0.0125,
        "Performance (YTD)" : 0.2758,
        "Performance (Week)" : -0.018,
        "P/B" : 2620,
        "EPS growth quarter over quarter" : -0.087,
        "Payout Ratio" : 1.001,
        "Performance (Quarter)" : -0.0556,
        "P/E" : 8.87,
        "200-Day Simple Moving Average" : -0.0305,
        "Shares Outstanding" : 21.4,
        "Earnings Date" : ISODate("2013-11-11T05:00:00Z"),
        "52-Week High" : -0.159,
        "P/Cash" : 1682.04,
        "Change" : 0.0064,
        "Volatility (Week)" : 0.0151,
        "Country" : "USA",
        "50-Day Low" : 0.0136,
        "Price" : 79.1,
        "50-Day High" : -0.0973,
        "Shares Float" : 21.4,
        "Dividend Yield" : 0.1103,
        "Industry" : "Oil & Gas Refining & Marketing",
        "Beta" : 0.77,
        "Sales growth quarter over quarter" : -0.086,
        "Operating Margin" : 0.994,
        "EPS (ttm)" : 8.86,
        "Float Short" : 0.0173,
        "52-Week Low" : 0.3422,
        "Average True Range" : 1.37,
        "Sales growth past 5 years" : 0.024,
        "Company" : "BP Prudhoe Bay Royalty Trust",
        "Gap" : -0.0061,
        "Relative Volume" : 0.93,
        "Volatility (Month)" : 0.016,
        "Market Cap" : 1682.04,
        "Volume" : 71575,
        "Short Ratio" : 4.41,
        "Performance (Half Year)" : 0.0022,
        "Relative Strength Index (14)" : 38.01,
        "20-Day Simple Moving Average" : -0.0318,
        "Performance (Month)" : -0.079,
        "Institutional Transactions" : -0.0057,
        "Performance (Year)" : 0.1837,
        "LT Debt/Equity" : 0,
        "Average Volume" : 84.15,
        "EPS growth this year" : -0.012,
        "50-Day Simple Moving Average" : -0.0496
}
{
        "_id" : ObjectId("52853802bb1177ca391c1b69"),
        "Ticker" : "CACB",
        "Profit Margin" : 0.994,
        "Institutional Ownership" : 0.547,
        "EPS growth past 5 years" : -0.584,
        "Total Debt/Equity" : 0,
        "Return on Assets" : 0.039,
        "Sector" : "Financial",
        "P/S" : 4.66,
        "Change from Open" : -0.0137,
        "Performance (YTD)" : -0.1869,
        "Performance (Week)" : 0.0079,
        "Insider Transactions" : 1.0755,
        "P/B" : 1.28,
        "EPS growth quarter over quarter" : 25.422,
        "Payout Ratio" : 0,
        "Performance (Quarter)" : -0.1314,
        "Forward P/E" : 42.42,
        "P/E" : 4.71,
        "200-Day Simple Moving Average" : -0.1709,
        "Shares Outstanding" : 47.17,
        "Earnings Date" : ISODate("2013-11-13T21:30:00Z"),
        "52-Week High" : -0.2994,
        "P/Cash" : 2.26,
        "Change" : -0.0118,
        "Analyst Recom" : 3,
        "Volatility (Week)" : 0.0353,
        "Country" : "USA",
        "Return on Equity" : 0.336,
        "50-Day Low" : 0.006,
        "Price" : 5.03,
        "50-Day High" : -0.2066,
        "Return on Investment" : 0.346,
        "Shares Float" : 40.67,
        "EPS growth next 5 years" : 0.05,
        "Industry" : "Regional - Pacific Banks",
        "Beta" : 2.34,
        "Sales growth quarter over quarter" : -0.101,
        "Operating Margin" : 0.027,
        "EPS (ttm)" : 1.08,
        "PEG" : 0.94,
        "Float Short" : 0.0088,
        "52-Week Low" : 0.0817,
        "Average True Range" : 0.19,
        "EPS growth next year" : -0.8904,
        "Sales growth past 5 years" : -0.203,
        "Company" : "Cascade Bancorp",
        "Gap" : 0.002,
        "Relative Volume" : 1.35,
        "Volatility (Month)" : 0.0399,
        "Market Cap" : 240.11,
        "Volume" : 21432,
        "Short Ratio" : 20.55,
        "Performance (Half Year)" : -0.1239,
        "Relative Strength Index (14)" : 29.61,
        "Insider Ownership" : 0.009,
        "20-Day Simple Moving Average" : -0.0729,
        "Performance (Month)" : -0.1039,
        "Institutional Transactions" : 0.0004,
        "Performance (Year)" : 0.0241,
        "LT Debt/Equity" : 0,
        "Average Volume" : 17.39,
        "EPS growth this year" : 1.12,
        "50-Day Simple Moving Average" : -0.116
}
(Dois primeiros registros)   

   
6. Renomeie o campo “Profit Margin” para apenas “profit”.
- db.stocks.update({}, {$rename: {"Profit Margin": "profit"}}, {multi: true});
WriteResult({ "nMatched" : 6756, "nUpserted" : 0, "nModified" : 4302 })

7. Agora liste apenas a empresa e seu respectivo resultado
- db.stocks.aggregate([{$group: {_id: "$Company", profit: {$avg: "$profit"}}}])
{ "_id" : "Heska Corp.", "profit" : -0.032 }
{ "_id" : "Consolidated Communications Holdings Inc.", "profit" : 0.047 }
{ "_id" : "Gray Television Inc.", "profit" : 0.046 }
(três primeiros registros)

8. Analise as ações. É uma bola de cristal na sua mão... Quais as três ações você investiria?
- db.stocks.find({}).sort({"EPS growth next 5 years": -1}).limit(3)
{ "_id" : ObjectId("52853807bb1177ca391c265a"), "Ticker" : "LYG", "Institutional Ownership" : 0.004, "EPS growth past 5 years" : -0.3745, "Total Debt/Equity" : 3.24, "Return on Assets" : 0.002, "Sector" : "Financial", "P/S" : 2.5, "Change from Open" : 0.0082, "Performance (YTD)" : 0.5281, "Performance (Week)" : 0.0103, "P/B" : 1.24, "EPS growth quarter over quarter" : 3.333, "Payout Ratio" : 0, "Performance (Quarter)" : 0.0449, "Forward P/E" : 10.63, "P/E" : 69.86, "200-Day Simple Moving Average" : 0.2397, "Shares Outstanding" : 17668, "Earnings Date" : ISODate("2008-07-30T04:00:00Z"), "52-Week High" : -0.0801, "P/Cash" : 0.26, "Change" : 0.0102, "Analyst Recom" : 1, "Volatility (Week)" : 0.0187, "Country" : "United Kingdom", "Return on Equity" : 0.045, "50-Day Low" : 0.0647, "Price" : 4.94, "50-Day High" : -0.0801, "Return on Investment" : 0.016, "Shares Float" : 10834.48, "EPS growth next 5 years" : 0.796, "Industry" : "Foreign Money Center Banks", "Beta" : 2.37, "Sales growth quarter over quarter" : -0.156, "Operating Margin" : 0.776, "EPS (ttm)" : 0.07, "PEG" : 0.88, "Float Short" : 0.0017, "52-Week Low" : 0.7964, "Average True Range" : 0.11, "EPS growth next year" : 0.2778, "Sales growth past 5 years" : 0.069, "Company" : "Lloyds Banking Group plc", "Gap" : 0.002, "Relative Volume" : 0.63, "Volatility (Month)" : 0.0174, "Market Cap" : 86396.52, "Volume" : 2740693, "Short Ratio" : 3.78, "Performance (Half Year)" : 0.3145, "Relative Strength Index (14)" : 47.77, "20-Day Simple Moving Average" : -0.0191, "Performance (Month)" : -0.0101, "Institutional Transactions" : 0.0316, "Performance (Year)" : 0.6747, "LT Debt/Equity" : 3.24, "Average Volume" : 4776.1, "EPS growth this year" : -2.25, "50-Day Simple Moving Average" : 0.0025, "profit" : 0.091 }
{ "_id" : ObjectId("5285380ebb1177ca391c300d"), "Ticker" : "UCP", "Institutional Ownership" : 0.457, "EPS growth past 5 years" : 0, "Total Debt/Equity" : 0.31, "Return on Assets" : 0, "Sector" : "Financial", "P/S" : 1.26, "Change from Open" : -0.0163, "Performance (YTD)" : 0.0757, "Performance (Week)" : 0.0749, "P/B" : 1.07, "EPS growth quarter over quarter" : 0, "Performance (Quarter)" : 0.0905, "Forward P/E" : 30.73, "200-Day Simple Moving Average" : 0.0653, "Shares Outstanding" : 7.75, "Earnings Date" : ISODate("2013-09-03T21:00:00Z"), "52-Week High" : -0.0157, "P/Cash" : 64.84, "Change" : 0.002, "Analyst Recom" : 2, "Volatility (Week)" : 0.0452, "Country" : "USA", "Return on Equity" : 0, "50-Day Low" : 0.1554, "Price" : 15.09, "50-Day High" : -0.0157, "Return on Investment" : 0.018, "Shares Float" : 7.44, "EPS growth next 5 years" : 0.7605, "Industry" : "Property Management", "Sales growth quarter over quarter" : 6.914, "Operating Margin" : 0.041, "EPS (ttm)" : 0, "Float Short" : 0.0282, "52-Week Low" : 0.1698, "Average True Range" : 0.46, "EPS growth next year" : 8.8, "Company" : "UCP, Inc.", "Gap" : 0.0186, "Relative Volume" : 1.01, "Volatility (Month)" : 0.0322, "Market Cap" : 116.72, "Volume" : 84109, "Gross Margin" : 0.257, "Short Ratio" : 2.27, "Relative Strength Index (14)" : 60.44, "Insider Ownership" : 0.041, "20-Day Simple Moving Average" : 0.0484, "Performance (Month)" : 0.0252, "LT Debt/Equity" : 0.31, "Average Volume" : 92.35, "EPS growth this year" : 0, "50-Day Simple Moving Average" : 0.0443, "profit" : 0 }
{ "_id" : ObjectId("5285380abb1177ca391c2be8"), "Ticker" : "RGP", "Institutional Ownership" : 0.523, "EPS growth past 5 years" : 0.184, "Total Debt/Equity" : 0.61, "Current Ratio" : 0.8, "Return on Assets" : 0.004, "Sector" : "Basic Materials", "P/S" : 2.53, "Change from Open" : 0.0021, "Performance (YTD)" : 0.2033, "Performance (Week)" : -0.0445, "Quick Ratio" : 0.8, "P/B" : 1.03, "EPS growth quarter over quarter" : 5.75, "Performance (Quarter)" : -0.1087, "Forward P/E" : 52.42, "P/E" : 202.25, "200-Day Simple Moving Average" : -0.0368, "Shares Outstanding" : 209.56, "Earnings Date" : ISODate("2013-11-05T21:30:00Z"), "52-Week High" : -0.1575, "Change" : 0.0062, "Analyst Recom" : 2.7, "Volatility (Week)" : 0.0181, "Country" : "USA", "Return on Equity" : 0.007, "50-Day Low" : 0.0095, "Price" : 24.42, "50-Day High" : -0.1575, "Return on Investment" : 0.006, "Shares Float" : 144.55, "Dividend Yield" : 0.0775, "EPS growth next 5 years" : 0.76, "Industry" : "Oil & Gas Pipelines", "Beta" : 0.42, "Sales growth quarter over quarter" : 1.119, "Operating Margin" : 0.033, "EPS (ttm)" : 0.12, "PEG" : 2.66, "Float Short" : 0.0218, "52-Week Low" : 0.2749, "Average True Range" : 0.53, "EPS growth next year" : 0.7808, "Sales growth past 5 years" : 0.024, "Company" : "Regency Energy Partners LP", "Gap" : 0.0041, "Relative Volume" : 1.25, "Volatility (Month)" : 0.0164, "Market Cap" : 5086.02, "Volume" : 661161, "Gross Margin" : 0.308, "Short Ratio" : 5.4, "Performance (Half Year)" : -0.0226, "Relative Strength Index (14)" : 34.98, "Insider Ownership" : 0.327, "20-Day Simple Moving Average" : -0.034, "Performance (Month)" : -0.0384, "Institutional Transactions" : 0.0157, "Performance (Year)" : 0.1747, "LT Debt/Equity" : 0.61, "Average Volume" : 585, "EPS growth this year" : -0.594, "50-Day Simple Moving Average" : -0.0744, "profit" : 0.014 }

- Investiria nas 3 ações acima

9. Liste as ações agrupadas por setor
- db.stocks.find({}).sort({"Sector": 1})
{ "_id" : ObjectId("52853800bb1177ca391c1800"), "Ticker" : "AA", "Institutional Ownership" : 0.599, "EPS growth past 5 years" : -0.439, "Total Debt/Equity" : 0.65, "Current Ratio" : 1.2, "Return on Assets" : 0.008, "Sector" : "Basic Materials", "P/S" : 0.41, "Change from Open" : -0.0022, "Performance (YTD)" : 0.0502, "Performance (Week)" : -0.0694, "Quick Ratio" : 0.7, "Insider Transactions" : 0.1031, "P/B" : 0.75, "EPS growth quarter over quarter" : 1.143, "Payout Ratio" : 0.429, "Performance (Quarter)" : 0.1058, "Forward P/E" : 21.35, "P/E" : 35.96, "200-Day Simple Moving Average" : 0.0823, "Shares Outstanding" : 1070, "Earnings Date" : ISODate("2013-10-08T20:30:00Z"), "52-Week High" : -0.0925, "P/Cash" : 9.46, "Change" : 0.0033, "Analyst Recom" : 3.1, "Volatility (Week)" : 0.0345, "Country" : "USA", "Return on Equity" : 0.023, "50-Day Low" : 0.1579, "Price" : 9.02, "50-Day High" : -0.0925, "Return on Investment" : 0.007, "Shares Float" : 1068.5, "Dividend Yield" : 0.0133, "EPS growth next 5 years" : 0.1747, "Industry" : "Aluminum", "Beta" : 2.02, "Sales growth quarter over quarter" : -0.012, "Operating Margin" : 0.049, "EPS (ttm)" : 0.25, "PEG" : 2.06, "Float Short" : 0.1129, "52-Week Low" : 0.1899, "Average True Range" : 0.3, "EPS growth next year" : 0.231, "Sales growth past 5 years" : -0.041, "Company" : "Alcoa, Inc.", "Gap" : 0.0056, "Relative Volume" : 0.6, "Volatility (Month)" : 0.0336, "Market Cap" : 9619.3, "Volume" : 14600992, "Gross Margin" : 0.163, "Short Ratio" : 4.51, "Performance (Half Year)" : 0.0652, "Relative Strength Index (14)" : 49.61, "Insider Ownership" : 0.0007, "20-Day Simple Moving Average" : -0.0192, "Performance (Month)" : 0.0766, "P/Free Cash Flow" : 33.17, "Institutional Transactions" : 0.0252, "Performance (Year)" : 0.0963, "LT Debt/Equity" : 0.6, "Average Volume" : 26728.11, "EPS growth this year" : -0.673, "50-Day Simple Moving Average" : 0.052, "profit" : 0.013 }
{ "_id" : ObjectId("52853800bb1177ca391c180b"), "Ticker" : "AAU", "Institutional Ownership" : 0.059, "EPS growth past 5 years" : -0.232, "Total Debt/Equity" : 0, "Current Ratio" : 44.8, "Return on Assets" : -0.207, "Sector" : "Basic Materials", "P/S" : 250.21, "Change from Open" : -0.0159, "Performance (YTD)" : -0.6057, "Performance (Week)" : -0.0385, "Quick Ratio" : 44, "P/B" : 1.58, "EPS growth quarter over quarter" : 0.333, "Performance (Quarter)" : -0.399, "200-Day Simple Moving Average" : -0.2745, "Shares Outstanding" : 60.05, "52-Week High" : -0.6242, "P/Cash" : 4.78, "Change" : -0.008, "Volatility (Week)" : 0.0617, "Country" : "Canada", "Return on Equity" : -0.209, "50-Day Low" : 0.0333, "Price" : 1.24, "50-Day High" : -0.2994, "Return on Investment" : -0.203, "Shares Float" : 52.97, "Industry" : "Gold", "Beta" : 0.43, "EPS (ttm)" : -0.16, "Float Short" : 0.0093, "52-Week Low" : 0.1273, "Average True Range" : 0.06, "Sales growth past 5 years" : -0.156, "Company" : "Almaden Minerals Ltd.", "Gap" : 0.008, "Relative Volume" : 0.32, "Volatility (Month)" : 0.0468, "Market Cap" : 75.06, "Volume" : 34762, "Short Ratio" : 4.14, "Performance (Half Year)" : -0.1935, "Relative Strength Index (14)" : 36.92, "Insider Ownership" : 0.0536, "20-Day Simple Moving Average" : -0.0722, "Performance (Month)" : 0.0246, "Institutional Transactions" : 1.7402, "Performance (Year)" : -0.5117, "LT Debt/Equity" : 0, "Average Volume" : 119.04, "EPS growth this year" : -2.417, "50-Day Simple Moving Average" : -0.1017 }
{ "_id" : ObjectId("52853800bb1177ca391c180c"), "Ticker" : "AAV", "Institutional Ownership" : 0.58, "EPS growth past 5 years" : -0.265, "Total Debt/Equity" : 0.32, "Current Ratio" : 0.8, "Return on Assets" : -0.032, "Sector" : "Basic Materials", "P/S" : 2.64, "Change from Open" : 0.0286, "Performance (YTD)" : 0.1914, "Performance (Week)" : 0.0158, "Quick Ratio" : 0.8, "P/B" : 0.63, "EPS growth quarter over quarter" : 1.556, "Performance (Quarter)" : 0.0349, "200-Day Simple Moving Average" : 0.0569, "Shares Outstanding" : 168.38, "Earnings Date" : ISODate("2011-03-16T04:00:00Z"), "52-Week High" : -0.1242, "Change" : 0.0233, "Analyst Recom" : 2.7, "Volatility (Week)" : 0.0381, "Country" : "Canada", "Return on Equity" : -0.055, "50-Day Low" : 0.1127, "Price" : 3.95, "50-Day High" : -0.0436, "Return on Investment" : -0.068, "Shares Float" : 167.07, "Industry" : "Oil & Gas Drilling & Exploration", "Beta" : 2.05, "Sales growth quarter over quarter" : 0.399, "Operating Margin" : 0.102, "EPS (ttm)" : -0.34, "Float Short" : 0.0008, "52-Week Low" : 0.4158, "Average True Range" : 0.12, "EPS growth next year" : -0.667, "Sales growth past 5 years" : -0.121, "Company" : "Advantage Oil & Gas Ltd.", "Gap" : -0.0052, "Relative Volume" : 0.85, "Volatility (Month)" : 0.0303, "Market Cap" : 649.96, "Volume" : 116750, "Gross Margin" : 0.682, "Short Ratio" : 0.89, "Performance (Half Year)" : 0.0078, "Relative Strength Index (14)" : 52.62, "Insider Ownership" : 0.0025, "20-Day Simple Moving Average" : -0.0001, "Performance (Month)" : 0.0158, "Institutional Transactions" : 0.0402, "Performance (Year)" : 0.1386, "LT Debt/Equity" : 0.32, "Average Volume" : 149.81, "EPS growth this year" : 0.42, "50-Day Simple Moving Average" : 0.023, "profit" : -0.232 }
(3 primeiros registos)

# Exercício 3 – Fraude na Enron!

1. Liste as pessoas que enviaram e-mails (de forma distinta, ou seja, sem repetir). Quantas pessoas são?
- db.enron.aggregate({$group: {_id: "$sender"}})
{ "_id" : "theweblion@hotmail.com" }
{ "_id" : "siukkuk@aol.com" }
{ "_id" : "gayla.seiter@enron.com" }
(3 primeiros registos)

2. Contabilize quantos e-mails tem a palavra “fraud”
- db.stocks.find({"$or": [{text: /fraud/}, {subject: /fraud/}]}).count()
23
