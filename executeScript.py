import pickle
import time
from multiprocessing import Pool

import numpy
from pymantic import sparql
import sys

numpy.set_printoptions(threshold=sys.maxsize)

def Average(lst):
    return sum(lst) / len(lst)

h_obj_iri = []
h_obj_lit = []
h_pred = []



# def get_props_average(namespace):
#     server_url = "http://localhost:9999/blazegraph/namespace/" + namespace + "/sparql"
#     server = sparql.SPARQLServer(server_url)
#     q = "Select (count(*) as ?count) where {?s ?p ?o. FILTER(isIRI(?o))}"
#     result = server.query(q)
#     for res in result['results']['bindings']:
#         h_obj_iri.append(int(res['count']['value']))
#
#     q = "Select (count(*) as ?count) where {?s ?p ?o. FILTER(isLiteral(?o))}"
#     result = server.query(q)
#     for res in result['results']['bindings']:
#         h_obj_lit.append(int(res['count']['value']))
#
#     q = "Select (count(distinct ?p) as ?count) where {?s ?p ?o.}"
#     result = server.query(q)
#     for res in result['results']['bindings']:
#         h_pred.append(int(res['count']['value']))
#
#
#
# print("history s2: ")
#
# h_obj_iri = []
# h_obj_lit = []
# h_pred = []
#
# get_props_average("v2s2h0")
# get_props_average("v2s2h1")
# get_props_average("v2s2h2")
# get_props_average("v2s2h3")
# get_props_average("v2s2h4")
# get_props_average("v2s2h5")
# get_props_average("v2s2h6")
# get_props_average("v2s2h7")
# get_props_average("v2s2h8")
# get_props_average("v2s2h9")
#
#
# avg_iri_s10 = Average(h_obj_iri)
# avg_lit_s10 = Average(h_obj_lit)
# avg_pred_s10 = Average(h_pred)
#
#
# print("Predicates: " + str(Average(h_pred)))
# print("literals: " + str(avg_lit_s10/(avg_lit_s10 + avg_iri_s10)))
# print("IRIs: " + str(avg_iri_s10/(avg_lit_s10 + avg_iri_s10)))
#
#
# print("history s5: ")
#
# h_obj_iri = []
# h_obj_lit = []
# h_pred = []
#
# get_props_average("v2s5h0")
# get_props_average("v2s5h1")
# get_props_average("v2s5h2")
# get_props_average("v2s5h3")
# get_props_average("v2s5h4")
# get_props_average("v2s5h5")
# get_props_average("v2s5h6")
# get_props_average("v2s5h7")
# get_props_average("v2s5h8")
# get_props_average("v2s5h9")
#
#
# avg_iri_s10 = Average(h_obj_iri)
# avg_lit_s10 = Average(h_obj_lit)
# avg_pred_s10 = Average(h_pred)
#
#
# print("Predicates: " + str(Average(h_pred)))
# print("literals: " + str(avg_lit_s10/(avg_lit_s10 + avg_iri_s10)))
# print("IRIs: " + str(avg_iri_s10/(avg_lit_s10 + avg_iri_s10)))
#
#
#
# print("history s10: ")
#
# h_obj_iri = []
# h_obj_lit = []
# h_pred = []
#
# get_props_average("v2h0")
# get_props_average("v2h1")
# get_props_average("v2h2")
# get_props_average("v2h3")
# get_props_average("v2h4")
# get_props_average("v2h5")
# get_props_average("v2h6")
# get_props_average("v2h7")
# get_props_average("v2h8")
# get_props_average("v2h9")
#
#
# avg_iri_s10 = Average(h_obj_iri)
# avg_lit_s10 = Average(h_obj_lit)
# avg_pred_s10 = Average(h_pred)
#
#
# print("Predicates: " + str(Average(h_pred)))
# print("literals: " + str(avg_lit_s10/(avg_lit_s10 + avg_iri_s10)))
# print("IRIs: " + str(avg_iri_s10/(avg_lit_s10 + avg_iri_s10)))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# print("random s2: ")
#
# h_obj_iri = []
# h_obj_lit = []
# h_pred = []
#
# get_props_average("v2s2r0")
# get_props_average("v2s2r1")
# get_props_average("v2s2r2")
# get_props_average("v2s2r3")
# get_props_average("v2s2r4")
# get_props_average("v2s2r5")
# get_props_average("v2s2r6")
# get_props_average("v2s2r7")
# get_props_average("v2s2r8")
# get_props_average("v2s2r9")
#
#
# avg_iri_s10 = Average(h_obj_iri)
# avg_lit_s10 = Average(h_obj_lit)
# avg_pred_s10 = Average(h_pred)
#
#
# print("Predicates: " + str(Average(h_pred)))
# print("literals: " + str(avg_lit_s10/(avg_lit_s10 + avg_iri_s10)))
# print("IRIs: " + str(avg_iri_s10/(avg_lit_s10 + avg_iri_s10)))
#
#
# print("random s5: ")
#
# h_obj_iri = []
# h_obj_lit = []
# h_pred = []
#
# get_props_average("v2s5r0")
# get_props_average("v2s5r1")
# get_props_average("v2s5r2")
# get_props_average("v2s5r3")
# get_props_average("v2s5r4")
# get_props_average("v2s5r5")
# get_props_average("v2s5r6")
# get_props_average("v2s5r7")
# get_props_average("v2s5r8")
# get_props_average("v2s5r9")
#
#
# avg_iri_s10 = Average(h_obj_iri)
# avg_lit_s10 = Average(h_obj_lit)
# avg_pred_s10 = Average(h_pred)
#
#
# print("Predicates: " + str(Average(h_pred)))
# print("literals: " + str(avg_lit_s10/(avg_lit_s10 + avg_iri_s10)))
# print("IRIs: " + str(avg_iri_s10/(avg_lit_s10 + avg_iri_s10)))
#
#
#
# print("random s10: ")
#
# h_obj_iri = []
# h_obj_lit = []
# h_pred = []
#
# get_props_average("v2r0")
# get_props_average("v2r1")
# get_props_average("v2r2")
# get_props_average("v2r3")
# get_props_average("v2r4")
# get_props_average("v2r5")
# get_props_average("v2r6")
# get_props_average("v2r7")
# get_props_average("v2r8")
# get_props_average("v2r9")
#
#
# avg_iri_s10 = Average(h_obj_iri)
# avg_lit_s10 = Average(h_obj_lit)
# avg_pred_s10 = Average(h_pred)
#
#
# print("Predicates: " + str(Average(h_pred)))
# print("literals: " + str(avg_lit_s10/(avg_lit_s10 + avg_iri_s10)))
# print("IRIs: " + str(avg_iri_s10/(avg_lit_s10 + avg_iri_s10)))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# print("history random s2: ")
#
# h_obj_iri = []
# h_obj_lit = []
# h_pred = []
#
# get_props_average("v2s2hr0")
# get_props_average("v2s2hr1")
# get_props_average("v2s2hr2")
# get_props_average("v2s2hr3")
# get_props_average("v2s2hr4")
# get_props_average("v2s2hr5")
# get_props_average("v2s2hr6")
# get_props_average("v2s2hr7")
# get_props_average("v2s2hr8")
# get_props_average("v2s2hr9")
#
#
# avg_iri_s10 = Average(h_obj_iri)
# avg_lit_s10 = Average(h_obj_lit)
# avg_pred_s10 = Average(h_pred)
#
#
# print("Predicates: " + str(Average(h_pred)))
# print("literals: " + str(avg_lit_s10/(avg_lit_s10 + avg_iri_s10)))
# print("IRIs: " + str(avg_iri_s10/(avg_lit_s10 + avg_iri_s10)))
#
#
# print("history random s5: ")
#
# h_obj_iri = []
# h_obj_lit = []
# h_pred = []
#
# get_props_average("v2s5hr0")
# get_props_average("v2s5hr1")
# get_props_average("v2s5hr2")
# get_props_average("v2s5hr3")
# get_props_average("v2s5hr4")
# get_props_average("v2s5hr5")
# get_props_average("v2s5hr6")
# get_props_average("v2s5hr7")
# get_props_average("v2s5hr8")
# get_props_average("v2s5hr9")
#
#
# avg_iri_s10 = Average(h_obj_iri)
# avg_lit_s10 = Average(h_obj_lit)
# avg_pred_s10 = Average(h_pred)
#
#
# print("Predicates: " + str(Average(h_pred)))
# print("literals: " + str(avg_lit_s10/(avg_lit_s10 + avg_iri_s10)))
# print("IRIs: " + str(avg_iri_s10/(avg_lit_s10 + avg_iri_s10)))
#
#
#
# print("history random s10: ")
#
# h_obj_iri = []
# h_obj_lit = []
# h_pred = []
#
#
# get_props_average("v2hr0")
# get_props_average("v2hr1")
# get_props_average("v2hr2")
# get_props_average("v2hr3")
# get_props_average("v2hr4")
# get_props_average("v2hr5")
# get_props_average("v2hr6")
# get_props_average("v2hr7")
# get_props_average("v2hr8")
# get_props_average("v2hr9")
#
# avg_iri_s10 = Average(h_obj_iri)
# avg_lit_s10 = Average(h_obj_lit)
# avg_pred_s10 = Average(h_pred)
#
#
# print("Predicates: " + str(Average(h_pred)))
# print("literals: " + str(avg_lit_s10/(avg_lit_s10 + avg_iri_s10)))
# print("IRIs: " + str(avg_iri_s10/(avg_lit_s10 + avg_iri_s10)))


















