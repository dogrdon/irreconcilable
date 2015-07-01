Basic Questions About Working with RDF 
======================================

###reconciling subject terms
Problem - subject terms can fall under any number of categories, how do you search through RDF linked data to find the concept they are referring to? Making a folksonomy a taxonomy by elevating community selected tags and connecting them with authority terms.

Question - is this the wrong way to go about this?

- Ok, I have to query it with SPARQL, it's a 500mb xml file, how do I now what properties there are to query?
- Basically I'll be doing this with keywords, so what do I query to get records that match those keywords
- defining the boundary for what you will want to search - if you had a list of peoples
- reconcilliation tools on open refine seem to be the best tool for now, can review the output to the log to see what SPARQL queries it generates
- any tools for python that allow you to create sparql queries and hit existing endpoints - might give more flexibility and control over the output
- what happened to this: http://lookup.dbpedia.org/api/search/KeywordSearch?QueryString=<searchstring>

###the problem of RDF/XML portability
- use docker to spin up a sparql endpoint?
- linked data fragments 
- maybe I am still not totally sure what I am trying to get out of this.

###the problem of gaining concensus around what each term means
- this needs to be manual at some point
- high purchase on local knowledge (examples?)

###What is Open Refine doing (rdf reconciliation)?
- pull out some queries from the log
- <bif:contains>
- why do it with something else?
- use questioning authority?

###Problems and TODOs with current approach:
- odd characters are catching in mongo
- if encoded one way, and checked another, you get duplicate entries
- would want to maybe create an option for "check again on another term"
-

OPEN REFINE RESULTS - Raw
- 55 matched
- 661 not matched
- of the 661, really not good options for matching manually

OPEN REFINE RESULTS - Preprocessed
- 54 matched
- 662 not matched
- ditto

