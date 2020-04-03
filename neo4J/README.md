# Pos-Datascience

# Exercício 1 - Retrieving Nodes

Coloque os comandos utilizado em cada item a seguir:

• Exercise 1.1: Retrieve all nodes from the database.
  - MATCH(n) return n;
  
• Exercise 1.2: Examine the data model for the graph.
  - CALL db.schema();

• Exercise 1.3: Retrieve all Person nodes.
  - MATCH(n:Person) return n;

• Exercise 1.4: Retrieve all Movie nodes.
  - MATCH(n:Movie) return n;


# Exercício 2 – Filtering queries using property values

Coloque os comandos utilizado em cada item a seguir:

• Exercise 2.1: Retrieve all movies that were released in a specific year.
  - MATCH(n:Movie {released:2003}) return n;
   
• Exercise 2.2: View the retrieved results as a table.
  - Exercicio 2-2 2-2.png

• Exercise 2.3: Query the database for all property keys.
  - CALL db.propertyKeys;
  
• Exercise 2.4: Retrieve all Movies released in a specific year, returning their titles.
  - match(n:Movie {released:2006}) return n.title;
  
• Exercise 2.5: Display title, released, and tagline values for every Movie node in the graph.
  match(n:Movie) return n.title, n.released, n.tagline;
  
• Exercise 2.6: Display more user-friendly headers in the table
  - MATCH (m:Movie) RETURN m.title AS `Título do filme`, m.released AS `Ano de lançamento`, m.tagline AS `Slogan`;
  
  
# Exercício 3 - Filtering queries using relationships

Coloque os comandos utilizado em cada item a seguir:

• Exercise 3.1: Display the schema of the database.
  - CALL db.schema();
  
• Exercise 3.2: Retrieve all people who wrote the movie Speed Racer.
  - MATCH (p:Person)-[:WROTE]->(:Movie {title: 'Speed Racer'}) RETURN p.name;

• Exercise 3.3: Retrieve all movies that are connected to the person, Tom Hanks.
  - MATCH (m:Movie)<--(:Person {name: 'Tom Hanks'}) RETURN m.title;

• Exercise 3.4: Retrieve information about the relationships Tom Hanks had with the set of movies retrieved earlier.
  - MATCH (m:Movie)-[rel]-(:Person {name: 'Tom Hanks'}) RETURN m.title, type(rel);

• Exercise 3.5: Retrieve information about the roles that Tom Hanks acted in.
  - MATCH (m:Movie)-[rel:ACTED_IN]-(p:Person {name: 'Tom Hanks'}) RETURN m.title, rel.roles;
  
  
# Exercício 4 – Filtering queries using WHERE clause

Coloque os comandos utilizado em cada item a seguir:

• Exercise 4.1: Retrieve all movies that Tom Cruise acted in.
  - MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE p.name = 'Tom Cruise' RETURN m.title;

• Exercise 4.2: Retrieve all people that were born in the 70’s.
  - MATCH (p:Person) WHERE p.born >= 1970 and p.born < 1980 RETURN p.name, p.born;

• Exercise 4.3: Retrieve the actors who acted in the movie The Matrix who were born after 1960.
  - MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE p.born > 1960 and m.title = 'The Matrix' RETURN p.name, p.born;

• Exercise 4.4: Retrieve all movies by testing the node label and a property.
  - MATCH (m:Movie) WHERE m.released = 2000 RETURN m.title;

• Exercise 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes.
  - MATCH (p:Person)-[:WROTE]->(m:Movie) RETURN p.name, m.title;

• Exercise 4.6: Retrieve all people in the graph that do not have a property.
  - MATCH (p:Person) WHERE not exists(p.born) RETURN p.name;

• Exercise 4.7: Retrieve all people related to movies where the relationship has a property.
  - MATCH (p:Person)-[rel]-(m:Movie) WHERE exists(rel.rating) RETURN p.name as `Pessoa`, m.title as `Filme`, rel.rating as `Rating`;

• Exercise 4.8: Retrieve all actors whose name begins with James.
  - MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WHERE p.name starts with 'James' RETURN distinct(p.name) as `Pessoa`;

• Exercise 4.9: Retrieve all all REVIEW relationships from the graph with filtered results.
  - MATCH (p:Person)-[r:REVIEWED]->(m:Movie) WHERE tolower(r.summary) contains 'fun' RETURN m.title as `Filme`, r.summary as Review, r.rating as Rating;

• Exercise 4.10: Retrieve all people who have produced a movie, but have not directed a movie.
  - MATCH (p:Person)-[:PRODUCED]->(m:Movie) WHERE NOT ((p)-[:DIRECTED]->(:Movie)) RETURN p.name, m.title;