# print("Select distinct properties...")
# server = sparql.SPARQLServer('http://localhost:9999/blazegraph/sparql')
#
# q = "Select distinct ?p where {?s ?p ?o. }"
# result = server.query(q)
# for res in result['results']['bindings']:
#     p = "" + res['p']['value'] + ""
#     properties.append(p)


# print("Select properties stats for Original db")
# f = open("C:\\Users\\mahmo\\OneDrive\\Desktop\\files2\\props-rank.txt", "w", encoding="utf-8")
#
# for i in properties:
#     total_count = 0
#     distinct_outgoing = 0
#     distinct_incoming = 0
#     q = "Select (count(*) as ?count) where {?s <" + i + "> ?o. }"
#     result = server.query(q)
#     for res in result['results']['bindings']:
#         total_count = int(res['count']['value'])
#
#     q = "Select (count(distinct ?s) as ?count) where {?s <" + i + "> ?o. }"
#     result = server.query(q)
#     for res in result['results']['bindings']:
#         distinct_outgoing = int(res['count']['value'])
#
#     q = "Select (count(distinct ?o) as ?count) where {?s <" + i + "> ?o. }"
#     result = server.query(q)
#     for res in result['results']['bindings']:
#         distinct_incoming = int(res['count']['value'])
#
#     f.write(i + "                    " + str(total_count/distinct_outgoing) + "                    " + str(total_count/distinct_incoming) + "\n")
#
#
# f.close()
#

