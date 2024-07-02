//CONTROLLER:

  def handle_cerca(self,e):
        numeroCondivisi=self._view.txt_attoriCondivisi.value
        if numeroCondivisi=="":
            self._view.create_alert("Inserire un numero massimo totale di attori condivisi")
            return
        direttore = self._view.dd_direttore.value
        if direttore is None:
            self._view.create_alert("Selezionare un direttore")
            return
        costo,listaNodi=self._model.getBestPath(direttore, int(numeroCondivisi))
        self._view.txt_result.controls.append(ft.Text(f"La soluzione migliore è costituita da {costo} attori"))
        for nodo in listaNodi:
            self._view.txt_result.controls.append(ft.Text(f"{nodo}"))
        self._view.update_page()


//RICORSIONE CON UN NODO DI PARTENZA CON MASSIMO PESO TOTALR E VINCOLO SUL NUMERO DI ELEMENTI

    def getBestPath(self, nodoInizialeString, limite):
        self._soluzione = []
        self._costoMigliore = 0
        nodoIniziale = self._idMap[int(nodoInizialeString.split("-")[0])]
        parziale = [nodoIniziale]
        self._ricorsione(parziale,limite)
        return self._costoMigliore,self._soluzione

    def _ricorsione(self, parziale, limite):
        if self.peso(parziale) <= limite:
            if len(parziale)>self._costoMigliore:
                self._soluzione=copy.deepcopy(parziale)
                self._costoMigliore=len(parziale)

            for n in self.grafo.neighbors(parziale[-1]):
                if n not in parziale:
                    parziale.append(n)
                    self._ricorsione(parziale, limite)
                    parziale.pop()
    def peso(self, listaNodi):
        pesoTot = 0
        for i in range(0, len(listaNodi) - 1):
            pesoTot += self.grafo[listaNodi[i]][listaNodi[i + 1]]["weight"]
        return pesoTot

//RICORSIONE CON NODO DI PARTENZA E NODO FINALE CON UN VINCOLO E MASSIMIZZAZIONE DIVERSA (NO PESO)

 def getBestPath(self, limite,nodoInizialeStringa, nodoFinaleStringa):
        self._soluzione = []
        self._costoMigliore = 0
        nodoIniziale = self._idMapNome[nodoInizialeStringa]
        nodoFinale=self._idMapNome[nodoFinaleStringa]
        parziale = [nodoIniziale]
        self._ricorsione(parziale, limite, nodoFinale)
        return self._costoMigliore, self._soluzione

    def _ricorsione(self, parziale, limite, nodoFinale):
        if self.pesoAmmissibile(parziale,limite) and parziale[-1] == nodoFinale:
            if self.count(parziale) > self._costoMigliore:
                self._soluzione = copy.deepcopy(parziale)
                self._costoMigliore = self.count(parziale)

        for n in self.grafo.neighbors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self._ricorsione(parziale, limite,nodoFinale)
                parziale.pop()

    def pesoAmmissibile(self, listaNodi,limite):
        ammissibile=True
        for i in range(0, len(listaNodi) - 1):
            if self.grafo[listaNodi[i]][listaNodi[i + 1]]["weight"]<limite:
                ammissibile=False
        return ammissibile
    def count(self, listaNodi):
        bilancioRiferimento=self.bilancio(listaNodi[0])
        contatore=0
        for nodo in listaNodi:
            if self.bilancio(nodo)>bilancioRiferimento:
                contatore+=1
        return contatore

//RICORSIONE SENZA NODI CONCATENATI EVITANDO I VICINI DI QUELLI GIA' INSERITI
//CON UN NUMERO DI NODI INCLUSI PRECISO E MASSIMIZZAZIONE

    def getBestPath(self,  numeroGiocatori):
        self._soluzione = []
        self._costoMigliore = 0
        battuti=[]
        for nodo in self.grafo.nodes:
            parziale = [nodo]
            for arcoUscente in self.grafo.out_edges(nodo):
                battuti.append(arcoUscente[1])
            self._ricorsione(parziale,numeroGiocatori,battuti)
        return self._costoMigliore,self._soluzione

    def _ricorsione(self, parziale, numeroGiocatori,battuti):
        if len(parziale) == numeroGiocatori:
            if self.grado(parziale)>self._costoMigliore:
                self._soluzione=copy.deepcopy(parziale)
                self._costoMigliore=self.grado(parziale)

        if len(parziale)<numeroGiocatori:
            for n in self.grafo.nodes:
                if n not in parziale and n not in battuti:
                    parziale.append(n)
                    for arcoUscente in self.grafo.out_edges(n):
                        battuti.append(arcoUscente[1])
                    self._ricorsione(parziale,numeroGiocatori,battuti)
                    parziale.pop()
                    for arcoUscente in self.grafo.out_edges(n):
                        battuti.remove(arcoUscente[1])
    def grado(self, listaNodi):
        gradoTot = 0
        for nodo in listaNodi:
            pesoUscente=0
            pesoEntrante=0
            for arcoUscente in self.grafo.out_edges(nodo):
                pesoUscente+= self.grafo[arcoUscente[0]][arcoUscente[1]]["weight"]
            for arcoEntrante in self.grafo.in_edges(nodo):
                pesoEntrante+=self.grafo[arcoEntrante[0]][arcoEntrante[1]]["weight"]
            gradoTot+=pesoUscente-pesoEntrante
        return gradoTot

