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

    def addEdges2(self, *):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni()
        for connessione in allEdges:
            nodo1 = self._idMap[connessione.v1]
            nodo2 = self._idMap[connessione.v2]
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:
                    peso = DAO.getPeso(forma, anno, connessione.v1, connessione.v2)
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)

    // METODO 3 archi -> itero sui nodi

    def addEdges(self, distanza):
        self.grafo.clear_edges()
        for nodo1 in self._grafo:
            for nodo2 in self._grafo:
                if nodo1 != nodo2 and self._grafo.has_edge(nodo1, nodo2) == False:
                    posizione1 = (nodo1.Latitude, nodo1.Longitude)
                    posizione2 = (nodo2.Latitude, nodo2.Longitude)
                    distanzaCalcolata = geodesic(posizione1, posizione2).kilometers
                    if distanzaCalcolata <= distanza:
                        self.grafo.add_edge(nodo1, nodo2, weight=abs(distanzaCalcolata))

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

    # nodi raggiungibili
    def analisi(self, attoreStringa):
        raggiungibili = []
        attore = self._idMapStringa[attoreStringa]
        for nodi in nx.dfs_tree(self.grafo, attore):
            raggiungibili.append((nodi, nodi.last_name))
        return sorted(raggiungibili, key=lambda x: x[1])

        # oppure
    def esistePercorso(self, v0, v1):
            connessa = nx.node_connected_component(self._grafo, v0)
            if v1 in connessa:
                return True

            return False

        def trovaCamminoD(self, v0, v1):
            return nx.dijkstra_path(self._grafo, v0, v1)

        def trovaCamminoBFS(self, v0, v1):
            tree = nx.bfs_tree(self._grafo, v0)
            if v1 in tree:
                print(f"{v1} è presente nell'albero di visita BFS")
            path = [v1]

            while path[-1] != v0:
                path.append(list(tree.predecessors(path[-1]))[0])

            path.reverse()
            return path

        def trovaCamminoDFS(self, v0, v1):
            tree = nx.dfs_tree(self._grafo, v0)
            if v1 in tree:
                print(f"{v1} è presente nell'albero di visita DFS")
            path = [v1]

            while path[-1] != v0:
                path.append(list(tree.predecessors(path[-1]))[0])

            path.reverse()
            return path
