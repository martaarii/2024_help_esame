class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._listYear = []
        self._listShape = []
def fillDD(self):
    self._view.ddingredienti.options.clear()
    for n in self._model._grafo.nodes:
        self._view.ddingredienti.options.append(
            ft.dropdown.Option(data=n, text=n.display_name, on_click=self.readDD))


def readDD(self, e):
    if e.control.data is None:
        self.choiceIngredient = None
    else:
        self.choiceIngredient = e.control.data

    def fillDDAnnoForme(self):
        anni = self._model.getYears()
        forme = self._model.getShapes()
        for anno in anni:
            self._view.ddyear.options.append(ft.dropdown.Option(text=anno))
        for forma in forme:
            self._view.ddshape.options.append(ft.dropdown.Option(text=forma))
        self._view.update_page()

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