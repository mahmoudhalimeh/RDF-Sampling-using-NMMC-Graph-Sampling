import array

from pymantic import sparql


def drop_graphs(namespace):
    print("drop graphs " + namespace + "...")
    server_url = "http://10.109.13.93:9999/blazegraph/namespace/" + namespace + "/sparql"
    server = sparql.SPARQLServer(server_url)
    q = "drop graphs"
    server.update(q)


def execute(namespace, file_name):
    print("execute " + namespace + "...")
    server_url = "http://10.51.65.178:9999/blazegraph/namespace/" + namespace + "/sparql"
    server = sparql.SPARQLServer(server_url)
    q = "load <file:///C:/Users/mahmo/OneDrive/Desktop/yyy/" + file_name + ">"
    server.update(q)


# print("Dropping graphs...")
#
# drop_graphs("v2h0")
# drop_graphs("v2h1")
# drop_graphs("v2h2")
# drop_graphs("v2h3")
# drop_graphs("v2h4")
# drop_graphs("v2h5")
# drop_graphs("v2h6")
# drop_graphs("v2h7")
# drop_graphs("v2h8")
# drop_graphs("v2h9")
#
# drop_graphs("v2s2h0")
# drop_graphs("v2s2h1")
# drop_graphs("v2s2h2")
# drop_graphs("v2s2h3")
# drop_graphs("v2s2h4")
# drop_graphs("v2s2h5")
# drop_graphs("v2s2h6")
# drop_graphs("v2s2h7")
# drop_graphs("v2s2h8")
# drop_graphs("v2s2h9")
#
# drop_graphs("v2s5h0")
# drop_graphs("v2s5h1")
# drop_graphs("v2s5h2")
# drop_graphs("v2s5h3")
# drop_graphs("v2s5h4")
# drop_graphs("v2s5h5")
# drop_graphs("v2s5h6")
# drop_graphs("v2s5h7")
# drop_graphs("v2s5h8")
# drop_graphs("v2s5h9")
#
# drop_graphs("v2r0")
# drop_graphs("v2r1")
# drop_graphs("v2r2")
# drop_graphs("v2r3")
# drop_graphs("v2r4")
# drop_graphs("v2r5")
# drop_graphs("v2r6")
# drop_graphs("v2r7")
# drop_graphs("v2r8")
# drop_graphs("v2r9")
#
# drop_graphs("v2s2r0")
# drop_graphs("v2s2r1")
# drop_graphs("v2s2r2")
# drop_graphs("v2s2r3")
# drop_graphs("v2s2r4")
# drop_graphs("v2s2r5")
# drop_graphs("v2s2r6")
# drop_graphs("v2s2r7")
# drop_graphs("v2s2r8")
# drop_graphs("v2s2r9")
#
# drop_graphs("v2s5r0")
# drop_graphs("v2s5r1")
# drop_graphs("v2s5r2")
# drop_graphs("v2s5r3")
# drop_graphs("v2s5r4")
# drop_graphs("v2s5r5")
# drop_graphs("v2s5r6")
# drop_graphs("v2s5r7")
# drop_graphs("v2s5r8")
# drop_graphs("v2s5r9")
#
# drop_graphs("v2hr0")
# drop_graphs("v2hr1")
# drop_graphs("v2hr2")
# drop_graphs("v2hr3")
# drop_graphs("v2hr4")
# drop_graphs("v2hr5")
# drop_graphs("v2hr6")
# drop_graphs("v2hr7")
# drop_graphs("v2hr8")
# drop_graphs("v2hr9")
#
# drop_graphs("v2s2hr0")
# drop_graphs("v2s2hr1")
# drop_graphs("v2s2hr2")
# drop_graphs("v2s2hr3")
# drop_graphs("v2s2hr4")
# drop_graphs("v2s2hr5")
# drop_graphs("v2s2hr6")
# drop_graphs("v2s2hr7")
# drop_graphs("v2s2hr8")
# drop_graphs("v2s2hr9")
#
# drop_graphs("v2s5hr0")
# drop_graphs("v2s5hr1")
# drop_graphs("v2s5hr2")
# drop_graphs("v2s5hr3")
# drop_graphs("v2s5hr4")
# drop_graphs("v2s5hr5")
# drop_graphs("v2s5hr6")
# drop_graphs("v2s5hr7")
# drop_graphs("v2s5hr8")
# drop_graphs("v2s5hr9")
# print("Dropping graphs ended...")

