# DAO Copia incolla per velocizzare
class DAO():
    def __init__(self):
        pass

    @staticmethod
    def nome1():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""
        cursor.execute(query)
        for row in cursor:
            result.append()
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def nome2():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""
        cursor.execute(query, ())
        for row in cursor:
            result.append(
                )
            #Prodotto(**row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def nome3():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""

        cursor.execute(query,)

        for row in cursor:
            result.append()

        cursor.close()
        conn.close()
        return result