• Exercise 4.11: Retrieve the movies and their actors where one of the actors also directed the movie.
  - MATCH (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2:Person) WHERE exists( (p2)-[:DIRECTED]->(m) ) RETURN p1.name as Ator, p2.name as `Ator/Diretor`, m.title as Filme;

• Exercise 4.12: Retrieve all movies that were released in a set of years.
  - MATCH(m:Movie) WHERE m.released in [2000, 2004, 2008] RETURN m.title, m.released;

• Exercise 4.13: Retrieve the movies that have an actor’s role that is the name of the movie.
  - MATCH (p:Person)-[r:ACTED_IN]->(m:Movie) WHERE m.title in r.roles RETURN  m.title as Filme, p.name as Ator; 

# Exercício 5 – Controlling query processing

Coloque os comandos utilizado em cada item a seguir:

• Exercise 5.1: Retrieve data using multiple MATCH patterns.
  - MATCH (a:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(d:Person), (a2:Person)-[:ACTED_IN]->(m) WHERE a.name = 'Gene Hackman' RETURN m.title as Filme, d.name AS Diretor , a2.name AS `Co-atores`;

• Exercise 5.2: Retrieve particular nodes that have a relationship.
  - MATCH(p1:Person)<-[:FOLLOWS]->(p2:Person) WHERE p1.name = 'James Thompson' RETURN p1, p2;

• Exercise 5.3: Modify the query to retrieve nodes that are exactly three hops away.
  - MATCH (p1:Person)-[:FOLLOWS*3]-(p2:Person) WHERE p1.name = 'James Thompson' RETURN p1, p2;

• Exercise 5.4: Modify the query to retrieve nodes that are one and two hops away.
  - MATCH (p1:Person)-[:FOLLOWS*1..2]-(p2:Person) WHERE p1.name = 'James Thompson' RETURN p1, p2;

• Exercise 5.5: Modify the query to retrieve particular nodes that are connected no matter how many hops are required.
  - MATCH (p1:Person)-[:FOLLOWS*]-(p2:Person) WHERE p1.name = 'James Thompson' RETURN p1, p2;

• Exercise 5.6: Specify optional data to be retrieved during the query.
  - MATCH (p:Person) WHERE p.name STARTS WITH 'Tom' OPTIONAL MATCH (p)-[:DIRECTED]->(m:Movie) RETURN p.name, m.title;

• Exercise 5.7: Retrieve nodes by collecting a list.
  - MATCH (p:Person)-[:ACTED_IN]->(m:Movie) RETURN p.name as actor, collect(m.title) AS `Filmes`;

  # (Não ter o 5.8 foi proposital ^^ ?)

• Exercise 5.9: Retrieve nodes as lists and return data associated with the corresponding lists.
  - MATCH (p:Person)-[:REVIEWED]->(m:Movie) RETURN m.title as Filme, count(p) as numReviews, collect(p.name) as Reviewers;

• Exercise 5.10: Retrieve nodes and their relationships as lists.
  - MATCH (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person) RETURN d.name AS Diretor, count(a) AS `Número de atores` , collect(a.name) AS `Actores com quem trabalhou`;

• Exercise 5.11: Retrieve the actors who have acted in exactly five movies.
  - MATCH (a:Person)-[:ACTED_IN]->(m:Movie) WITH  a, count(a) AS numFilmes, collect(m.title) AS filmes WHERE numFilmes = 5 RETURN a.name, filmes;

• Exercise 5.12: Retrieve the movies that have at least 2 directors with other optional data.
  - MATCH (m:Movie) WITH m, size((:Person)-[:DIRECTED]->(m)) AS directors WHERE directors >= 2 OPTIONAL MATCH (p:Person)-[:REVIEWED]->(m) RETURN  m.title, p.name;

# Exercício 6 – Controlling results returned

Coloque os comandos utilizado em cada item a seguir:

• Exercise 6.1: Execute a query that returns duplicate records.
  - MATCH (a:Person)-[:ACTED_IN]->(m:Movie) WHERE m.released >= 1990 AND m.released < 2000 RETURN DISTINCT m.released, m.title, collect(a.name);

• Exercise 6.2: Modify the query to eliminate duplication.
  - MATCH (a:Person)-[:ACTED_IN]->(m:Movie) WHERE m.released >= 1990 AND m.released < 2000 RETURN  m.released, collect(m.title), collect(a.name);

• Exercise 6.3: Modify the query to eliminate more duplication.
  - MATCH (a:Person)-[:ACTED_IN]->(m:Movie) WHERE m.released >= 1990 AND m.released < 2000 RETURN  m.released, collect(DISTINCT m.title), collect(a.name);

• Exercise 6.4: Sort results returned.
  - MATCH (a:Person)-[:ACTED_IN]->(m:Movie) WHERE m.released >= 1990 AND m.released < 2000 RETURN  m.released, collect(DISTINCT m.title), collect(a.name) ORDER BY m.released DESC;

• Exercise 6.5: Retrieve the top 5 ratings and their associated movies.    
  - MATCH (:Person)-[r:REVIEWED]->(m:Movie) RETURN  m.title AS movie, r.rating AS rating ORDER BY r.rating DESC LIMIT 5;
      
• Exercise 6.6: Retrieve all actors that have not appeared in more than 3 movies.      
  - MATCH (a:Person)-[:ACTED_IN]->(m:Movie) WITH  a,  count(a) AS numMovies, collect(m.title) AS movies WHERE numMovies <= 3 RETURN a.name, movies;      


# Exercício 7 – Working with cypher data

Coloque os comandos utilizado em cada item a seguir:

• Exercise 7.1: Collect and use lists.
  - MATCH (a:Person)-[:ACTED_IN]->(m:Movie), (m)<-[:PRODUCED]-(p:Person) WITH  m, collect(DISTINCT a.name) AS cast, collect(DISTINCT p.name) AS producers RETURN DISTINCT m.title, cast, producers ORDER BY size(cast);
 
• Exercise 7.2: Collect a list.
  - MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WITH p, collect(m) AS movies WHERE size(movies)  > 5 RETURN p.name, movies;
  
• Exercise 7.3: Unwind a list.
  - MATCH (p:Person)-[:ACTED_IN]->(m:Movie) WITH p, collect(m) AS movies WHERE size(movies)  > 5 WITH p, movies UNWIND movies AS movie RETURN p.name, movie.title;

• Exercise 7.4: Perform a calculation with the date type.
  - MATCH (a:Person)-[:ACTED_IN]->(m:Movie) WHERE a.name = 'Tom Hanks' RETURN  m.title, m.released, date().year  - m.released as yearsAgoReleased, m.released  - a.born AS `age of Tom` ORDER BY yearsAgoReleased;


# Exercício 8 – Creating nodes

Coloque os comandos utilizado em cada item a seguir:

• Exercise 8.1: Create a Movie node.
  - CREATE (:Movie {title: 'Forrest Gump'});

• Exercise 8.2: Retrieve the newly-created node.
  - MATCH (m:Movie) WHERE m.title = 'Forrest Gump' RETURN m;

• Exercise 8.3: Create a Person node.
  - CREATE (:Person {name: 'Robin Wright'});

• Exercise 8.4: Retrieve the newly-created node.
  - MATCH (p:Person) WHERE p.name = 'Robin Wright' RETURN p;

• Exercise 8.5: Add a label to a node.
  - MATCH (m:Movie) WHERE m.released < 2010 SET m:OlderMovie RETURN DISTINCT labels(m);

• Exercise 8.6: Retrieve the node using the new label.
  - MATCH (m:OlderMovie) RETURN m.title, m.released;

• Exercise 8.7: Add the Female label to selected nodes.
  - MATCH (p:Person) WHERE p.name STARTS WITH 'Robin' SET p:Female;

• Exercise 8.8: Retrieve all Female nodes.
  - MATCH (p:Female) RETURN p.name;

• Exercise 8.9: Remove the Female label from the nodes that have this label.
  - MATCH (p:Female) REMOVE p:Female;

• Exercise 8.10: View the current schema of the graph.
  - CALL db.schema;

• Exercise 8.11: Add properties to a movie.
- MATCH (m:Movie) WHERE m.title = 'Forrest Gump'
       
       SET m:OlderMovie,
       
           m.released = 1994,
           
           m.tagline = "Life is like a box of chocolates...you never know what you're gonna get.",
           
           m.lengthInMinutes = 142;

• Exercise 8.12: Retrieve an OlderMovie node to confirm the label and properties.
  - MATCH (m:OlderMovie) WHERE m.title = 'Forrest Gump' RETURN m;

• Exercise 8.13: Add properties to the person, Robin Wright.
  - MATCH (p:Person) WHERE p.name = 'Robin Wright' SET p.born = 1966, p.birthPlace = 'Dallas';

• Exercise 8.14: Retrieve an updated Person node.
  - MATCH (p:Person) WHERE p.name = 'Robin Wright' RETURN p;
  
• Exercise 8.15: Remove a property from a Movie node.
  - MATCH (m:Movie) WHERE m.title = 'Forrest Gump' SET m.lengthInMinutes = null;

• Exercise 8.16: Retrieve the node to confirm that the property has been removed.
  - MATCH (m:Movie) WHERE m.title = 'Forrest Gump' RETURN m;

• Exercise 8.17: Remove a property from a Person node.
  - MATCH (p:Person) WHERE p.name = 'Robin Wright' REMOVE p.birthPlace;

• Exercise 8.18: Retrieve the node to confirm that the property has been removed.
  - MATCH (p:Person) WHERE p.name = 'Robin Wright' RETURN p;



# Exercício 9 – Creating relationships

Coloque os comandos utilizado em cada item a seguir:

• Exercise 9.1: Create ACTED_IN relationships.
  - MATCH (m:Movie) WHERE m.title = 'Forrest Gump' MATCH (p:Person) WHERE p.name = 'Tom Hanks' OR p.name = 'Robin Wright' OR p.name = 'Gary Sinise' CREATE (p)-[:ACTED_IN]->(m);
  
• Exercise 9.2: Create DIRECTED relationships.
  - MATCH (m:Movie) WHERE m.title = 'Forrest Gump' MATCH (p:Person) WHERE p.name = 'Robert Zemeckis' CREATE (p)-[:DIRECTED]->(m);

• Exercise 9.3: Create a HELPED relationship.
  - MATCH (p1:Person) WHERE p1.name = 'Tom Hanks' MATCH (p2:Person) WHERE p2.name = 'Gary Sinise' CREATE (p1)-[:HELPED]->(p2);

• Exercise 9.4: Query nodes and new relationships.
  - MATCH (p:Person)-[rel]-(m:Movie) WHERE m.title = 'Forrest Gump' RETURN p, rel, m;

• Exercise 9.5: Add properties to relationships.
  - MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie) WHERE m.title = 'Forrest Gump'
      
      SET rel.roles =
      
      CASE p.name
      
        WHEN 'Tom Hanks' THEN ['Forrest Gump']
        
        WHEN 'Robin Wright' THEN ['Jenny Curran']
        
        WHEN 'Gary Sinise' THEN ['Lieutenant Dan Taylor']
        
      END;

