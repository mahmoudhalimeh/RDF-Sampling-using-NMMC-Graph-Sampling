import pickle
import time
from multiprocessing import Pool

from pymantic import sparql

from Sampler import Machine

# 2100, 5500, 10500
# h, r, hr

# machine = Machine("http://localhost:9999/blazegraph/sparql")
# machine.initialize()
#
#
# def create_sample(nb_of_agents, sample_size, s_type, file_name, m):
#     m.reset(nb_of_agents, sample_size)
#     m.execute_simulations(s_type)
#     path = "/home/user/results/" + file_name
#     m.save_results(path)
#
#     print("Finished sample " + file_name)
#     # file = open(path, 'rb')
#     # obj = pickle.load(file)
#     # file.close()
#
#
# create_sample(1, 146000, "r", "one-random0.obj", machine)
# create_sample(1, 146000, "r", "one-random1.obj", machine)
# create_sample(1, 146000, "r", "one-random2.obj", machine)
#
# create_sample(1, 146000, "hr", "one-historyrandom0.obj", machine)
# create_sample(1, 146000, "hr", "one-historyrandom1.obj", machine)
# create_sample(1, 146000, "hr", "one-historyrandom2.obj", machine)
#
# create_sample(1, 146000, "h", "one-history0.obj", machine)
# create_sample(1, 146000, "h", "one-history1.obj", machine)
# create_sample(1, 146000, "h", "one-history2.obj", machine)




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

    xyz(main_path, "one-random0")
    xyz(main_path, "one-random1")
    xyz(main_path, "one-random2")

    xyz(main_path, "one-historyrandom0")
    xyz(main_path, "one-historyrandom1")
    xyz(main_path, "one-historyrandom2")

    xyz(main_path, "one-history0")
    xyz(main_path, "one-history1")
    xyz(main_path, "one-history2")











# create_sample(70, 2100, "h", "3-historyv2-s2.obj", machine)
# create_sample(70, 2100, "h", "4-historyv2-s2.obj", machine)
# create_sample(70, 2100, "h", "5-historyv2-s2.obj", machine)
# create_sample(70, 2100, "h", "6-historyv2-s2.obj", machine)
# create_sample(70, 2100, "h", "7-historyv2-s2.obj", machine)
# create_sample(70, 2100, "h", "8-historyv2-s2.obj", machine)
# create_sample(70, 2100, "h", "9-historyv2-s2.obj", machine)
#
# create_sample(70, 5500, "h", "0-historyv2-s5.obj", machine)
# create_sample(70, 5500, "h", "1-historyv2-s5.obj", machine)
# create_sample(70, 5500, "h", "2-historyv2-s5.obj", machine)
# create_sample(70, 5500, "h", "3-historyv2-s5.obj", machine)
# create_sample(70, 5500, "h", "4-historyv2-s5.obj", machine)
# create_sample(70, 5500, "h", "5-historyv2-s5.obj", machine)
# create_sample(70, 5500, "h", "6-historyv2-s5.obj", machine)
# create_sample(70, 5500, "h", "7-historyv2-s5.obj", machine)
# create_sample(70, 5500, "h", "8-historyv2-s5.obj", machine)
# create_sample(70, 5500, "h", "9-historyv2-s5.obj", machine)

# create_sample(70, 10500, "h", "0-historyv2-s10.obj", machine)
# create_sample(70, 10500, "h", "1-historyv2-s10.obj", machine)
# create_sample(70, 10500, "h", "2-historyv2-s10.obj", machine)
# create_sample(70, 10500, "h", "3-historyv2-s10.obj", machine)
# create_sample(70, 10500, "h", "4-historyv2-s10.obj", machine)
# create_sample(70, 10500, "h", "5-historyv2-s10.obj", machine)
# create_sample(70, 10500, "h", "6-historyv2-s10.obj", machine)
# create_sample(70, 10500, "h", "7-historyv2-s10.obj", machine)
# create_sample(70, 10500, "h", "8-historyv2-s10.obj", machine)
# create_sample(70, 10500, "h", "9-historyv2-s10.obj", machine)


# create_sample(70, 2100, "r", "0-randomv2-s2.obj", machine)
# create_sample(70, 2100, "r", "1-randomv2-s2.obj", machine)
# create_sample(70, 2100, "r", "2-randomv2-s2.obj", machine)
# create_sample(70, 2100, "r", "3-randomv2-s2.obj", machine)
# create_sample(70, 2100, "r", "4-randomv2-s2.obj", machine)
# create_sample(70, 2100, "r", "5-randomv2-s2.obj", machine)
# create_sample(70, 2100, "r", "6-randomv2-s2.obj", machine)
# create_sample(70, 2100, "r", "7-randomv2-s2.obj", machine)
# create_sample(70, 2100, "r", "8-randomv2-s2.obj", machine)
# create_sample(70, 2100, "r", "9-randomv2-s2.obj", machine)


# create_sample(70, 5500, "r", "0-randomv2-s5.obj", machine)
# create_sample(70, 5500, "r", "1-randomv2-s5.obj", machine)
# create_sample(70, 5500, "r", "2-randomv2-s5.obj", machine)
# create_sample(70, 5500, "r", "3-randomv2-s5.obj", machine)
# create_sample(70, 5500, "r", "4-randomv2-s5.obj", machine)
# create_sample(70, 5500, "r", "5-randomv2-s5.obj", machine)
# create_sample(70, 5500, "r", "6-randomv2-s5.obj", machine)
# create_sample(70, 5500, "r", "7-randomv2-s5.obj", machine)
# create_sample(70, 5500, "r", "8-randomv2-s5.obj", machine)
# create_sample(70, 5500, "r", "9-randomv2-s5.obj", machine)


