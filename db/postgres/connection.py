import psycopg2

def dbConnect(rdsHost, rdsPort, rdsDbName, rdsDbUser, rdsDbPassword):
    conn = psycopg2.connect(host=rdsHost, port=rdsPort, dbname=rdsDbName, user=rdsDbUser, password=rdsDbPassword)
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_READ_COMMITTED)
    return conn