from multiprocessing import Process,Queue,Pipe
from Inp import f

parent_conn, child_conn = Pipe()
f(child_conn)
print(parent_conn.recv())