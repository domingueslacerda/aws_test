import psycopg2

def getFileLine(dbConn, fileLineId):
    curs = dbConn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    curs.execute("SELECT * FROM file_lines WHERE id = %s", (fileLineId,))
    res = curs.fetchone()
    curs.close()
    return res