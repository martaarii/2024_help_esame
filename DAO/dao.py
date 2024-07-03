from database.DB_connect import DBConnect
from model.state import Stato

class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllYear():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct year(`datetime`) as anni
                    from sighting s """
        cursor.execute(query)
        for row in cursor:
            result.append(row["anni"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllShape():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct shape
                    from sighting s """
        cursor.execute(query, ())
        for row in cursor:
            result.append(row["shape"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    from state s """

        cursor.execute(query,)

        for row in cursor:
            result.append(Stato(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getVicini():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select id, Neighbors 
                    from state s """

        cursor.execute(query, )

        for row in cursor:
            result.append((row["id"], row["Neighbors"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAvvistamenti(forma, anno):
        """ somma avvistamenti per ogni stato"""
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select s.state, count(*) as avvistamenti
                       from sighting s 
                       where year(s.`datetime`) = %s
                       and s.shape= %s
                       group by s.state """

        cursor.execute(query, (anno, forma))
        for row in cursor:
            result.append((row["state"], row["avvistamenti"]))

        cursor.close()
        conn.close()
        return result


