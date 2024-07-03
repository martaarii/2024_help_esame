class Controller:
    def __init__(self):
        pass
    def fillDD(self):
        self._view.ddingredienti.options.clear()
        for n in self._model._grafo.nodes:
            self._view.ddingredienti.options.append(
                # se non funziona aggiorna!!
                ft.dropdown.Option(data=n, text=n.display_name, on_click=self.readDD))

    def readDD(self, e):
        if e.control.data is None:
            self.choiceIngredient = None
        else:
            self.choiceIngredient = e.control.data

#nel caso in cui mancasse il create alert nel VIEW
    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def handleGraph(self, e):
        nMinStr = self._view._txtInNumC.value
        try:
            nMin = int(nMinStr)
        except ValueError:
            self._view.txt_result.controls.append(ft.Text("Inserire un intero!"))
            self._view.update_page()
            return

        self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodi()}\n"
                                                      f"Numero di archi: {self._model.getNumArchi()}"))
        self._view.update_page()


