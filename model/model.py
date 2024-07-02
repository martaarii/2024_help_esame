//CREAZIONE GRAFO

    def __init__(self):
        self.grafo = nx.Graph()
        self._idMap = {}

    def creaGrafo(self,*):
        self.nodi = DAO.getNodi(*)
        self.grafo.add_nodes_from(self.nodi)
        for v in self.nodi:
            self._idMap[v.id] = v
         self.addEdges(*)
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

//NB: sulla base al metodo utilizzato per la creazione degli archi ->  necessario
// creare una metodo nel DAO che prende tutti gli oggetti di una tipologia
// su cui poi creare la _idMap  dall'init in quel caso:

 def __init__(self):
        self.allOggetti=DAO.getAllOggetti()
        self.grafo = nx.Graph()
        self._idMap = {}
       for v in self.allOggetti:
                self._idMap[v.id] = v

//METODO 1 ARCHI -> creo le connessioni che sono generiche non solo dei nodi del grafo
//per usare questo metodo la idMap deve essere generica
// in base alle necessita le connessioni possono includere o meno il peso

    def addEdges(self, *):
        self.grafo.clear_edges()
        allEdges = DAO.getConnessioni()
        for connessione in allEdges:
            nodo1 = self._idMap[connessione.v1]
            nodo2 = self._idMap[connessione.v2]
            if nodo1 in self.grafo.nodes and nodo2 in self.grafo.nodes:
                if self.grafo.has_edge(nodo1, nodo2) == False:
                    peso = DAO.getPeso(forma, anno, connessione.v1, connessione.v2)
                    self.grafo.add_edge(nodo1, nodo2, weight=peso)


//CLASSE CONNESSIONI (NO PESO E VARIARE STR O INT IN BASE AL CASO)
from dataclasses import dataclass

@dataclass
class Connessione:
    v1:int
    v2:int


    def __str__(self):
        return f"{self.v1} - {self.v2}"

//METODO 2 ARCHI -> itero sui nodi

 def addEdges(self, distanza):
         self.grafo.clear_edges()
         for nodo1 in self.grafo:
             for nodo2 in self.grafo:
                 if nodo1!=nodo2 and self.grafo.has_edge(nodo1, nodo2) == False:
                    posizione1=(nodo1.Latitude, nodo1.Longitude)
                    posizione2 = (nodo2.Latitude, nodo2.Longitude)
                    distanzaCalcolata=geodesic(posizione1,posizione2).kilometers
                    if distanzaCalcolata<=distanza:
                        self.grafo.add_edge(nodo1, nodo2, weight=abs(distanzaCalcolata))
//DATACLASSE TIPO
from dataclasses import dataclass

@dataclass
class Stato:
    id:str
    Name:str
    Capital:str
    Lat:float
    Lng:float
    Area:int
    Population:int
    Neighbors:str


    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"{self.Name}"

  //ORDINARE LISTA DI TUPLE
    ordinaLista=sorted(lista,key=lambda x:x[2], reverse=False)

//ORDINARE DIZIONARIO per valore
    dizioOrdinato= dict(sorted(dizio.items(), key=lambda item: item[1], reverse=True))

//TAGLIARE LA LISTA
  listaOrdinata=listaOrdinata[:3]   -> questo codice mi permette di prendere i primi tre


//CALCOLO DISTANZA
// CON IMPORTAZIONE DI import geopy.distance

posizione1 = (nodo1.lat, nodo1.lng)
posizione2 = (nodo2.lat, nodo2.lng)
distanzaCalcolata= geopy.distance.distance(posizione1, posizione2).km

//arrotondare a tot cifre
rount(numero, numeroCifre)

//splittare
        direttoreid=direttoreStringa.split("-")[0]

//FAR ACCADERE QUALCOSA ALLA SELEZIONE DI UN DD
        self.dd_anno=ft.Dropdown(label="Anno", on_change=self._controller.getSquadre)
//NB captando un evento la funzione nel controller va dafinita così:   def getSquadre(self,e): con l'evento e