• Exercise 9.6: Add a property to the HELPED relationship.
  - MATCH (p1:Person)-[rel:HELPED]->(p2:Person) WHERE p1.name = 'Tom Hanks' AND p2.name = 'Gary Sinise' SET rel.research = 'war history';

• Exercise 9.7: View the current list of property keys in the graph.
  - call db.propertyKeys;

• Exercise 9.8: View the current schema of the graph.
  - call db.schema;

• Exercise 9.9: Retrieve the names and roles for actors.
  - MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie) WHERE m.title = 'Forrest Gump' RETURN p.name, rel.roles;

• Exercise 9.10: Retrieve information about any specific relationships.
  - MATCH (p1:Person)-[rel:HELPED]-(p2:Person) RETURN p1.name, rel, p2.name;

• Exercise 9.11: Modify a property of a relationship.
 - MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie) WHERE m.title = 'Forrest Gump' AND p.name = 'Gary Sinise' SET rel.roles =['Lt. Dan Taylor'];

• Exercise 9.12: Remove a property from a relationship.
  - MATCH (p1:Person)-[rel:HELPED]->(p2:Person) WHERE p1.name = 'Tom Hanks' AND p2.name = 'Gary Sinise' REMOVE rel.research;

• Exercise 9.13: Confirm that your modifications were made to the graph.
 - MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie) WHERE m.title = 'Forrest Gump' return p, rel, m;

# Exercício 10 – Deleting nodes and relationships

Coloque os comandos utilizado em cada item a seguir:

• Exercise 10.1: Delete a relationship.
 - MATCH (:Person)-[rel:HELPED]-(:Person) DELETE rel;

• Exercise 10.2: Confirm that the relationship has been deleted.
 - MATCH (:Person)-[rel:HELPED]-(:Person) RETURN rel;

• Exercise 10.3: Retrieve a movie and all of its relationships.
  - MATCH (p:Person)-[rel]-(m:Movie) WHERE m.title = 'Forrest Gump' RETURN p, rel, m;

• Exercise 10.4: Try deleting a node without detaching its relationships.
  - MATCH (m:Movie) WHERE m.title = 'Forrest Gump' DELETE m;

• Exercise 10.5: Delete a Movie node, along with its relationships.
  - MATCH (m:Movie) WHERE m.title = 'Forrest Gump' DETACH DELETE m;

• Exercise 10.6: Confirm that the Movie node has been deleted.
  - MATCH (p:Person)-[rel]-(m:Movie) WHERE m.title = 'Forrest Gump' RETURN p, rel, m;