print("Executing graphs started...")

execute("v4h1", "triples-one-history1.txt")
execute("v4h2", "triples-one-history2.txt")
execute("v4hr1", "triples-one-historyrandom1.txt")
execute("v4hr2", "triples-one-historyrandom2.txt")
execute("v4r1", "triples-one-random1.txt")
execute("v4r2", "triples-one-random2.txt")




# execute("v3s2h0", "triples-0-historyv2-s2.txt")
# execute("v3s2h1", "triples-1-historyv2-s2.txt")
# execute("v3s2h2", "triples-2-historyv2-s2.txt")
# execute("v3s5h0", "triples-0-historyv2-s5.txt")
# execute("v3s5h1", "triples-1-historyv2-s5.txt")
# execute("v3s5h2", "triples-2-historyv2-s5.txt")
# execute("v3s10h0", "triples-0-historyv2-s10.txt")
# execute("v3s10h1", "triples-1-historyv2-s10.txt")
# execute("v3s10h2", "triples-2-historyv2-s10.txt")
#
# execute("v3s2r0", "triples-0-randomv2-s2.txt")
# execute("v3s2r1", "triples-1-randomv2-s2.txt")
# execute("v3s2r2", "triples-2-randomv2-s2.txt")
# execute("v3s5r0", "triples-0-randomv2-s5.txt")
# execute("v3s5r1", "triples-1-randomv2-s5.txt")
# execute("v3s5r2", "triples-2-randomv2-s5.txt")
# execute("v3s10r0", "triples-0-randomv2-s10.txt")
# execute("v3s10r1", "triples-1-randomv2-s10.txt")
# execute("v3s10r2", "triples-2-randomv2-s10.txt")
#
# execute("v3s2hr0", "triples-0-historyrandomv2-s2.txt")
# execute("v3s2hr1", "triples-1-historyrandomv2-s2.txt")
# execute("v3s2hr2", "triples-2-historyrandomv2-s2.txt")
# execute("v3s5hr0", "triples-0-historyrandomv2-s5.txt")
# execute("v3s5hr1", "triples-1-historyrandomv2-s5.txt")
# execute("v3s5hr2", "triples-2-historyrandomv2-s5.txt")
# execute("v3s10hr0", "triples-0-historyrandomv2-s10.txt")
# execute("v3s10hr1", "triples-1-historyrandomv2-s10.txt")
# execute("v3s10hr2", "triples-2-historyrandomv2-s10.txt")












