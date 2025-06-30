# surpresa.py (versão com botão de desligar)
import http.server
import socketserver
import webbrowser
import os
import threading

# Define a porta do servidor.
PORTA = 8000

# Esta será nossa classe de manipulador personalizada
class MeuManipulador(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Se a URL acessada for '/desligar', iniciamos o processo de desligamento
        if self.path == '/desligar':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>Servidor desligado. Voce ja pode fechar esta aba.</h1>")
            
            # Função que efetivamente desliga o servidor (precisa ser em outra thread)
            def desligar_servidor():
                httpd.shutdown()
                httpd.server_close()
            
            print("Recebido comando para desligar o servidor...")
            # Inicia o desligamento para não bloquear a resposta atual
            threading.Thread(target=desligar_servidor).start()
        else:
            # Para qualquer outra URL, comporta-se como um servidor de arquivos simples
            super().do_GET()

# Garante que o servidor encontre o arquivo index.html na mesma pasta do script.
diretorio_script = os.path.dirname(__file__)
if diretorio_script:
    os.chdir(diretorio_script)

# Cria e configura o servidor com o nosso manipulador personalizado
with socketserver.TCPServer(("", PORTA), MeuManipulador) as httpd:
    print(f"Servidor rodando em http://localhost:{PORTA}")
    
    url = f"http://localhost:{PORTA}/index.html"
    webbrowser.open(url)
    
    print("Para parar o servidor, pressione Ctrl+C no terminal ou clique no link 'Fechar Surpresa' na pagina.")
    
    # Mantém o servidor ativo.
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor interrompido pelo usuario.")
    
    print("Servidor finalizado.")