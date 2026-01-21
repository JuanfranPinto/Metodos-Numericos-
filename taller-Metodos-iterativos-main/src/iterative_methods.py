# -*- coding: utf-8 -*-

"""
Python 3
19 / 07 / 2024
@author: z_tjona

"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
"""

# ----------------------------- logging --------------------------
import logging
import os
from sys import stdout
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format=f"[%(asctime)s][%(levelname)s][{os.environ.get('USERNAME')}] %(message)s",
    stream=stdout,
    datefmt="%m-%d %H:%M:%S",
)
logging.info(datetime.now())

import numpy as np


# ####################################################################
def gauss_jacobi(
    *, A: np.ndarray, b: np.ndarray, x: np.ndarray, tol: float, max_iter: int,
    return_traj: bool = False
):
    """Resuelve el sistema de ecuaciones lineales Ax = b mediante el método de Jacobi.

    ## Parameters
    ``A``: Matriz de coeficientes del sistema de ecuaciones lineales.
    ``b``: Vector de términos independientes del sistema de ecuaciones lineales.
    ``x0``: Vector de aproximación inicial.
    ``tol``: Tolerancia.
    ``max_iter``: Número máximo de iteraciones.
    ``return_traj``: Si True, devuelve también la trayectoria de iteraciones.

    ## Return
    Si return_traj=False:
        ``x``: Vector solución (aproximado) del sistema de ecuaciones lineales.
    Si return_traj=True:
        ``x, trayectoria``: donde trayectoria es un array de tamaño (iteraciones+1, n)
    """
    # --- Validación de los argumentos de la función ---
    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A, dtype=float)
    assert A.shape[0] == A.shape[1], "La matriz A debe ser de tamaño n-by-(n)."

    if not isinstance(b, np.ndarray):
        logging.debug("Convirtiendo b a numpy array.")
        b = np.array(b, dtype=float)

    # Acepta b como (n,) o (n,1) y lo normaliza a (n,1)
    b = np.array(b, dtype=float)
    if b.ndim == 1:
        b = b.reshape(-1, 1)
    assert b.shape[0] == A.shape[0], "El vector b debe ser de tamaño n."

    if not isinstance(x, np.ndarray):
        x = np.array(x, dtype=float, ndmin=2).T
    x = np.array(x, dtype=float)
    if x.ndim == 1:
        x = x.reshape(-1, 1)
    assert x.shape[0] == A.shape[0], "El vector x0 debe ser de tamaño n."

    # --- Algoritmo ---
    n = A.shape[0]

    trayectoria = [x.copy()]  # guarda x^(0)

    logging.info(f"i= {0} x: {x.T}")
    for k in range(1, max_iter + 1):
        x_new = np.zeros((n, 1))  # prealloc
        for i in range(n):
            suma = sum([A[i, j] * x[j] for j in range(n) if j != i])
            x_new[i] = (b[i] - suma) / A[i, i]

        trayectoria.append(x_new.copy())  # guarda x^(k)

        if np.linalg.norm(x_new - x) < tol:
            traj = np.hstack(trayectoria).T  # (iter+1, n)
            return (x_new, traj) if return_traj else x_new

        x = x_new.copy()
        logging.info(f"i= {k} x: {x.T}")

    traj = np.hstack(trayectoria).T
    return (x, traj) if return_traj else x


# ####################################################################
def gauss_seidel(
    *, A: np.ndarray, b: np.ndarray, x: np.ndarray, tol: float, max_iter: int,
    return_traj: bool = False
):
    """Resuelve el sistema de ecuaciones lineales Ax = b mediante el método de Gauss-Seidel.

    ## Parameters
    ``A``: Matriz de coeficientes del sistema de ecuaciones lineales.
    ``b``: Vector de términos independientes del sistema de ecuaciones lineales.
    ``x0``: Vector de aproximación inicial.
    ``tol``: Tolerancia.
    ``max_iter``: Número máximo de iteraciones.
    ``return_traj``: Si True, devuelve también la trayectoria de iteraciones.

    ## Return
    Si return_traj=False:
        ``x``: Vector solución (aproximado) del sistema de ecuaciones lineales.
    Si return_traj=True:
        ``x, trayectoria``: donde trayectoria es un array de tamaño (iteraciones+1, n)
    """
    # --- Validación de los argumentos de la función ---
    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A, dtype=float)
    assert A.shape[0] == A.shape[1], "La matriz A debe ser de tamaño n-by-(n)."

    if not isinstance(b, np.ndarray):
        logging.debug("Convirtiendo b a numpy array.")
        b = np.array(b, dtype=float)

    # Acepta b como (n,) o (n,1) y lo normaliza a (n,1)
    b = np.array(b, dtype=float)
    if b.ndim == 1:
        b = b.reshape(-1, 1)
    assert b.shape[0] == A.shape[0], "El vector b debe ser de tamaño n."

    if not isinstance(x, np.ndarray):
        x = np.array(x, dtype=float, ndmin=2).T
    x = np.array(x, dtype=float)
    if x.ndim == 1:
        x = x.reshape(-1, 1)
    assert x.shape[0] == A.shape[0], "El vector x0 debe ser de tamaño n."

    # --- Algoritmo ---
    n = A.shape[0]

    trayectoria = [x.copy()]  # guarda x^(0)

    logging.info(f"i= {0} x: {x.T}")
    for k in range(1, max_iter + 1):
        x_new = np.zeros((n, 1))  # prealloc
        for i in range(n):
            # suma usando valores nuevos para j < i y valores viejos para j >= i
            suma_1 = sum([A[i, j] * x_new[j] for j in range(i)])
            suma_2 = sum([A[i, j] * x[j] for j in range(i + 1, n)])
            x_new[i] = (b[i] - suma_1 - suma_2) / A[i, i]

        trayectoria.append(x_new.copy())  # guarda x^(k)

        if np.linalg.norm(x_new - x) < tol:
            traj = np.hstack(trayectoria).T  # (iter+1, n)
            return (x_new, traj) if return_traj else x_new

        x = x_new.copy()
        logging.info(f"i= {k} x: {x.T}")

    traj = np.hstack(trayectoria).T
    return (x, traj) if return_traj else x

