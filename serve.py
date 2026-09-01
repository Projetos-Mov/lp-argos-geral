"""Servidor local de preview.

ThreadingHTTPServer, nao TCPServer: com um unico thread, uma conexao
keep-alive presa pelo navegador bloqueia todas as outras requisicoes —
foi o que fez os assets pararem de carregar.
"""
import http.server, os, socketserver

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        super().log_message(fmt, *args)

class Servidor(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

with Servidor(("127.0.0.1", 4329), Handler) as h:
    print("serving", os.getcwd(), "on 4329", flush=True)
    h.serve_forever()
