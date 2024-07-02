// VALIDAZIONE CAMPI:

// dropdown
porzione = self._view.ddporzione.value
if porzione is None:
    self._view.create_alert("Selezionare un tipo di porzione")
    return
dizio = self._model.analisi(porzione)

// textfield:
calorie = self._view.txtcalorie.value
if calorie == "":
    self._view.create_alert("Inserire un valore numerico per le calorie")
    return
grafo = self._model.creaGrafo(int(calorie))

// NB: in entrambi
i
casi
il
cast
del valore(se
necessario) va
fatto
dopo
altrimenti
da
errore

/ RIMPIRE
IL
DROPDOWN -> ricordati
di
chiamare
self._controller.fillDD()
NELLA
VIEW
DOPO
// DOPO
LA
CREAZIONE
DEL
DD


def fillDD(self):
    ann = "201"
    for i in range(5, 9):
        anno = ann + str(i)
        self._view.dd_anno.options.append(ft.dropdown.Option(
            text=anno))

// RIEMPIRE
IL
IL
DD
DA
UNA
COLONNA / TABELLA
DEL
DATABASE
// NB
se
nazioni
fosse
costituita
da
Oggetti
bisogna
accertarsi
che
il
metodo
/ str
stampa
ciò
che
desideriamo
inserire
nel
DD

nazioni = self._model.getNazioni
for nazione in nazioni:
    self._view.dd_nazione.options.append(ft.dropdown.Option(
        text=nazione))

// CREA
GRAFO -> Ricordarsi
la
validazione
dei
campi
se
necessario


def handle_grafo(self, e):
    nazione = self._view.dd_nazione.value
    if nazione is None:
        self._view.create_alert("Selezionare una Nazione")
        return
    anno = self._view.dd_anno.value
    if anno is None:
        self._view.create_alert("Selezionare un Anno")
        return
    nProdotti = self._view.txt_prodotti.value
    if nProdotti == "":
        self._view.create_alert("Inserire un valore numerico per il numero di prodotti in comune")
        return
    grafo = self._model.creaGrafo(nazione, int(anno), int(nProdotti))
    self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
    self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                  f"{self._model.getNumNodes()} nodi."))
    self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                  f"{self._model.getNumEdges()} archi."))
    self._view.update_page()

// CREATE
ALERT:


def create_alert(self, message):
    dlg = ft.AlertDialog(title=ft.Text(message))
    self._page.dialog = dlg
    dlg.open = True
    self._page.update()

// UN
DD
CHE
SI
POPOLA
AL
CLICK
SULL
ALTRO


def fillDDanno(self):
    anni = self._model.getAnni
    for anno in anni:
        self._view.dd_anno.options.append(ft.dropdown.Option(
            text=anno))


def fillDDforme(self, e):
    self._view.dd_shape.options = []
    forme = self._model.getForme(int(self._view.dd_anno.value))
    for forma in forme:
        self._view.dd_shape.options.append(ft.dropdown.Option(
            text=forma))
    self._view.update_page()


SU
VIEW:
self.dd_anno = ft.Dropdown(label="Anno", on_change=self._controller.fillDDforme)
self.dd_shape = ft.Dropdown(label="Shape")
self._controller.fillDDanno()