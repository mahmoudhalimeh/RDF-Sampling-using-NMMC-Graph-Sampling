import pickle
import time
from multiprocessing import Pool

import numpy
from pymantic import sparql
import sys

numpy.set_printoptions(threshold=sys.maxsize)

# file = open("C:\\Users\\mahmo\\OneDrive\\Desktop\\Results-v2\\History\\history-s10.obj", 'rb')




def Execute(s):
    server = sparql.SPARQLServer('http://localhost:9999/blazegraph/sparql')

    q = "Select * where {<" + s + "> ?p ?o. }"
    result = server.query(q)
    for res in result['results']['bindings']:
        # s = "<" + s + ">   "
        p = "" + res['p']['value'] + ""
        o = ""
        if res['o']['type'] == "uri":
            o = "<" + res['o']['value'] + ">"
        else:
            o = "\"" + res['o']['value'] + "\""
        f.write("<" + s + ">   <" + p + ">   " + o + ".\n")


if __name__ == '__main__':

    f = ""

    def xyz(path, f_name):
        file = open(path + f_name + ".obj", 'rb')
        obj = pickle.load(file)
        file.close()

        global f
        f = open(path + "triples-" + f_name + ".txt", "w", encoding="utf-8")

        ti = time.perf_counter()

        pool = Pool(70)
        pool.map(Execute, obj.results)
        te = time.perf_counter()
        f.close()

        print(f"Created triples file in {te - ti:0.4f} seconds")

    main_path = "/home/user/results/"

    # xyz(main_path, "one-historyrandom-s2")
    # xyz(main_path, "one-history-s2")
    # xyz(main_path, "one-random-s10")

    xyz(main_path, "one-random1")
    xyz(main_path, "one-random2")

    xyz(main_path, "one-historyrandom1")
    xyz(main_path, "one-historyrandom2")

    xyz(main_path, "one-history1")
    xyz(main_path, "one-history2")

    # xyz(main_path, "0-randomv2-s2")
    # xyz(main_path, "1-randomv2-s2")
    # xyz(main_path, "2-randomv2-s2")
    # xyz(main_path, "3-randomv2-s2")
    # xyz(main_path, "4-randomv2-s2")
    # xyz(main_path, "5-randomv2-s2")
    # xyz(main_path, "6-randomv2-s2")
    # xyz(main_path, "7-randomv2-s2")
    # xyz(main_path, "8-randomv2-s2")
    # xyz(main_path, "9-randomv2-s2")

    # xyz(main_path, "0-randomv2-s5")
    # xyz(main_path, "1-randomv2-s5")
    # xyz(main_path, "2-randomv2-s5")
    # xyz(main_path, "3-randomv2-s5")
    # xyz(main_path, "4-randomv2-s5")
    # xyz(main_path, "5-randomv2-s5")
    # xyz(main_path, "6-randomv2-s5")
    # xyz(main_path, "7-randomv2-s5")
    # xyz(main_path, "8-randomv2-s5")
    # xyz(main_path, "9-randomv2-s5")

    # xyz(main_path, "0-randomv2-s10")
    # xyz(main_path, "1-randomv2-s10")
    # xyz(main_path, "2-randomv2-s10")
    # xyz(main_path, "3-randomv2-s10")
    # xyz(main_path, "4-randomv2-s10")
    # xyz(main_path, "5-randomv2-s10")
    # xyz(main_path, "6-randomv2-s10")
    # xyz(main_path, "7-randomv2-s10")
    # xyz(main_path, "8-randomv2-s10")
    # xyz(main_path, "9-randomv2-s10")

    # xyz(main_path, "0-historyv2-s2")
    # xyz(main_path, "1-historyv2-s2")
    # xyz(main_path, "2-historyv2-s2")
    # xyz(main_path, "3-historyv2-s2")
    # xyz(main_path, "4-historyv2-s2")
    # xyz(main_path, "5-historyv2-s2")
    # xyz(main_path, "6-historyv2-s2")
    # xyz(main_path, "7-historyv2-s2")
    # xyz(main_path, "8-historyv2-s2")
    # xyz(main_path, "9-historyv2-s2")

    # xyz(main_path, "0-historyv2-s5")
    # xyz(main_path, "1-historyv2-s5")
    # xyz(main_path, "2-historyv2-s5")
    # xyz(main_path, "3-historyv2-s5")
    # xyz(main_path, "4-historyv2-s5")
    # xyz(main_path, "5-historyv2-s5")
    # xyz(main_path, "6-historyv2-s5")
    # xyz(main_path, "7-historyv2-s5")
    # xyz(main_path, "8-historyv2-s5")
    # xyz(main_path, "9-historyv2-s5")

    # xyz(main_path, "0-historyv2-s10")
    # xyz(main_path, "1-historyv2-s10")
    # xyz(main_path, "2-historyv2-s10")
    # xyz(main_path, "3-historyv2-s10")
    # xyz(main_path, "4-historyv2-s10")
    # xyz(main_path, "5-historyv2-s10")
    # xyz(main_path, "6-historyv2-s10")
    # xyz(main_path, "7-historyv2-s10")
    # xyz(main_path, "8-historyv2-s10")
    # xyz(main_path, "9-historyv2-s10")

    # xyz(main_path, "0-historyrandomv2-s2")
    # xyz(main_path, "1-historyrandomv2-s2")
    # xyz(main_path, "2-historyrandomv2-s2")
    # xyz(main_path, "3-historyrandomv2-s2")
    # xyz(main_path, "4-historyrandomv2-s2")
    # xyz(main_path, "5-historyrandomv2-s2")
    # xyz(main_path, "6-historyrandomv2-s2")
    # xyz(main_path, "7-historyrandomv2-s2")
    # xyz(main_path, "8-historyrandomv2-s2")
    # xyz(main_path, "9-historyrandomv2-s2")

    # xyz(main_path, "0-historyrandomv2-s5")
    # xyz(main_path, "1-historyrandomv2-s5")
    # xyz(main_path, "2-historyrandomv2-s5")
    # xyz(main_path, "3-historyrandomv2-s5")
    # xyz(main_path, "4-historyrandomv2-s5")
    # xyz(main_path, "5-historyrandomv2-s5")
    # xyz(main_path, "6-historyrandomv2-s5")
    # xyz(main_path, "7-historyrandomv2-s5")
    # xyz(main_path, "8-historyrandomv2-s5")
    # xyz(main_path, "9-historyrandomv2-s5")

    # xyz(main_path, "0-historyrandomv2-s10")
    # xyz(main_path, "1-historyrandomv2-s10")
    # xyz(main_path, "2-historyrandomv2-s10")
    # xyz(main_path, "3-historyrandomv2-s10")
    # xyz(main_path, "4-historyrandomv2-s10")
    # xyz(main_path, "5-historyrandomv2-s10")
    # xyz(main_path, "6-historyrandomv2-s10")
    # xyz(main_path, "7-historyrandomv2-s10")
    # xyz(main_path, "8-historyrandomv2-s10")
    # xyz(main_path, "9-historyrandomv2-s10")

    # xyz(main_path, "history-s2-samples", "0-history-s2")
    # xyz(main_path, "history-s2-samples", "1-history-s2")
    # xyz(main_path, "history-s2-samples", "2-history-s2")
    # xyz(main_path, "history-s2-samples", "3-history-s2")
    # xyz(main_path, "history-s2-samples", "4-history-s2")
    # xyz(main_path, "history-s2-samples", "5-history-s2")
    # xyz(main_path, "history-s2-samples", "6-history-s2")
    # xyz(main_path, "history-s2-samples", "7-history-s2")
    # xyz(main_path, "history-s2-samples", "8-history-s2")
    # xyz(main_path, "history-s2-samples", "9-history-s2")
    #
    # xyz(main_path, "history-s5-samples", "0-history-s5")
    # xyz(main_path, "history-s5-samples", "1-history-s5")
    # xyz(main_path, "history-s5-samples", "2-history-s5")
    # xyz(main_path, "history-s5-samples", "3-history-s5")
    # xyz(main_path, "history-s5-samples", "4-history-s5")
    # xyz(main_path, "history-s5-samples", "5-history-s5")
    # xyz(main_path, "history-s5-samples", "6-history-s5")
    # xyz(main_path, "history-s5-samples", "7-history-s5")
    # xyz(main_path, "history-s5-samples", "8-history-s5")
    # xyz(main_path, "history-s5-samples", "9-history-s5")
    #
    # xyz(main_path, "history-s10-samples", "0-history-s10")
    # xyz(main_path, "history-s10-samples", "1-history-s10")
    # xyz(main_path, "history-s10-samples", "2-history-s10")
    # xyz(main_path, "history-s10-samples", "3-history-s10")
    # xyz(main_path, "history-s10-samples", "4-history-s10")
    # xyz(main_path, "history-s10-samples", "5-history-s10")
    # xyz(main_path, "history-s10-samples", "6-history-s10")
    # xyz(main_path, "history-s10-samples", "7-history-s10")
    # xyz(main_path, "history-s10-samples", "8-history-s10")
    # xyz(main_path, "history-s10-samples", "9-history-s10")
    #
    # xyz(main_path, "random-s2-samples", "0-random-s2")
    # xyz(main_path, "random-s2-samples", "1-random-s2")
    # xyz(main_path, "random-s2-samples", "2-random-s2")
    # xyz(main_path, "random-s2-samples", "3-random-s2")
    # xyz(main_path, "random-s2-samples", "4-random-s2")
    # xyz(main_path, "random-s2-samples", "5-random-s2")
    # xyz(main_path, "random-s2-samples", "6-random-s2")
    # xyz(main_path, "random-s2-samples", "7-random-s2")
    # xyz(main_path, "random-s2-samples", "8-random-s2")
    # xyz(main_path, "random-s2-samples", "9-random-s2")
    #
    # xyz(main_path, "random-s5-samples", "0-random-s5")
    # xyz(main_path, "random-s5-samples", "1-random-s5")
    # xyz(main_path, "random-s5-samples", "2-random-s5")
    # xyz(main_path, "random-s5-samples", "3-random-s5")
    # xyz(main_path, "random-s5-samples", "4-random-s5")
    # xyz(main_path, "random-s5-samples", "5-random-s5")
    # xyz(main_path, "random-s5-samples", "6-random-s5")
    # xyz(main_path, "random-s5-samples", "7-random-s5")
    # xyz(main_path, "random-s5-samples", "8-random-s5")
    # xyz(main_path, "random-s5-samples", "9-random-s5")

    # xyz(main_path, "random-s10-samples", "0-random-s10")
    # xyz(main_path, "random-s10-samples", "1-random-s10")
    # xyz(main_path, "random-s10-samples", "2-random-s10")
    # xyz(main_path, "random-s10-samples", "3-random-s10")
    # xyz(main_path, "random-s10-samples", "4-random-s10")
    # xyz(main_path, "random-s10-samples", "5-random-s10")
    # xyz(main_path, "random-s10-samples", "6-random-s10")
    # xyz(main_path, "random-s10-samples", "7-random-s10")
    # xyz(main_path, "random-s10-samples", "8-random-s10")
    # xyz(main_path, "random-s10-samples", "9-random-s10")
    #
    # xyz(main_path, "historyrandom-s2-samples", "0-historyrandom-s2")
    # xyz(main_path, "historyrandom-s2-samples", "1-historyrandom-s2")
    # xyz(main_path, "historyrandom-s2-samples", "2-historyrandom-s2")
    # xyz(main_path, "historyrandom-s2-samples", "3-historyrandom-s2")
    # xyz(main_path, "historyrandom-s2-samples", "4-historyrandom-s2")
    # xyz(main_path, "historyrandom-s2-samples", "5-historyrandom-s2")
    # xyz(main_path, "historyrandom-s2-samples", "6-historyrandom-s2")
    # xyz(main_path, "historyrandom-s2-samples", "7-historyrandom-s2")
    # xyz(main_path, "historyrandom-s2-samples", "8-historyrandom-s2")
    # xyz(main_path, "historyrandom-s2-samples", "9-historyrandom-s2")
    #
    # xyz(main_path, "historyrandom-s5-samples", "0-historyrandom-s5")
    # xyz(main_path, "historyrandom-s5-samples", "1-historyrandom-s5")
    # xyz(main_path, "historyrandom-s5-samples", "2-historyrandom-s5")
    # xyz(main_path, "historyrandom-s5-samples", "3-historyrandom-s5")
    # xyz(main_path, "historyrandom-s5-samples", "4-historyrandom-s5")
    # xyz(main_path, "historyrandom-s5-samples", "5-historyrandom-s5")
    # xyz(main_path, "historyrandom-s5-samples", "6-historyrandom-s5")
    # xyz(main_path, "historyrandom-s5-samples", "7-historyrandom-s5")
    # xyz(main_path, "historyrandom-s5-samples", "8-historyrandom-s5")
    # xyz(main_path, "historyrandom-s5-samples", "9-historyrandom-s5")
    print("Creating the last triples...")
    # xyz(main_path, "historyrandom-s10-samples", "0-historyrandom-s10")
    # xyz(main_path, "historyrandom-s10-samples", "1-historyrandom-s10")
    # xyz(main_path, "historyrandom-s10-samples", "2-historyrandom-s10")
    # xyz(main_path, "historyrandom-s10-samples", "3-historyrandom-s10")
    # xyz(main_path, "historyrandom-s10-samples", "4-historyrandom-s10")
    # xyz(main_path, "historyrandom-s10-samples", "5-historyrandom-s10")
    # xyz(main_path, "historyrandom-s10-samples", "6-historyrandom-s10")
    # xyz(main_path, "historyrandom-s10-samples", "7-historyrandom-s10")
    # xyz(main_path, "historyrandom-s10-samples", "8-historyrandom-s10")
    # xyz(main_path, "historyrandom-s10-samples", "9-historyrandom-s10")