properties = []


properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/birthday>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/browserUsed>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/classYear>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/creationDate>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/email>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/firstName>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/gender>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/hasInterest>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/hasOrganisation>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/hasPerson>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/id>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/isLocatedIn>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/knows>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/lastName>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/locationIP>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/speaks>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/studyAt>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/workAt>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/workFrom>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/isPartOf>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/url>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/containerOf>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/content>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/hasComment>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/hasCreator>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/hasMember>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/hasModerator>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/hasPost>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/hasTag>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/imageFile>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/joinDate>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/language>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/length>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/likes>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/replyOf>")
properties.append("<http://www.ldbc.eu/ldbc_socialnet/1.0/vocabulary/title>")
properties.append("<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>")
properties.append("<http://www.w3.org/2000/01/rdf-schema#label>")
properties.append("<http://www.w3.org/2000/01/rdf-schema#subClassOf>")
properties.append("<http://xmlns.com/foaf/0.1/name>")


main_path = "C:\\Users\\mahmo\\OneDrive\\Desktop\\yyy\\"


# def get_props_average(namespace, folder, file):
#     print("Starting execution for " + namespace + "...")
#     server_url = "http://localhost:9999/blazegraph/namespace/" + namespace + "/sparql"
#     server = sparql.SPARQLServer(server_url)
#     f = open(main_path + folder + "\\" + file + ".txt", "w", encoding="utf-8")
#     for i in properties:
#         total_count = 0
#         distinct_outgoing = 0
#         distinct_incoming = 0
#         q = "Select (count(*) as ?count) where {?s " + i + " ?o. }"
#         result = server.query(q)
#         for res in result['results']['bindings']:
#             total_count = int(res['count']['value'])
#
#         q = "Select (count(distinct ?s) as ?count) where {?s " + i + " ?o. }"
#         result = server.query(q)
#         for res in result['results']['bindings']:
#             distinct_outgoing = int(res['count']['value'])
#
#         q = "Select (count(distinct ?o) as ?count) where {?s " + i + " ?o. }"
#         result = server.query(q)
#         for res in result['results']['bindings']:
#             distinct_incoming = int(res['count']['value'])
#
#         x = 0
#         y = 0
#         if distinct_outgoing > 0:
#             x = total_count / distinct_outgoing
#         if distinct_incoming > 0:
#             y = total_count / distinct_incoming
#
#         f.write(str(x) + "                    " + str(y) + "\n")
#
#     f.close()


