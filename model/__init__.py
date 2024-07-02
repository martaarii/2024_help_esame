# Copia incolla MODEL per fare getCaratteristiche
import networkx as nx

class Model():
    def __init__(self):
        self._grafo = nx.Graph()
        self.nodi = []
        self.idMap = {}

    def buildGraph(self):
        self._grafo.clear()
        self.addEdges()

    def addEdges(self):
        self._grafo.clear_edges()

    def ricorsione(self, parziale, v0):
        if v0 in parziale:
            if self.peso(parziale) > self._costBest:
                self._costBest = self.peso(parziale)
                self._solBest = copy.deepcopy(parziale)

        for v in self._grafo.nodes:
            if v not in self._grafo.neighbors(parziale[-1]):
                if v not in parziale:
                    parziale.append(v)
                    self.ricorsione(parziale, v0)
                    parziale.pop()

    def peso(self, parziale):
        peso = 0
        for nodi in parziale:
            peso += nodi.condiment_calories
        return peso

    def getCaratteristiche(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

#PER AGGIUNGERE UN INSIEME DI ARCHI A TUTTI I NODI --> UTILIZZARE ITERTOOL
    myedges = list(itertools.combinations(self._allTeams, 2))
    alternativaaaaaa
    def addEdgePesati(self, year):
        salary = DAO.getAllSalaries(year)
        self.grafo.clear_edges()
        for n1 in self.grafo.nodes:
            for n2 in self.grafo.nodes:
                if n1.ID != n2.ID:
                    self.grafo.add_edge(n1, n2, peso=(salary[n1.ID] + salary[n2.ID]))

    #PER VEDERE I VICINI IN UN GRAFO UTILIZZO
        self.grafo.neighbors(nodo_partenza)

    #PER VEDERE GLI ARCHI ENTRANTI ED USCENTI
    def creaDizionarioBilancio(self):
        self.bilancio = {}
        for n in self._grafo.nodes:
            self.bilancio[n.AlbumId] = 0
            for bil in self._grafo.predecessors(n):
                self.bilancio[n.AlbumId] += float(self._grafo[bil][n]['weight'])
            for bil2 in self._grafo.successors(n):
                self.bilancio[n.AlbumId] -= float(self._grafo[n][bil2]['weight'])
    #OPPURE
    def bilancio(self, nodo):
        entranti = 0
        uscenti = 0
        for archientranti in self.grafo.in_edges(nodo):
            entranti += self.grafo[archientranti[0]][archientranti[1]]["weight"]
        for archiuscenti in self.grafo.out_edges(nodo):
            uscenti += self.grafo[archiuscenti[0]][archiuscenti[1]]["weight"]
        return entranti - uscenti

#Ordinare un dizionario
    list(sorted(self.bestDizio.items(), key=lambda item: item[1], reverse=True))

    #nodi raggiungibili
    def analisi(self, attoreStringa):
        raggiungibili = []
        attore = self._idMapStringa[attoreStringa]
        for nodi in nx.dfs_tree(self.grafo, attore):
            raggiungibili.append((nodi, nodi.last_name))
        return sorted(raggiungibili, key=lambda x: x[1])