# create_sample(70, 10500, "r", "0-randomv2-s10.obj", machine)
# create_sample(70, 10500, "r", "1-randomv2-s10.obj", machine)
# create_sample(70, 10500, "r", "2-randomv2-s10.obj", machine)
# create_sample(70, 10500, "r", "3-randomv2-s10.obj", machine)
# create_sample(70, 10500, "r", "4-randomv2-s10.obj", machine)
# create_sample(70, 10500, "r", "5-randomv2-s10.obj", machine)
# create_sample(70, 10500, "r", "6-randomv2-s10.obj", machine)
# create_sample(70, 10500, "r", "7-randomv2-s10.obj", machine)
# create_sample(70, 10500, "r", "8-randomv2-s10.obj", machine)
# create_sample(70, 10500, "r", "9-randomv2-s10.obj", machine)
#


# create_sample(70, 2100, "hr", "0-historyrandomv2-s2.obj", machine)
# create_sample(70, 2100, "hr", "1-historyrandomv2-s2.obj", machine)
# create_sample(70, 2100, "hr", "2-historyrandomv2-s2.obj", machine)
# create_sample(70, 2100, "hr", "3-historyrandomv2-s2.obj", machine)
# create_sample(70, 2100, "hr", "4-historyrandomv2-s2.obj", machine)
# create_sample(70, 2100, "hr", "5-historyrandomv2-s2.obj", machine)
# create_sample(70, 2100, "hr", "6-historyrandomv2-s2.obj", machine)
# create_sample(70, 2100, "hr", "7-historyrandomv2-s2.obj", machine)
# create_sample(70, 2100, "hr", "8-historyrandomv2-s2.obj", machine)
# create_sample(70, 2100, "hr", "9-historyrandomv2-s2.obj", machine)


# create_sample(70, 5500, "hr", "0-historyrandomv2-s5.obj", machine)
# create_sample(70, 5500, "hr", "1-historyrandomv2-s5.obj", machine)
# create_sample(70, 5500, "hr", "2-historyrandomv2-s5.obj", machine)
# create_sample(70, 5500, "hr", "3-historyrandomv2-s5.obj", machine)
# create_sample(70, 5500, "hr", "4-historyrandomv2-s5.obj", machine)
# create_sample(70, 5500, "hr", "5-historyrandomv2-s5.obj", machine)
# create_sample(70, 5500, "hr", "6-historyrandomv2-s5.obj", machine)
# create_sample(70, 5500, "hr", "7-historyrandomv2-s5.obj", machine)
# create_sample(70, 5500, "hr", "8-historyrandomv2-s5.obj", machine)
# create_sample(70, 5500, "hr", "9-historyrandomv2-s5.obj", machine)


# create_sample(70, 10500, "hr", "0-historyrandomv2-s10.obj", machine)
# create_sample(70, 10500, "hr", "1-historyrandomv2-s10.obj", machine)
# create_sample(70, 10500, "hr", "2-historyrandomv2-s10.obj", machine)
# create_sample(70, 10500, "hr", "3-historyrandomv2-s10.obj", machine)
# create_sample(70, 10500, "hr", "4-historyrandomv2-s10.obj", machine)
# create_sample(70, 10500, "hr", "5-historyrandomv2-s10.obj", machine)
# create_sample(70, 10500, "hr", "6-historyrandomv2-s10.obj", machine)
# create_sample(70, 10500, "hr", "7-historyrandomv2-s10.obj", machine)
# create_sample(70, 10500, "hr", "8-historyrandomv2-s10.obj", machine)
# create_sample(70, 10500, "hr", "9-historyrandomv2-s10.obj", machine)


# machine = Machine(70, 2100, "http://localhost:9999/blazegraph/sparql", "h")
# machine.initialize()
# machine.execute_simulations()
# machine.save_results("/home/user/results/history/2/1-random-s2.obj")

# file = open("/home/user/results/random-s2.obj", 'rb')
# obj = pickle.load(file)
# file.close()

# print("Init duration: " + str(obj.duration_init))
# print("Number of cores: " + str(len(obj.durations)))
# print("Results: " + str(len(obj.results)))


# f = open("/home/user/results/history/2/1-triples-history-s2.txt", "w", encoding="utf-8")
#
#
# def execute(s):
#     server = sparql.SPARQLServer('http://localhost:9999/blazegraph/sparql')
#     predicates = set()
#     q = "Select * where {<" + s + "> ?p ?o. }"
#     result = server.query(q)
#     for res in result['results']['bindings']:
#         # s = "<" + s + ">   "
#         p = res['p']['value']
#         predicates.add(p)
#         o = ""
#         if res['o']['type'] == "uri":
#             o = "<" + res['o']['value'] + ">"
#         else:
#             o = "\"" + res['o']['value'] + "\""
#         f.write("<" + s + ">   <" + p + ">   " + o + ".\n")
#
#
# if __name__ == '__main__':
#     ti = time.perf_counter()
#
#     pool = Pool(70)
#     pool.map(execute, obj.results)
#
#     te = time.perf_counter()
#     f.close()
#     print(f"Created triples file in {te - ti:0.4f} seconds")