OPEN REFINE RESULTS - dbpedia (not using Zemanta, which appears to have closed it's api)
- 79 matched
- 637 not matched



LOGS
====

##Verbose Logs - LCSH
`GET http://sparql.freeyourmetadata.org/?query=SELECT+DISTINCT+%3Fentity+%3Flabel+%3Fscore1+WHERE%7B%3Fentity+%3Fp+%3Flabel.+%3Flabel+%3Cbif%3Acontains%3E+%22%27%2BSquatting+%2B%2F+%2BEuro+%2Bsocial+%2Bcentres%27%22+OPTION%28score+%3Fscore1%29.+FILTER+%28%3Fp%3D%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23prefLabel%3E%29.+%3Fentity+a+%3Ftype.+FILTER+%28%3Ftype+IN+%28%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23Concept%3E%29%29.+FILTER+isIRI%28%3Fentity%29.+%7D+ORDER+BY+desc%28%3Fscore1%29+LIMIT+6&default-graph-uri=http%3A%2F%2Fsparql.freeyourmetadata.org%2Fauthorities-processed%2F (0ms)
13:43:08.538 [        QueryEndpointImpl] reconciling Squatting / Euro social centres took 130 milliseconds (130ms)
13:43:08.839 [..l.engine.http.HttpQuery] URL: http://sparql.freeyourmetadata.org/ (301ms)
13:43:08.840 [..hp.hpl.jena.arq.service] query=SELECT+DISTINCT+%3Fentity+%3Flabel+%3Fscore1+WHERE%7B%3Fentity+%3Fp+%3Flabel.+%3Flabel+%3Cbif%3Acontains%3E+%22%27%2BClass+%2BStruggle%27%22+OPTION%28score+%3Fscore1%29.+FILTER+%28%3Fp%3D%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23prefLabel%3E%29.+%3Fentity+a+%3Ftype.+FILTER+%28%3Ftype+IN+%28%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23Concept%3E%29%29.+FILTER+isIRI%28%3Fentity%29.+%7D+ORDER+BY+desc%28%3Fscore1%29+LIMIT+6&default-graph-uri=http%3A%2F%2Fsparql.freeyourmetadata.org%2Fauthorities-processed%2F (1ms)`

##Verbose Logs - dbpedia
SPARQL query:
SELECT DISTINCT ?entity ?label ?score1 WHERE{?entity ?p ?label. ?label <bif:contains> "'+Montreal +Anarchist +Bookfair'" OPTION(score ?score1). FILTER (?p=<http://www.w3.org/2004/02/skos/core#prefLabel>). ?entity a ?type. FILTER (?type IN (<http://www.w3.org/2004/02/skos/core#Concept>)). FILTER isIRI(?entity). } ORDER BY desc(?score1) LIMIT 6

SPARQL query:
SELECT DISTINCT ?entity ?label ?score1 WHERE{?entity ?p ?label. ?label <bif:contains> "'+Image +Shift'" OPTION(score ?score1). FILTER (?p=<http://www.w3.org/2004/02/skos/core#prefLabel>). ?entity a ?type. FILTER (?type IN (<http://www.w3.org/2004/02/skos/core#Concept>)). FILTER isIRI(?entity). } ORDER BY desc(?score1) LIMIT 6

`15:26:31.734 [        QueryEndpointImpl] reconciling Bound Togetther Collection - Labor took 116 milliseconds (116ms)
15:26:32.035 [..l.engine.http.HttpQuery] URL: http://dbpedia.org/sparql (301ms)
15:26:32.035 [..hp.hpl.jena.arq.service] query=SELECT+DISTINCT+%3Fentity+%3Flabel+%3Fscore1+WHERE%7B%3Fentity+%3Fp+%3Flabel.+%3Flabel+%3Cbif%3Acontains%3E+%22%27%2BGreen+%2BScare%27%22+OPTION%28score+%3Fscore1%29.+FILTER+%28%3Fp%3D%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23prefLabel%3E%29.+%3Fentity+a+%3Ftype.+FILTER+%28%3Ftype+IN+%28%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23Concept%3E%29%29.+FILTER+isIRI%28%3Fentity%29.+%7D+ORDER+BY+desc%28%3Fscore1%29+LIMIT+6&default-graph-uri=http%3A%2F%2Fdbpedia.org (0ms)
15:26:32.035 [..l.engine.http.HttpQuery] GET http://dbpedia.org/sparql?query=SELECT+DISTINCT+%3Fentity+%3Flabel+%3Fscore1+WHERE%7B%3Fentity+%3Fp+%3Flabel.+%3Flabel+%3Cbif%3Acontains%3E+%22%27%2BGreen+%2BScare%27%22+OPTION%28score+%3Fscore1%29.+FILTER+%28%3Fp%3D%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23prefLabel%3E%29.+%3Fentity+a+%3Ftype.+FILTER+%28%3Ftype+IN+%28%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23Concept%3E%29%29.+FILTER+isIRI%28%3Fentity%29.+%7D+ORDER+BY+desc%28%3Fscore1%29+LIMIT+6&default-graph-uri=http%3A%2F%2Fdbpedia.org (0ms)
15:26:38.767 [        QueryEndpointImpl] reconciling Green Scare took 6733 milliseconds (6732ms)
15:26:39.068 [..l.engine.http.HttpQuery] URL: http://dbpedia.org/sparql (301ms)
15:26:39.068 [..hp.hpl.jena.arq.service] query=SELECT+DISTINCT+%3Fentity+%3Flabel+%3Fscore1+WHERE%7B%3Fentity+%3Fp+%3Flabel.+%3Flabel+%3Cbif%3Acontains%3E+%22%27%2BRicardo+%2BJimenez%27%22+OPTION%28score+%3Fscore1%29.+FILTER+%28%3Fp%3D%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23prefLabel%3E%29.+%3Fentity+a+%3Ftype.+FILTER+%28%3Ftype+IN+%28%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23Concept%3E%29%29.+FILTER+isIRI%28%3Fentity%29.+%7D+ORDER+BY+desc%28%3Fscore1%29+LIMIT+6&default-graph-uri=http%3A%2F%2Fdbpedia.org (0ms)
15:26:39.068 [..l.engine.http.HttpQuery] GET http://dbpedia.org/sparql?query=SELECT+DISTINCT+%3Fentity+%3Flabel+%3Fscore1+WHERE%7B%3Fentity+%3Fp+%3Flabel.+%3Flabel+%3Cbif%3Acontains%3E+%22%27%2BRicardo+%2BJimenez%27%22+OPTION%28score+%3Fscore1%29.+FILTER+%28%3Fp%3D%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23prefLabel%3E%29.+%3Fentity+a+%3Ftype.+FILTER+%28%3Ftype+IN+%28%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23Concept%3E%29%29.+FILTER+isIRI%28%3Fentity%29.+%7D+ORDER+BY+desc%28%3Fscore1%29+LIMIT+6&default-graph-uri=http%3A%2F%2Fdbpedia.org (0ms)`

##Info output for results
`13:13:15.552 [            rdf_extension] {"q6":{"result":[{"id":"http://id.loc.gov/authorities/sh2002002618#concept","name":"Folk songs, Cham?","score":0.5882352590560913,"match":false,"type":[]},{"id":"http://id.loc.gov/authorities/sh85050066#concept","name":"Folk songs, Russian","score":0.5263158082962036,"match":false,"type":[]},{"id":"http://id.loc.gov/authorities/sh85049956#concept","name":"Folk songs, Catalan","score":0.5263158082962036,"match":false,"type":[]}]},"q5":{"result":[]},"q8":{"result":[]},"q7":{"result":[{"id":"http://id.loc.gov/authorities/sh85083615#concept","name":"Mental health","score":1.0,"match":true,"type":[]},{"id":"http://id.loc.gov/authorities/sh85083635#concept","name":"Mental health policy","score":0.6499999761581421,"match":true,"type":[]},{"id":"http://id.loc.gov/authorities/sh85083637#concept","name":"Mental health services--Citizen participation","score":0.2888888716697693,"match":true,"type":[]}]},"q2":{"result":[]},"q1":{"result":[{"id":"http://id.loc.gov/authorities/sh85123098#concept","name":"Skateboarding","score":1.0,"match":true,"type":[]},{"id":"http://id.loc.gov/authorities/sh85123099#concept","name":"Skateboarding parks","score":0.6842105388641357,"match":false,"type":[]},{"id":"http://id.loc.gov/authorities/sh98004978#concept","name":"Skateboarding--Equipment and supplies","score":0.35135138034820557,"match":true,"type":[]}]},"q4":{"result":[{"id":"http://id.loc.gov/authorities/sh2008005212#concept","name":"Reproductive rights","score":1.0,"match":true,"type":[]},{"id":"http://id.loc.gov/authorities/sh2009005902#concept","name":"Reproductive rights (Islamic law)","score":0.5757575631141663,"match":true,"type":[]}]},"q3":{"result":[]},"q0":{"result":[]},"q9":{"result":[]}} (4382ms)
13:13:15.630 [            rdf_extension] receiving request for services/lcsh (78ms)
13:13:15.632 [            rdf_extension] command is multi-reconcile (2ms)
13:13:15.632 [            rdf_extension] command is multi-reconcile, while service name is lcsh (0ms)
13:13:20.119 [            rdf_extension] {"q6":{"result":[{"id":"http://id.loc.gov/authorities/sh85051675#concept","name":"Free schools","score":1.0,"match":true,"type":[]},{"id":"http://id.loc.gov/authorities/sh91000701#concept","name":"National Drug-Free Schools and Communities Education and Awareness Day","score":0.14693876675197057,"match":true,"type":[]}]},"q5":{"result":[]},"q8":{"result":[]},"q7":{"result":[]},"q2":{"result":[]},"q1":{"result":[]},"q4":{"result":[]},"q3":{"result":[]},"q0":{"result":[{"id":"http://id.loc.gov/authorities/sh85069833#concept","name":"Jazz","score":1.0,"match":true,"type":[]},{"id":"http://id.loc.gov/authorities/sh2002002665#concept","name":"Jazz--Asian influences","score":0.1818181872367859,"match":true,"type":[]},{"id":"http://id.loc.gov/authorities/sh2002002664#concept","name":"Jazz--African influences","score":0.1666666865348816,"match":true,"type":[]}]},"q9":{"result":[]}} (4487ms)
13:13:20.191 [            rdf_extension] receiving request for services/lcsh (72ms)
13:13:20.191 [            rdf_extension] command is multi-reconcile (0ms)
13:13:20.191 [            rdf_extension] command is multi-reconcile, while service name is lcsh (0ms)
13:13:25.985 [            rdf_extension] {"q6":{"result":[]},"q5":{"result":[]},"q8":{"result":[{"id":"http://id.loc.gov/authorities/sh85093048#concept","name":"Nuclear power plants--Piping","score":0.4642857313156128,"match":false,"type":[]},{"id":"http://id.loc.gov/authorities/sh85093054#concept","name":"Nuclear power plants--Ireland","score":0.4482758641242981,"match":false,"type":[]},{"id":"http://id.loc.gov/authorities/sh85093060#concept","name":"Nuclear power plants--Tennessee","score":0.4193548560142517,"match":false,"type":[]}]},"q7":{"result":[]},"q2":{"result":[]},"q1":{"result":[]},"q4":{"result":[]},"q3":{"result":[]},"q0":{"result":[]},"q9":{"result":[{"id":"http://id.loc.gov/authorities/sh2005007932#concept","name":"Nostoc commune","score":0.5,"match":false,"type":[]},{"id":"http://id.loc.gov/authorities/sh2010010086#concept","name":"Fusarium commune","score":0.4375,"match":false,"type":[]},{"id":"http://id.loc.gov/authorities/sh85098061#concept","name":"Paris (France)--History--Commune, 1871","score":0.15789474759783062,"match":false,"type":[]}]}} (5794ms)`
