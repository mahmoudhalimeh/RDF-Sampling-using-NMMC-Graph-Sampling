import array

from pymantic import sparql

"""
This method drops all the graphs from the database or namespace.
"""


def drop_graphs(namespace):
    print("drop graphs " + namespace + "...")
    server_url = "http://10.109.13.93:9999/blazegraph/namespace/" + namespace + "/sparql"
    server = sparql.SPARQLServer(server_url)
    q = "drop graphs"
    server.update(q)


"""
This method executes an insert query to add rdf triples to the database.
It adds the triples from the file_name to the namespace.
"""


def execute(namespace, file_name):
    print("execute " + namespace + "...")
    server_url = "http://10.51.65.178:9999/blazegraph/namespace/" + namespace + "/sparql"
    server = sparql.SPARQLServer(server_url)
    q = "load <file:///C:/Users/mahmo/OneDrive/Desktop/yyy/" + file_name + ">"
    server.update(q)

# print("Dropping graphs...")
# drop_graphs("v2h0")
# drop_graphs("v2h1")
# print("Dropping graphs ended...")


# print("Executing graphs started...")
# execute("v4h1", "triples-history.txt")
# execute("v4h2", "triples-history.txt")
# print("Executing graphs ended...")
