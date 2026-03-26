import os
import socket
import time
import sys

HOST = os.environ.get("DB_HOST", "db")
PORT = int(os.environ.get("DB_PORT", 5432))

print("Esperando a PostgreSQL...")

while True:
  try:
    s = socket.create_connection((HOST, PORT), timeout=2)
    s.close()
    print("PostgreSQL listo!")
    break
  except OSError:
    print("Reintentando conexión...")
    time.sleep(1)

sys.exit(0)