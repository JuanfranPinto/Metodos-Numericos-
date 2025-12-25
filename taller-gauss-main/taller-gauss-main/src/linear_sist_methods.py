# -*- coding: utf-8 -*-
"""
Python 3
05 / 07 / 2024
@author: z_tjona

"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
"""

# ----------------------------- logging --------------------------
import logging
from sys import stdout
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s] %(message)s",
    stream=stdout,
    datefmt="%m-%d %H:%M:%S",
)
logging.info(datetime.now())

import numpy as np

# creamos el contador de operaciones
from dataclasses import dataclass


@dataclass
class OpCount:
    swaps: int = 0
    addsub: int = 0
    muldiv: int = 0
    
# ####################################################################
def eliminacion_gaussiana(
    A: np.ndarray | list[list[float | int]],
    *,
    return_counts: bool = False,
    tol: float = 1e-12,
) -> np.ndarray | tuple[np.ndarray, OpCount]:
    """Resuelve un sistema de ecuaciones lineales mediante el método de eliminación gaussiana.

    ## Parameters

    ``A``: matriz aumentada del sistema de ecuaciones lineales. Debe ser de tamaño n-by-(n+1), donde n es el número de incógnitas.

    ## Return

    ``solucion``: vector con la solución del sistema de ecuaciones lineales.

    """
    counts = OpCount()

    if not isinstance(A, np.ndarray):
        logging.debug("convirtiendo A a numpy array.")
        A = np.array(A, dtype=float)  # (ajuste) usar float
    else:
        A = A.astype(float, copy=True)

    assert A.shape[0] == A.shape[1] - 1, "la matriz A debe ser de tamaño n-by-(n+1)."
    n = A.shape[0]

    for i in range(0, n - 1):  # loop por columna

        # --- encontrar pivote
        p = None  # default, first element
        for pi in range(i, n):
            if abs(A[pi, i]) < tol:
                # must be nonzero
                continue

            if p is None:
                # first nonzero element
                p = pi
                continue

            # (BUG FIX) pivoteo parcial correcto: escoger MAYOR |a|
            if abs(A[pi, i]) > abs(A[p, i]):
                p = pi

        if p is None:
            # no pivot found.
            raise ValueError("No existe solución única.")

        if p != i:
            # swap rows
            logging.debug(f"Intercambiando filas {i} y {p}")
            _aux = A[i, :].copy()
            A[i, :] = A[p, :].copy()
            A[p, :] = _aux
            counts.swaps += 1

        # --- Eliminacion: loop por fila
        for j in range(i + 1, n):
            if abs(A[j, i]) < tol:
                continue

            # m = A[j, i] / A[i, i]
            counts.muldiv += 1  # 1 division
            m = A[j, i] / A[i, i]

            for k in range(i, n + 1):
                counts.muldiv += 1  # 1 multiplicacion
                counts.addsub += 1  # 1 resta
                A[j, k] = A[j, k] - m * A[i, k]

        logging.info(f"\n{A}")

    if abs(A[n - 1, n - 1]) < tol:
        print(f"\n{A}")
        raise ValueError("No existe solución única.")

    # --- Sustitución hacia atrás
    solucion = np.zeros(n, dtype=float)

    counts.muldiv += 1  # 1 división
    solucion[n - 1] = A[n - 1, n] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            counts.muldiv += 1  # mult
            counts.addsub += 1  # suma
            suma += A[i, j] * solucion[j]
        counts.addsub += 1  # resta
        counts.muldiv += 1  # división
        solucion[i] = (A[i, n] - suma) / A[i, i]

    if return_counts:
        return solucion, counts
    return solucion


# ####################################################################
def gauss_jordan(
    A: np.ndarray | list[list[float | int]],
    *,
    return_counts: bool = False,
    tol: float = 1e-12,
) -> np.ndarray | tuple[np.ndarray, OpCount]:
    """
    solucion para sistema de ecuaciones con gauss-Jordan.
    La entrada A debe ser matriz aumentada n-by-(n+1).
    """
    counts = OpCount()

    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A, dtype=float)
    else:
        A = A.astype(float, copy=True)

    assert A.shape[0] == A.shape[1] - 1, "La matriz A debe ser de tamaño n-by-(n+1)."
    n = A.shape[0]

    for i in range(0, n):  # loop por columna

        # --- encontrar pivote (pivoteo parcial)
        p = None
        for pi in range(i, n):
            if abs(A[pi, i]) < tol:
                continue
            if p is None:
                p = pi
                continue
            if abs(A[pi, i]) > abs(A[p, i]):
                p = pi

        if p is None:
            raise ValueError("No existe solución única.")

        if p != i:
            logging.debug(f"Intercambiando filas {i} y {p}")
            _aux = A[i, :].copy()
            A[i, :] = A[p, :].copy()
            A[p, :] = _aux
            counts.swaps += 1

        # --- Normalizar fila pivote (hacer pivote = 1)
        piv = A[i, i]
        if abs(piv) < tol:
            raise ValueError("No existe solución única.")

        for k in range(i, n + 1):
            counts.muldiv += 1  # división
            A[i, k] = A[i, k] / piv

        # --- Eliminar en todas las otras filas
        for j in range(0, n):
            if j == i:
                continue
            factor = A[j, i]
            if abs(factor) < tol:
                continue
            for k in range(i, n + 1):
                counts.muldiv += 1  # mult
                counts.addsub += 1  # resta
                A[j, k] = A[j, k] - factor * A[i, k]

        logging.info(f"\n{A}")

    solucion = A[:, -1].copy()
    if return_counts:
        return solucion, counts
    return solucion