# execute("v2s2r0", "random/s2/triples", "triples-0-randomv2-s2.txt")
# execute("v2s2r1", "random/s2/triples", "triples-1-randomv2-s2.txt")
# execute("v2s2r2", "random/s2/triples", "triples-2-randomv2-s2.txt")
# execute("v2s2r3", "random/s2/triples", "triples-3-randomv2-s2.txt")
# execute("v2s2r4", "random/s2/triples", "triples-4-randomv2-s2.txt")
# execute("v2s2r5", "random/s2/triples", "triples-5-randomv2-s2.txt")
# execute("v2s2r6", "random/s2/triples", "triples-6-randomv2-s2.txt")
# execute("v2s2r7", "random/s2/triples", "triples-7-randomv2-s2.txt")
# execute("v2s2r8", "random/s2/triples", "triples-8-randomv2-s2.txt")
# execute("v2s2r9", "random/s2/triples", "triples-9-randomv2-s2.txt")
#
# execute("v2s5r0", "random/s5/triples", "triples-0-randomv2-s5.txt")
# execute("v2s5r1", "random/s5/triples", "triples-1-randomv2-s5.txt")
# execute("v2s5r2", "random/s5/triples", "triples-2-randomv2-s5.txt")
# execute("v2s5r3", "random/s5/triples", "triples-3-randomv2-s5.txt")
# execute("v2s5r4", "random/s5/triples", "triples-4-randomv2-s5.txt")
# execute("v2s5r5", "random/s5/triples", "triples-5-randomv2-s5.txt")
# execute("v2s5r6", "random/s5/triples", "triples-6-randomv2-s5.txt")
# execute("v2s5r7", "random/s5/triples", "triples-7-randomv2-s5.txt")
# execute("v2s5r8", "random/s5/triples", "triples-8-randomv2-s5.txt")
# execute("v2s5r9", "random/s5/triples", "triples-9-randomv2-s5.txt")
#
# execute("v2r0", "random/s10/triples", "triples-0-randomv2-s10.txt")
# execute("v2r1", "random/s10/triples", "triples-1-randomv2-s10.txt")
# execute("v2r2", "random/s10/triples", "triples-2-randomv2-s10.txt")
# execute("v2r3", "random/s10/triples", "triples-3-randomv2-s10.txt")
# execute("v2r4", "random/s10/triples", "triples-4-randomv2-s10.txt")
# execute("v2r5", "random/s10/triples", "triples-5-randomv2-s10.txt")
# execute("v2r6", "random/s10/triples", "triples-6-randomv2-s10.txt")
# execute("v2r7", "random/s10/triples", "triples-7-randomv2-s10.txt")
# execute("v2r8", "random/s10/triples", "triples-8-randomv2-s10.txt")
# execute("v2r9", "random/s10/triples", "triples-9-randomv2-s10.txt")
#
# execute("v2s2h0", "history/s2/triples", "triples-0-historyv2-s2.txt")
# execute("v2s2h1", "history/s2/triples", "triples-1-historyv2-s2.txt")
# execute("v2s2h2", "history/s2/triples", "triples-2-historyv2-s2.txt")
# execute("v2s2h3", "history/s2/triples", "triples-3-historyv2-s2.txt")
# execute("v2s2h4", "history/s2/triples", "triples-4-historyv2-s2.txt")
# execute("v2s2h5", "history/s2/triples", "triples-5-historyv2-s2.txt")
# execute("v2s2h6", "history/s2/triples", "triples-6-historyv2-s2.txt")
# execute("v2s2h7", "history/s2/triples", "triples-7-historyv2-s2.txt")
# execute("v2s2h8", "history/s2/triples", "triples-8-historyv2-s2.txt")
# execute("v2s2h9", "history/s2/triples", "triples-9-historyv2-s2.txt")
#
# execute("v2s5h0", "history/s5/triples", "triples-0-historyv2-s5.txt")
# execute("v2s5h1", "history/s5/triples", "triples-1-historyv2-s5.txt")
# execute("v2s5h2", "history/s5/triples", "triples-2-historyv2-s5.txt")
# execute("v2s5h3", "history/s5/triples", "triples-3-historyv2-s5.txt")
# execute("v2s5h4", "history/s5/triples", "triples-4-historyv2-s5.txt")
# execute("v2s5h5", "history/s5/triples", "triples-5-historyv2-s5.txt")
# execute("v2s5h6", "history/s5/triples", "triples-6-historyv2-s5.txt")
# execute("v2s5h7", "history/s5/triples", "triples-7-historyv2-s5.txt")
# execute("v2s5h8", "history/s5/triples", "triples-8-historyv2-s5.txt")
# execute("v2s5h9", "history/s5/triples", "triples-9-historyv2-s5.txt")
#
# execute("v2h0", "history/s10/triples", "triples-0-historyv2-s10.txt")
# execute("v2h1", "history/s10/triples", "triples-1-historyv2-s10.txt")
# execute("v2h2", "history/s10/triples", "triples-2-historyv2-s10.txt")
# execute("v2h3", "history/s10/triples", "triples-3-historyv2-s10.txt")
# execute("v2h4", "history/s10/triples", "triples-4-historyv2-s10.txt")
# execute("v2h5", "history/s10/triples", "triples-5-historyv2-s10.txt")
# execute("v2h6", "history/s10/triples", "triples-6-historyv2-s10.txt")
# execute("v2h7", "history/s10/triples", "triples-7-historyv2-s10.txt")
# execute("v2h8", "history/s10/triples", "triples-8-historyv2-s10.txt")
# execute("v2h9", "history/s10/triples", "triples-9-historyv2-s10.txt")
#
# execute("v2s2hr0", "historyrandom/s2/triples", "triples-0-historyrandomv2-s2.txt")
# execute("v2s2hr1", "historyrandom/s2/triples", "triples-1-historyrandomv2-s2.txt")
# execute("v2s2hr2", "historyrandom/s2/triples", "triples-2-historyrandomv2-s2.txt")
# execute("v2s2hr3", "historyrandom/s2/triples", "triples-3-historyrandomv2-s2.txt")
# execute("v2s2hr4", "historyrandom/s2/triples", "triples-4-historyrandomv2-s2.txt")
# execute("v2s2hr5", "historyrandom/s2/triples", "triples-5-historyrandomv2-s2.txt")
# execute("v2s2hr6", "historyrandom/s2/triples", "triples-6-historyrandomv2-s2.txt")
# execute("v2s2hr7", "historyrandom/s2/triples", "triples-7-historyrandomv2-s2.txt")
# execute("v2s2hr8", "historyrandom/s2/triples", "triples-8-historyrandomv2-s2.txt")
# execute("v2s2hr9", "historyrandom/s2/triples", "triples-9-historyrandomv2-s2.txt")
#
# execute("v2s5hr0", "historyrandom/s5/triples", "triples-0-historyrandomv2-s5.txt")
# execute("v2s5hr1", "historyrandom/s5/triples", "triples-1-historyrandomv2-s5.txt")
# execute("v2s5hr2", "historyrandom/s5/triples", "triples-2-historyrandomv2-s5.txt")
# execute("v2s5hr3", "historyrandom/s5/triples", "triples-3-historyrandomv2-s5.txt")
# execute("v2s5hr4", "historyrandom/s5/triples", "triples-4-historyrandomv2-s5.txt")
# execute("v2s5hr5", "historyrandom/s5/triples", "triples-5-historyrandomv2-s5.txt")
# execute("v2s5hr6", "historyrandom/s5/triples", "triples-6-historyrandomv2-s5.txt")
# execute("v2s5hr7", "historyrandom/s5/triples", "triples-7-historyrandomv2-s5.txt")
# execute("v2s5hr8", "historyrandom/s5/triples", "triples-8-historyrandomv2-s5.txt")
# execute("v2s5hr9", "historyrandom/s5/triples", "triples-9-historyrandomv2-s5.txt")
#
# execute("v2hr0", "historyrandom/s10/triples", "triples-0-historyrandomv2-s10.txt")
# execute("v2hr1", "historyrandom/s10/triples", "triples-1-historyrandomv2-s10.txt")
# execute("v2hr2", "historyrandom/s10/triples", "triples-2-historyrandomv2-s10.txt")
# execute("v2hr3", "historyrandom/s10/triples", "triples-3-historyrandomv2-s10.txt")
# execute("v2hr4", "historyrandom/s10/triples", "triples-4-historyrandomv2-s10.txt")
# execute("v2hr5", "historyrandom/s10/triples", "triples-5-historyrandomv2-s10.txt")
# execute("v2hr6", "historyrandom/s10/triples", "triples-6-historyrandomv2-s10.txt")
# execute("v2hr7", "historyrandom/s10/triples", "triples-7-historyrandomv2-s10.txt")
# execute("v2hr8", "historyrandom/s10/triples", "triples-8-historyrandomv2-s10.txt")
# execute("v2hr9", "historyrandom/s10/triples", "triples-9-historyrandomv2-s10.txt")

print("Executing graphs ended...")
