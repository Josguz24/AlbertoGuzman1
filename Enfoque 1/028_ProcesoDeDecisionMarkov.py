
# Definición de los estados, acciones, transiciones y recompensas
estados = ['A', 'B', 'C']
acciones = ['Mover', 'Esperar']
transiciones = {
    'A': {'Mover': {'B': 0.8, 'A': 0.2}, 'Esperar': {'A': 1.0}},
    'B': {'Mover': {'C': 0.9, 'B': 0.1}, 'Esperar': {'B': 1.0}},
    'C': {'Esperar': {'C': 1.0}}
}
recompensas = {'A': 0, 'B': 1, 'C': 10}

# Parámetros
gamma = 0.9  # Factor de descuento
iteraciones = 10

# Inicialización de los valores
valores = {estado: 0 for estado in estados}

# Función de iteración de valores para el MDP
def iteracion_valores_mdp():
    for _ in range(iteraciones):
        nuevos_valores = valores.copy()
        for estado in estados:
            valores_accion = []
            for accion in acciones:
                if accion in transiciones[estado]:
                    valor_accion = sum(prob * (recompensas[siguiente] + gamma * valores[siguiente]) 
                                       for siguiente, prob in transiciones[estado][accion].items())
                    valores_accion.append(valor_accion)
            nuevos_valores[estado] = max(valores_accion) if valores_accion else 0
        valores.update(nuevos_valores)
    return valores

# Ejemplo de uso
valores_finales = iteracion_valores_mdp()
print("Valores de los estados en el MDP:", valores_finales)
