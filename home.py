import pickle
import time
from multiprocessing import Pool

from pymantic import sparql

from Sampler import Machine

machine = Machine("http://localhost:9999/blazegraph/sparql")
machine.initialize()

"""
Run a sampling machine.
"""


def create_sample(nb_of_agents, sample_size, s_type, file_name, m):
    m.reset(nb_of_agents, sample_size)
    m.execute_simulations(s_type)
    path = "/home/user/results/" + file_name
    m.save_results(path)

    print("Finished sample " + file_name)


"""
This method collects all the tripled where the subject is sampled by the machine.
"""


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

    """
    This method collects the sampled triples simultaneously and piles them up in one file.
    """


    def pool_triples(path, f_name):
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

create_sample(70, 2000, "h", "historyv2-s2.obj", machine)

pool_triples(main_path, "one-random0")
