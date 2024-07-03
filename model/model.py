//CLASSE CONNESSIONI (NO PESO E VARIARE STR O INT IN BASE AL CASO)
from dataclasses import dataclass
import datetime
@dataclass
class Connessione:
    v1:int
    v2:int
    def __str__(self):
        return f"{self.v1} - {self.v2}"

// CLASSE STATO
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

// CLASSE AVVISTAMENTO
@dataclass
class sighting:
    id: int
    datetime: datetime
    city: str
    state: str
    country: str
    shape: str
    duration: int
    duration_hm: str
    comments: str
    date_posted: datetime
    latitude: float
    longitude: float

//ORDINARE LISTA DI TUPLE
ordinaLista=sorted(lista,key=lambda x:x[2], reverse=False)

//ORDINARE DIZIONARIO per valore
dizioOrdinato= dict(sorted(dizio.items(), key=lambda item: item[1], reverse=True))

//TAGLIARE LA LISTA
listaOrdinata=listaOrdinata[:3]   -> questo codice mi permette di prendere i primi tre


//CALCOLO DISTANZA CON IMPORTAZIONE DI import geopy.distance

posizione1 = (nodo1.lat, nodo1.lng)
posizione2 = (nodo2.lat, nodo2.lng)
distanzaCalcolata= geopy.distance.distance(posizione1, posizione2).km

//arrotondare a tot cifre
rount(numero, numeroCifre)

//splittare
direttoreid=direttoreStringa.split("-")[0]

//FAR ACCADERE QUALCOSA ALLA SELEZIONE DI UN DD
self.dd_anno=ft.Dropdown(label="Anno", on_change=self._controller.getSquadre)