# ####################################################################
def descomposicion_LU(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Realiza la descomposición LU de una matriz cuadrada A.
    [IMPORTANTE] No se realiza pivoteo.

    ## Parameters

    ``A``: matriz cuadrada de tamaño n-by-n.

    ## Return

    ``L``: matriz triangular inferior.

    ``U``: matriz triangular superior. Se obtiene de la matriz ``A`` después de aplicar la eliminación gaussiana.
    """

    A = np.array(
        A, dtype=float
    )  # convertir en float, porque si no, puede convertir como entero

    assert A.shape[0] == A.shape[1], "La matriz A debe ser cuadrada."
    n = A.shape[0]

    L = np.zeros((n, n), dtype=float)

    for i in range(0, n):  # loop por columna

        # --- deterimnar pivote
        if A[i, i] == 0:
            raise ValueError("No existe solución única.")

        # --- Eliminación: loop por fila
        L[i, i] = 1
        for j in range(i + 1, n):
            m = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - m * A[i, i:]

            L[j, i] = m

        logging.info(f"\n{A}")

    if A[n - 1, n - 1] == 0:
        raise ValueError("No existe solución única.")

    return L, A


# ####################################################################
def resolver_LU(L: np.ndarray, U: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Resuelve un sistema de ecuaciones lineales mediante la descomposición LU.

    ## Parameters

    ``L``: matriz triangular inferior.

    ``U``: matriz triangular superior.

    ``b``: vector de términos independientes.

    ## Return

    ``solucion``: vector con la solución del sistema de ecuaciones lineales.

    """

    n = L.shape[0]

    # --- Sustitución hacia adelante
    logging.info("Sustitución hacia adelante")

    y = np.zeros((n, 1), dtype=float)

    y[0] = b[0] / L[0, 0]

    for i in range(1, n):
        suma = 0
        for j in range(i):
            suma += L[i, j] * y[j]
        y[i] = (b[i] - suma) / L[i, i]

    logging.info(f"y = \n{y}")

    # --- Sustitución hacia atrás
    logging.info("Sustitución hacia atrás")
    sol = np.zeros((n, 1), dtype=float)

    sol[-1] = y[-1] / U[-1, -1]

    for i in range(n - 2, -1, -1):
        logging.info(f"i = {i}")
        suma = 0
        for j in range(i + 1, n):
            suma += U[i, j] * sol[j]
        logging.info(f"suma = {suma}")
        logging.info(f"U[i, i] = {U[i, i]}")
        logging.info(f"y[i] = {y[i]}")
        sol[i] = (y[i] - suma) / U[i, i]

    logging.debug(f"x = \n{sol}")
    return sol


# ####################################################################
def matriz_aumentada(A: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Construye la matriz aumentada de un sistema de ecuaciones lineales.

    ## Parameters

    ``A``: matriz de coeficientes.

    ``b``: vector de términos independientes.

    ## Return

    ``Ab``: matriz aumentada.

    """
    if not isinstance(A, np.ndarray):
        logging.debug("Convirtiendo A a numpy array.")
        A = np.array(A, dtype=float)
    if not isinstance(b, np.ndarray):
        b = np.array(b, dtype=float)
    assert A.shape[0] == b.shape[0], "Las dimensiones de A y b no coinciden."
    return np.hstack((A, b.reshape(-1, 1)))


# ####################################################################
def separar_m_aumentada(Ab: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Separa la matriz aumentada en la matriz de coeficientes y el vector de términos independientes.

    ## Parameters
    ``Ab``: matriz aumentada.

    ## Return
    ``A``: matriz de coeficientes.
    ``b``: vector de términos independientes.
    """
    logging.debug(f"Ab = \n{Ab}")
    if not isinstance(Ab, np.ndarray):
        logging.debug("Convirtiendo Ab a numpy array")
        Ab = np.array(Ab, dtype=float)
    return Ab[:, :-1], Ab[:, -1].reshape(-1, 1)
