from datetime import datetime
import multiprocessing
import operator
from pymantic import sparql
import numpy as np
import random
import time
from scipy.sparse import lil_matrix
import pickle


class MachineResult:

    def __init__(self, duration_init, length, durations, accepted, rejected, ended, results):
        self.duration_init = duration_init
        self.length = length
        self.durations = durations
        self.accepted = accepted
        self.rejected = rejected
        self.ended = ended
        self.results = results


class Machine:
    matrix = []
    length = 0
    nodes = {}
    in_degrees = {}
    out_degrees = {}
    nodes_inverse = {}

    acc_list = []
    in_list = []
    out_list = []
    constant_c = 0
    max_out_degree_index = 0

    starting_nodes = []

    distinct_subjects = set()
    distinct_subjects_inverse = []

    duration_init = 0

    durations = []
    accepted = []
    rejected = []
    ended = []
    results = []

    triples_size = 0

    nb_of_agents = 0
    items_per_agent = 0

    def __init__(self, server):
        self.server = sparql.SPARQLServer(server)

    def reset(self, nb_of_agents, items_per_agent):
        self.durations = []
        self.accepted = []
        self.rejected = []
        self.ended = []
        self.results = []
        self.nb_of_agents = nb_of_agents
        self.items_per_agent = items_per_agent

    def get_triple_count(self):
        q = "SELECT (COUNT(*) AS ?count) WHERE { ?s ?p ?o. }"
        result = self.server.query(q)
        for res in result['results']['bindings']:
            self.triples_size = res['count']['value']

    def get_iri_in_out_degrees(self):
        q = """
        select distinct ?iri (SUM(?incoming) as ?in) (SUM(?outgoing) as ?out)
        where {
          {
            {
            select distinct ?iri (count(?col1) as ?incoming) (0 as ?outgoing)
            where
            {
                ?col1 ?col2 ?iri. 
                filter (isIRI(?iri))
            }group by ?iri
            }
            union {
              select distinct ?iri (0 as ?incoming) (count(?col2) as ?outgoing) 
                where
                {
                    ?iri ?col1 ?col2 .
                }group by ?iri
              }
          }
        } group by ?iri
            """
        result = self.server.query(q)
        current = 0
        for res in result['results']['bindings']:
            self.nodes[res['iri']['value']] = current
            self.in_degrees[current] = int(res['in']['value'])
            self.out_degrees[current] = int(res['out']['value'])

            self.in_list.append(int(res['in']['value']))
            self.out_list.append(int(res['out']['value']))

            current = current + 1

        return current

    def get_adjacency_matrix(self):
        q = 'Select ?s ?o Where {?s ?p ?o. Filter isIRI(?o)}'
        result = self.server.query(q)
        for res1 in result['results']['bindings']:
            try:
                self.matrix[self.nodes[res1['s']['value']], self.nodes[res1['o']['value']]] = 1
            except:
                continue

    def get_transition_matrix(self):
        for i in range(0, self.length):
            if sum(self.matrix.data[i]) > 0:
                self.matrix.data[i] = self.matrix.data[i] / sum(self.matrix.data[i])

    def get_distinct_nodes(self):
        subjects = set()
        objects = set()

        q = "SELECT distinct ?s WHERE { ?s ?p ?o. }"
        result = self.server.query(q)
        for res in result['results']['bindings']:
            s = res['s']['value']
            subjects.add(s)

        q = "SELECT distinct ?o WHERE { ?s ?p ?o. }"
        result = self.server.query(q)
        for res in result['results']['bindings']:
            o = res['o']['value']
            objects.add(o)

        self.distinct_subjects = subjects.difference(objects)

    def select_start_nodes(self):
        print("Select start nodes.")
        random.choice(self.distinct_subjects_inverse)

        # i = 0
        # while i < self.nb_of_agents:
        #     rand = random.choice(self.distinct_subjects_inverse)
        #     if rand not in self.starting_nodes and int(self.out_degrees[rand]) > 0:
        #         self.starting_nodes.append(rand)
        #         i = i + 1

        i = 0
        while i < self.nb_of_agents:
            rand = random.randint(0, self.length - 1)
            if rand not in self.starting_nodes:
                self.starting_nodes.append(rand)
                i = i + 1

    def create_results(self, res):
        print("Creating results...")
        for i in res:
            self.results.append(self.nodes_inverse[i])

    def add_agent(self, node, q, sim_type):
        agent = Agent(node, self.length, self.matrix, self.acc_list, self.items_per_agent, sim_type, self.nodes_inverse)
        res = agent.simulate()
        q.put(res)

    def execute_simulations(self, sim_type):
        print("Machine simulation started...")

        if len(self.starting_nodes) > 1:
            rand = random.randint(0, self.length - 1)

            agent = Agent(rand, self.length, self.matrix, self.acc_list, self.items_per_agent, sim_type, self.nodes_inverse)
            res = agent.simulate()
            self.accepted.append(res.accepted)
            self.rejected.append(res.rejected)
            self.ended.append(res.ended)
            self.durations.append(res.duration)

            for i in res.results:
                self.results.append(self.nodes_inverse[i])

        else:

            q = multiprocessing.Queue()
            manager = multiprocessing.Manager()
            ret = manager.dict()
            processes = []
            for i in self.starting_nodes:
                p = multiprocessing.Process(target=self.add_agent, args=(i, q, sim_type))
                processes.append(p)
                p.start()

            count = 0
            for p in processes:
                res = q.get()
                self.accepted.append(res.accepted)
                self.rejected.append(res.rejected)
                self.ended.append(res.ended)
                self.durations.append(res.duration)

                # print(len(res.results))
                # print(res.results[0])

                for i in res.results:
                    self.results.append(self.nodes_inverse[i])

                count += 1

            for process in processes:
                process.join()

    def initialize(self):
        print("Machine initialization started...")
        t_init = time.perf_counter()

        self.length = self.get_iri_in_out_degrees()

        index = max(self.out_degrees.items(), key=operator.itemgetter(1))[0]

        in_deg = int(self.in_degrees[index])
        out_deg = int(self.out_degrees[index])

        self.constant_c = out_deg / in_deg

        self.matrix = lil_matrix((self.length, self.length), dtype=np.float64)

        self.get_adjacency_matrix()
        self.get_transition_matrix()

        for i in range(0, self.length):
            if self.in_list[i] > 0:
                self.acc_list.append(self.out_list[i] / (self.in_list[i] * self.constant_c))
            else:
                self.acc_list.append(self.out_list[i] / self.constant_c)

        self.nodes_inverse = {v: k for k, v in self.nodes.items()}

        self.get_distinct_nodes()

        for i in self.distinct_subjects:
            self.distinct_subjects_inverse.append(self.nodes[i])

        self.select_start_nodes()

        t_end = time.perf_counter()

        self.duration_init = t_end - t_init

    def save_results(self, path):
        self.results = set(self.results)
        m = MachineResult(self.duration_init, self.length, self.durations, self.accepted, self.rejected,
                          self.ended, self.results)

        filehandler = open(path, "wb")
        pickle.dump(m, filehandler)
        filehandler.close()


