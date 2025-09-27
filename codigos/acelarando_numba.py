import random
import time
from numba import jit
import math

# Versão Python puro
def monte_carlo_pi_python(n_samples):
    inside_circle = 0
    
    for _ in range(n_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        # Verifica se o ponto está dentro do círculo (raio = 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    return 4 * inside_circle / n_samples

# Versão acelerada com Numba
@jit(nopython=True)
def monte_carlo_pi_numba(n_samples):
    inside_circle = 0
    
    for i in range(n_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        
        if x**2 + y**2 <= 1:
            inside_circle += 1
    
    return 4 * inside_circle / n_samples

# Teste de desempenho
n_samples = 10_000_000

# Python puro
start_time = time.time()
pi_approx_python = monte_carlo_pi_python(n_samples)
python_time = time.time() - start_time

# Numba (primeira execução inclui compilação)
start_time = time.time()
pi_approx_numba = monte_carlo_pi_numba(n_samples)
numba_time_first = time.time() - start_time

# Numba (execuções subsequentes)
start_time = time.time()
pi_approx_numba = monte_carlo_pi_numba(n_samples)
numba_time_second = time.time() - start_time

print(f"Valor real de π: {math.pi}")
print(f"Aproximação Python: {pi_approx_python}")
print(f"Aproximação Numba: {pi_approx_numba}")
print(f"Erro Python: {abs(math.pi - pi_approx_python)}")
print(f"Erro Numba: {abs(math.pi - pi_approx_numba)}")
print(f"Tempo Python puro: {python_time:.4f} segundos")
print(f"Tempo Numba (primeira execução): {numba_time_first:.4f} segundos")
print(f"Tempo Numba (execuções seguintes): {numba_time_second:.4f} segundos")
print(f"Speedup (execuções seguintes): {python_time/numba_time_second:.2f}x")