def aaa(namespace, folder, file):
    print("Starting execution for " + namespace + "...")
    server_url = "http://127.0.0.1:9999/blazegraph/namespace/" + namespace + "/sparql"
    server = sparql.SPARQLServer(server_url)
    f = open(main_path + folder + "\\" + file + ".txt", "w", encoding="utf-8")

    for i in properties:
        total_count = 0
        distinct_outgoing = 0
        distinct_incoming = 0
        q = "Select (count(*) as ?count) where {?s " + i + " ?o. }"
        result = server.query(q)
        for res in result['results']['bindings']:
            total_count = int(res['count']['value'])

        q = "Select (count(distinct ?s) as ?count) where {?s " + i + " ?o. }"
        result = server.query(q)
        for res in result['results']['bindings']:
            distinct_outgoing = int(res['count']['value'])

        q = "Select (count(distinct ?o) as ?count) where {?s " + i + " ?o. }"
        result = server.query(q)
        for res in result['results']['bindings']:
            distinct_incoming = int(res['count']['value'])

        f.write(str(total_count / distinct_outgoing) + "                               " + str(total_count / distinct_incoming) + "\n")

    f.close()



aaa("v4h1", "props", "h1")
aaa("v4hr1", "props", "hr1")
aaa("v4r1", "props", "r1")

aaa("v4h2", "props", "h2")
aaa("v4hr2", "props", "hr2")
aaa("v4r2", "props", "v4r2")





# aaa("v3s2hr0", "props", "0-hr-s2")
# aaa("v3s2hr1", "props", "1-hr-s2")
# aaa("v3s2hr2", "props", "2-hr-s2")
# aaa("v3s5hr0", "props", "0-hr-s5")
# aaa("v3s5hr1", "props", "1-hr-s5")
# aaa("v3s5hr2", "props", "2-hr-s5")
# aaa("v3s10hr0", "props", "0-hr-s10")
# aaa("v3s10hr1", "props", "1-hr-s10")
# aaa("v3s10hr2", "props", "2-hr-s10")
# aaa("v3s2r0", "props", "0-r-s2")
# aaa("v3s2r1", "props", "1-r-s2")
# aaa("v3s2r2", "props", "2-r-s2")
# aaa("v3s5r0", "props", "0-r-s5")
# aaa("v3s5r1", "props", "1-r-s5")
# aaa("v3s5r2", "props", "2-r-s5")
# aaa("v3s10r0", "props", "0-r-s10")
# aaa("v3s10r1", "props", "1-r-s10")
# aaa("v3s10r2", "props", "2-r-s10")
# aaa("v3s2h0", "props", "0-h-s2")
# aaa("v3s2h1", "props", "1-h-s2")
# aaa("v3s2h2", "props", "2-h-s2")
# aaa("v3s5h0", "props", "0-h-s5")
# aaa("v3s5h1", "props", "1-h-s5")
# aaa("v3s5h2", "props", "2-h-s5")
# aaa("v3s10h0", "props", "0-h-s10")
# aaa("v3s10h1", "props", "1-h-s10")
# aaa("v3s10h2", "props", "2-h-s10")






