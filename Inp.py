from multiprocessing import Process,Pipe

msg = 1
def f(child_conn):
    child_conn.send(msg)
