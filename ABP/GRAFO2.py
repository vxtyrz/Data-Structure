import heapq

class Grafo:
    def __init__(self):
        self.adjacencias = {}

    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.adjacencias:
            self.adjacencias[origem] = []
        if destino not in self.adjacencias:
            self.adjacencias[destino] = []
        self.adjacencias[origem].append((destino, peso))
        self.adjacencias[destino].append((origem, peso))

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo.adjacencias}
    distancias[inicio] = 0
    caminho_anterior = {nodo: None for nodo in grafo.adjacencias}
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        distancia_atual, cidade_atual = heapq.heappop(fila_prioridade)
        if distancia_atual > distancias[cidade_atual]:
            continue
        for vizinho, peso in grafo.adjacencias[cidade_atual]:
            nova_distancia = distancia_atual + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                caminho_anterior[vizinho] = cidade_atual
                heapq.heappush(fila_prioridade, (nova_distancia, vizinho))
    return distancias, caminho_anterior

def reconstruir_caminho(caminho_anterior, inicio, destino):
    caminho = []
    atual = destino
    if destino not in caminho_anterior: 
        return "Caminho nao encontrado"
    while atual is not None:
        caminho.append(atual)
        if atual == inicio:
            break
        atual = caminho_anterior[atual]
    return " -> ".join(reversed(caminho))


if __name__ == "__main__":
    g = Grafo()
    g.adicionar_aresta("Criciuma", "Laguna", 4)
    g.adicionar_aresta("Criciuma", "Formosa", 8)
    g.adicionar_aresta("Laguna", "Palhoca", 8)
    g.adicionar_aresta("Laguna", "Formosa", 11)
    g.adicionar_aresta("Formosa", "Xique-Xique", 7)
    g.adicionar_aresta("Formosa", "Goiania", 1) 
    g.adicionar_aresta("Palhoca", "Xique-Xique", 2)
    g.adicionar_aresta("Palhoca", "Blumenau", 7)
    g.adicionar_aresta("Palhoca", "Aracatuba", 4)
    g.adicionar_aresta("Xique-Xique", "Goiania", 6)
    g.adicionar_aresta("Goiania", "Aracatuba", 2)
    g.adicionar_aresta("Aracatuba", "Blumenau", 14)
    g.adicionar_aresta("Aracatuba", "Curitiba", 10)
    g.adicionar_aresta("Blumenau", "Curitiba", 9)

    origem = "Criciuma"
    menores_distancias, predecessores = dijkstra(g, origem)

    print("-" * 70)
    print(f"RESULTADO DO ALGORITMO DE DIJKSTRA")
    print(f"Origem da Transportadora: {origem.upper()}")
    print("-" * 70)
    print(f"{'DESTINO':<15} | {'CUSTO':<5} | {'ROTA OTIMIZADA'}")
    print("-" * 70)
    cidades_ordenadas = sorted(menores_distancias.keys())

    for cidade in cidades_ordenadas:
        custo = menores_distancias[cidade]
        rota = reconstruir_caminho(predecessores, origem, cidade)
        print(f"{cidade:<15} | {custo:<5} | {rota}")
    print("-" * 70)