//RICORSIONE SU GRAFO ORIENTATO CON REQUISITI SPECIFICI QUALI: primo vertice no archi entranti, ultimo vertice no archi uscenti
// vertici intermedi adiacenti e massimizzazione della lunghezza

 def getBestPath(self):
        self._soluzione = []
        self._costoMigliore = 0
        for nodo in self.grafo.nodes:
            if self.grafo.in_degree(nodo)==0:
                parziale = [nodo]
                self._ricorsione(parziale)
        return self._costoMigliore, self._soluzione

    def _ricorsione(self, parziale):
        if self.grafo.out_degree(parziale[-1])==0:
            if len(parziale) > self._costoMigliore:
                self._soluzione = copy.deepcopy(parziale)
                self._costoMigliore = len(parziale)

        for n in self.grafo.successors(parziale[-1]):
            if n not in parziale:
                parziale.append(n)
                self._ricorsione(parziale)
                parziale.pop()


//RICORSIONE CON I NODI APPARTENENTI ALLA STESSA COMPONENTE CONNESSA DI UN NODO INIZIALE

 def getBestPath(self, nodoInizialeString, limite):
        self._soluzione = []
        self._costoMigliore = 0
        componenteConnessa=[]
        nodoIniziale = self._idMapNome[nodoInizialeString]
        for component in nx.connected_components(self.grafo):
            if nodoIniziale in component:
                componenteConnessa=set(component)
        parziale = [nodoIniziale]
        self._ricorsione(parziale, limite,componenteConnessa)
        return self._costoMigliore, self._soluzione

    def _ricorsione(self, parziale, limite,componenteConnessa):
        if self.memoria(parziale) <= limite:
            if len(parziale) > self._costoMigliore:
                self._soluzione = copy.deepcopy(parziale)
                self._costoMigliore = len(parziale)

            for n  in componenteConnessa:
                if n not in parziale:
                    parziale.append(n)
                    self._ricorsione(parziale, limite,componenteConnessa)
                    parziale.pop()

    def memoria(self, listaNodi):
        memoriaTot=0
        for nodo in listaNodi:
            memoriaTot+=nodo.Bytes
        return memoriaTot

//CAMMINO O PERCORSO = SELF.GRAFO.NEIGHBOURS
//LISTA/INSEIEM -> non ci interessa se sono concatenati -> self.grafo.nodes

//RICORSIONE CON NODI NON RIPETUTI, INSIEME DI TOT ELEMENTI E ULTIMO NODO COINCIDENTE CON IL PRIMO

    def getBestPath(self, limiteEsatto):
        self._soluzione = []
        self._costoMigliore = 0
        for nodo in self.grafo.nodes:
            parziale=[nodo]
            self._ricorsione(parziale,limiteEsatto+1)
        return self._costoMigliore,self._soluzione

    def _ricorsione(self, parziale, limiteEsatto):
        if len(parziale) == limiteEsatto:
            if self.peso(parziale)>self._costoMigliore:
                self._soluzione=copy.deepcopy(parziale)
                self._costoMigliore=self.peso(parziale)

        if len(parziale)<limiteEsatto:
            for n in self.grafo.neighbors(parziale[-1]):
                if len(parziale)==limiteEsatto-1 and n==parziale[0]:
                        parziale.append(n)
                        self._ricorsione(parziale, limiteEsatto)
                        parziale.pop()
                if len(parziale)<limiteEsatto-1 and n not in parziale:
                    parziale.append(n)
                    self._ricorsione(parziale, limiteEsatto)
                    parziale.pop()

    def peso(self, listaNodi):
        pesoTot = 0
        for i in range(0, len(listaNodi) - 1):
            pesoTot += self.grafo[listaNodi[i]][listaNodi[i + 1]]["weight"]
        return pesoTot

//RICORSIONE MASSIMIZZARE LA DISTANZA E PESO CRESCENTE
    def getBestPath(self):
        self._soluzione = []
        self._costoMigliore = 0
        for nodo in self.grafo.nodes:
                parziale = [nodo]
                self._ricorsione(parziale)
        return self._costoMigliore, self._soluzione

    def _ricorsione(self, parziale):
        if self.distanza(parziale) > self._costoMigliore:
                self._soluzione = copy.deepcopy(parziale)
                self._costoMigliore = self.distanza(parziale)

        for n in self.grafo.neighbors(parziale[-1]):
            if n not in parziale:
                if len(parziale)>=2:
                    if self.grafo[parziale[-1]][n]["weight"]>self.grafo[parziale[-1]][parziale[-2]]["weight"]:
                        parziale.append(n)
                        self._ricorsione(parziale)
                        parziale.pop()
                else:
                    parziale.append(n)
                    self._ricorsione(parziale)
                    parziale.pop()

    def distanza(self,listaNodi):
        distanzaTot=0
        for i in range(0, len(listaNodi) - 1):
            stato1=listaNodi[i]
            stato2=listaNodi[i+1]
            posizione1=(stato1.Lat,stato1.Lng)
            posizione2 = (stato2.Lat, stato2.Lng)
            distanza = distance.geodesic(posizione1, posizione2).km
            distanzaTot+=distanza
            self.dista[f"{stato1.id}-{stato2.id}"]=distanza
        return distanzaTot