class Agent:
    results = set()
    accepted = 0
    rejected = 0
    ended = 0
    duration = 0

    def __init__(self, starting_node, length, matrix, acc_list, items_per_agent, agent_type, nodes_inverse):
        self.starting_node = starting_node
        self.length = length
        self.matrix = matrix
        self.acc_list = acc_list
        self.iterations = items_per_agent
        self.type = agent_type
        self.nodes_inverse = nodes_inverse

    def select_next_node(self, node):
        weights = self.matrix.data[node]
        indexes = self.matrix.getrow(node).nonzero()[1]

        if len(indexes) == 0:
            return -1
        x = random.choices(indexes, weights=weights, k=1)
        x = x[0]
        return x

    def simulate(self):
        if self.type == "r":
            self.simulate_random()
        elif self.type == "h":
            self.simulate_history()
        elif self.type == "ht":
            self.simulate_history_top()
        elif self.type == "hr":
            self.simulate_history_random_mix()
        elif self.type == "srw":
            self.simulate_srw()

        return AgentResult(self.results, self.accepted, self.rejected, self.ended, self.duration)

    def simulate_srw(self):
        t_i = time.perf_counter()

        print("Agent simulation srw started...")

        current_node = self.starting_node

        self.results.add(current_node)

        while len(self.results) < self.iterations:
            next_node = self.select_next_node(current_node)

            if next_node == -1:
                next_node = random.randrange(0, self.length)
                self.ended += 1
            else:
                self.accepted += 1

            self.results.add(next_node)
            current_node = next_node

        t_e = time.perf_counter()
        self.duration = t_e - t_i

        print(f"While loop ended in {self.duration:0.4f} seconds")

    def simulate_random(self):
        t_i = time.perf_counter()

        print("Agent simulation random started with length: " + str(self.length))
        current_node = self.starting_node

        self.results.add(current_node)

        while len(self.results) < self.iterations:
            # print(len(self.results))
            next_node = self.select_next_node(current_node)

            if next_node == -1:
                next_node = random.randrange(0, self.length)
                self.ended += 1
            elif random.uniform(0, 1) > self.acc_list[current_node]:
                next_node = random.randrange(0, self.length)
                self.rejected += 1
            else:
                self.accepted += 1

            # if "thesis/skolemized" not in self.nodes_inverse[next_node]:
            #     self.results.add(next_node)
            self.results.add(next_node)
            current_node = next_node

        t_e = time.perf_counter()
        self.duration = t_e - t_i

        print(f"While loop ended in {self.duration:0.4f} seconds")

    def simulate_history(self):
        t_i = time.perf_counter()
        start = datetime.now()

        print("Agent simulation history started...")

        historical_distribution = lil_matrix((1, self.length - 1), dtype=np.float64)

        current_node = self.starting_node

        self.results.add(current_node)

        historical_distribution[0, current_node] = historical_distribution[0, current_node] + 1

        # for i in range(0, 100):
        #     next_node = self.select_next_node(current_node)
        #
        #     if next_node >= 0:
        #         self.results.add(next_node)
        #         historical_distribution[0, next_node] = historical_distribution[0, next_node] + 1
        #         current_node = next_node
        #     else:
        #         current_node = random.randrange(0, self.length)
        #         historical_distribution[0, current_node] = historical_distribution[0, current_node] + 1

        terminated = True

        while len(self.results) < self.iterations:
            # print(len(self.results))
            # if (datetime.now() - start).total_seconds() > 100:
            #     terminated = True
            #     break

            next_node = self.select_next_node(current_node)
            if next_node == -1:
                weights = historical_distribution.data[0]
                indexes = historical_distribution.getrow(0).nonzero()[1]
                next_node = random.choices(indexes, weights=weights, k=1)
                next_node = next_node[0]
                self.ended += 1
            elif random.uniform(0, 1) > self.acc_list[current_node]:
                weights = historical_distribution.data[0]
                indexes = historical_distribution.getrow(0).nonzero()[1]
                next_node = random.choices(indexes, weights=weights, k=1)
                next_node = next_node[0]
                self.rejected += 1
            else:
                historical_distribution[0, next_node] = historical_distribution[0, next_node] + 1
                self.accepted += 1

            self.results.add(next_node)
            current_node = next_node

        t_e = time.perf_counter()
        self.duration = t_e - t_i

        # if terminated:
        #     print(f"While loop terminated in {t_e - t_i:0.4f} seconds")
        # else:
        print(f"While loop ended in {t_e - t_i:0.4f} seconds")

    def simulate_history_random_mix(self):
        t_i = time.perf_counter()

        print("Agent simulation history random started...")

        historical_distribution = lil_matrix((1, self.length - 1), dtype=np.float64)

        current_node = self.starting_node

        self.results.add(current_node)

        historical_distribution[0, current_node] = historical_distribution[0, current_node] + 1

        # for i in range(0, 100):
        #     next_node = self.select_next_node(current_node)
        #
        #     if next_node >= 0:
        #         self.results.add(next_node)
        #         historical_distribution[0, next_node] = historical_distribution[0, next_node] + 1
        #         current_node = next_node
        #     else:
        #         current_node = random.randrange(0, self.length)
        #         historical_distribution[0, current_node] = historical_distribution[0, current_node] + 1

        while len(self.results) < self.iterations:
            next_node = self.select_next_node(current_node)
            if next_node == -1:
                next_node = random.randrange(0, self.length)
                historical_distribution[0, next_node] = historical_distribution[0, next_node] + 1
                self.ended += 1
            elif random.uniform(0, 1) > self.acc_list[current_node]:
                weights = historical_distribution.data[0]
                indexes = historical_distribution.getrow(0).nonzero()[1]
                next_node = random.choices(indexes, weights=weights, k=1)
                next_node = next_node[0]
                self.rejected += 1
            else:
                historical_distribution[0, next_node] = historical_distribution[0, next_node] + 1
                self.accepted += 1

            self.results.add(next_node)
            current_node = next_node

        t_e = time.perf_counter()
        self.duration = t_e - t_i
        print(f"While loop ended in {t_e - t_i:0.4f} seconds")

    def simulate_history_top(self):
        t_i = time.perf_counter()

        print("Agent simulation history top started...")

        current_node = self.starting_node

        self.results.add(current_node)

        his_indexes = []
        his_weights = []

        his_weights.append(1)
        his_indexes.append(current_node)

        for i in range(0, 100):
            next_node = self.select_next_node(current_node)

            if next_node >= 0:
                self.results.add(next_node)
                if next_node in his_indexes:
                    ind = his_indexes.index(next_node)
                    his_weights[ind] += 1
                else:
                    his_indexes.append(next_node)
                    his_weights.append(1)
                current_node = next_node
            else:
                current_node = random.randrange(0, self.length)

                if next_node in his_indexes:
                    ind = his_indexes.index(next_node)
                    his_weights[ind] += 1
                else:
                    his_indexes.append(next_node)
                    his_weights.append(1)

        while len(self.results) < self.iterations:
            next_node = self.select_next_node(current_node)
            # print(len(self.results))
            if next_node == -1:
                max_value = max(his_weights)
                max_index = his_weights.index(max_value)
                next_node = his_indexes[max_index]
                self.ended += 1
            elif random.uniform(0, 1) > self.acc_list[current_node]:
                max_value = max(his_weights)
                max_index = his_weights.index(max_value)
                next_node = his_indexes[max_index]
                self.rejected += 1
            else:
                if next_node in his_indexes:
                    ind = his_indexes.index(next_node)
                    his_weights[ind] += 1
                else:
                    his_indexes.append(next_node)
                    his_weights.append(1)
                self.accepted += 1

            self.results.add(next_node)
            current_node = next_node

        t_e = time.perf_counter()
        self.duration = t_e - t_i
        print(f"While loop ended in {self.duration:0.4f} seconds")


class AgentResult:

    def __init__(self, results, accepted, rejected, ended, duration):

        self.results = results
        self.accepted = accepted
        self.rejected = rejected
        self.ended = ended
        self.duration = duration