# get_props_average("0h2", "historyrandom-s10-samples", "triples-0-historyrandom-s10")
# get_props_average("1h2", "historyrandom-s10-samples", "triples-1-historyrandom-s10")
# get_props_average("2h2", "historyrandom-s10-samples", "triples-2-historyrandom-s10")
# get_props_average("3h2", "historyrandom-s10-samples", "triples-3-historyrandom-s10")
# get_props_average("4h2", "historyrandom-s10-samples", "triples-4-historyrandom-s10")
# get_props_average("5h2", "historyrandom-s10-samples", "triples-5-historyrandom-s10")
# get_props_average("6h2", "historyrandom-s10-samples", "triples-6-historyrandom-s10")
# get_props_average("7h2", "historyrandom-s10-samples", "triples-7-historyrandom-s10")
# get_props_average("8h2", "historyrandom-s10-samples", "triples-8-historyrandom-s10")
# get_props_average("9h2", "historyrandom-s10-samples", "triples-9-historyrandom-s10")


# get_props_average("v2s2r0", "random/s2/props", "props-0-randomv2-s2.txt")
# get_props_average("v2s2r1", "random/s2/props", "props-1-randomv2-s2.txt")
# get_props_average("v2s2r2", "random/s2/props", "props-2-randomv2-s2.txt")
# get_props_average("v2s2r3", "random/s2/props", "props-3-randomv2-s2.txt")
# get_props_average("v2s2r4", "random/s2/props", "props-4-randomv2-s2.txt")
# get_props_average("v2s2r5", "random/s2/props", "props-5-randomv2-s2.txt")
# get_props_average("v2s2r6", "random/s2/props", "props-6-randomv2-s2.txt")
# get_props_average("v2s2r7", "random/s2/props", "props-7-randomv2-s2.txt")
# get_props_average("v2s2r8", "random/s2/props", "props-8-randomv2-s2.txt")
# get_props_average("v2s2r9", "random/s2/props", "props-9-randomv2-s2.txt")
#
# get_props_average("v2s5r0", "random/s5/props", "props0-randomv2-s5.txt")
# get_props_average("v2s5r1", "random/s5/props", "props1-randomv2-s5.txt")
# get_props_average("v2s5r2", "random/s5/props", "props2-randomv2-s5.txt")
# get_props_average("v2s5r3", "random/s5/props", "props3-randomv2-s5.txt")
# get_props_average("v2s5r4", "random/s5/props", "props4-randomv2-s5.txt")
# get_props_average("v2s5r5", "random/s5/props", "props5-randomv2-s5.txt")
# get_props_average("v2s5r6", "random/s5/props", "props6-randomv2-s5.txt")
# get_props_average("v2s5r7", "random/s5/props", "props7-randomv2-s5.txt")
# get_props_average("v2s5r8", "random/s5/props", "props8-randomv2-s5.txt")
# get_props_average("v2s5r9", "random/s5/props", "props9-randomv2-s5.txt")
#
# get_props_average("v2s2h0", "history/s2/props", "props-0-historyv2-s2.txt")
# get_props_average("v2s2h1", "history/s2/props", "props-1-historyv2-s2.txt")
# get_props_average("v2s2h2", "history/s2/props", "props-2-historyv2-s2.txt")
# get_props_average("v2s2h3", "history/s2/props", "props-3-historyv2-s2.txt")
# get_props_average("v2s2h4", "history/s2/props", "props-4-historyv2-s2.txt")
# get_props_average("v2s2h5", "history/s2/props", "props-5-historyv2-s2.txt")
# get_props_average("v2s2h6", "history/s2/props", "props-6-historyv2-s2.txt")
# get_props_average("v2s2h7", "history/s2/props", "props-7-historyv2-s2.txt")
# get_props_average("v2s2h8", "history/s2/props", "props-8-historyv2-s2.txt")
# get_props_average("v2s2h9", "history/s2/props", "props-9-historyv2-s2.txt")
#
# get_props_average("v2s5h0", "history/s5/props", "props-0-historyv2-s5.txt")
# get_props_average("v2s5h1", "history/s5/props", "props-1-historyv2-s5.txt")
# get_props_average("v2s5h2", "history/s5/props", "props-2-historyv2-s5.txt")
# get_props_average("v2s5h3", "history/s5/props", "props-3-historyv2-s5.txt")
# get_props_average("v2s5h4", "history/s5/props", "props-4-historyv2-s5.txt")
# get_props_average("v2s5h5", "history/s5/props", "props-5-historyv2-s5.txt")
# get_props_average("v2s5h6", "history/s5/props", "props-6-historyv2-s5.txt")
# get_props_average("v2s5h7", "history/s5/props", "props-7-historyv2-s5.txt")
# get_props_average("v2s5h8", "history/s5/props", "props-8-historyv2-s5.txt")
# get_props_average("v2s5h9", "history/s5/props", "props-9-historyv2-s5.txt")
#
# get_props_average("v2s2hr0", "historyrandom/s2/props", "props-0-historyrandomv2-s2.txt")
# get_props_average("v2s2hr1", "historyrandom/s2/props", "props-1-historyrandomv2-s2.txt")
# get_props_average("v2s2hr2", "historyrandom/s2/props", "props-2-historyrandomv2-s2.txt")
# get_props_average("v2s2hr3", "historyrandom/s2/props", "props-3-historyrandomv2-s2.txt")
# get_props_average("v2s2hr4", "historyrandom/s2/props", "props-4-historyrandomv2-s2.txt")
# get_props_average("v2s2hr5", "historyrandom/s2/props", "props-5-historyrandomv2-s2.txt")
# get_props_average("v2s2hr6", "historyrandom/s2/props", "props-6-historyrandomv2-s2.txt")
# get_props_average("v2s2hr7", "historyrandom/s2/props", "props-7-historyrandomv2-s2.txt")
# get_props_average("v2s2hr8", "historyrandom/s2/props", "props-8-historyrandomv2-s2.txt")
# get_props_average("v2s2hr9", "historyrandom/s2/props", "props-9-historyrandomv2-s2.txt")
#
# get_props_average("v2s5hr0", "historyrandom/s5/props", "props-0-historyrandomv2-s5.txt")
# get_props_average("v2s5hr1", "historyrandom/s5/props", "props-1-historyrandomv2-s5.txt")
# get_props_average("v2s5hr2", "historyrandom/s5/props", "props-2-historyrandomv2-s5.txt")
# get_props_average("v2s5hr3", "historyrandom/s5/props", "props-3-historyrandomv2-s5.txt")
# get_props_average("v2s5hr4", "historyrandom/s5/props", "props-4-historyrandomv2-s5.txt")
# get_props_average("v2s5hr5", "historyrandom/s5/props", "props-5-historyrandomv2-s5.txt")
# get_props_average("v2s5hr6", "historyrandom/s5/props", "props-6-historyrandomv2-s5.txt")
# get_props_average("v2s5hr7", "historyrandom/s5/props", "props-7-historyrandomv2-s5.txt")
# get_props_average("v2s5hr8", "historyrandom/s5/props", "props-8-historyrandomv2-s5.txt")
# get_props_average("v2s5hr9", "historyrandom/s5/props", "props-9-historyrandomv2-s5.txt")





