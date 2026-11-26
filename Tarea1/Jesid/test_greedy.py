"""Contraste de las soluciones con búsquedas exhaustivas independientes."""

from functools import lru_cache
from itertools import product
import unittest

from assign_cookies import Solution as Asignacion
from lemonade_change import Solution as Cambio


def asignacion_exhaustiva(demandas, galletas):
    """Explora todas las asignaciones; solo se usa con entradas pequeñas."""

    @lru_cache(maxsize=None)
    def explorar(nino, usadas):
        if nino == len(demandas):
            return 0
        mejor = explorar(nino + 1, usadas)
        for indice, tamano in enumerate(galletas):
            if not usadas & (1 << indice) and tamano >= demandas[nino]:
                mejor = max(mejor, 1 + explorar(nino + 1, usadas | (1 << indice)))
        return mejor

    return explorar(0, 0)


def cambio_exhaustivo(billetes):
    """Conserva todos los estados factibles, incluidas ambas formas de dar 15."""
    estados = {(0, 0)}
    for billete in billetes:
        siguientes = set()
        for cincos, dieces in estados:
            if billete == 5:
                siguientes.add((cincos + 1, dieces))
            elif billete == 10 and cincos > 0:
                siguientes.add((cincos - 1, dieces + 1))
            elif billete == 20:
                if dieces > 0 and cincos > 0:
                    siguientes.add((cincos - 1, dieces - 1))
                if cincos >= 3:
                    siguientes.add((cincos - 3, dieces))
        estados = siguientes
        if not estados:
            return False
    return True


class TestAssignCookies(unittest.TestCase):
    def test_ejemplos_y_casos_limite(self):
        casos = [
            ([1, 2, 3], [1, 1], 1),
            ([1, 2], [1, 2, 3], 2),
            ([2, 2, 2], [1, 1], 0),
            ([2, 2, 2], [2, 2], 2),
            ([3, 1, 2], [3, 1], 2),
            ([2**31 - 1], [2**31 - 1], 1),
            ([], [1], 0),
            ([1], [], 0),
        ]
        for demandas, galletas, esperado in casos:
            with self.subTest(demandas=demandas, galletas=galletas):
                self.assertEqual(
                    Asignacion().findContentChildren(demandas, galletas), esperado
                )

    def test_no_modifica_las_listas(self):
        demandas = [3, 1, 2]
        galletas = [3, 1]
        originales = demandas.copy(), galletas.copy()
        Asignacion().findContentChildren(demandas, galletas)
        self.assertEqual((demandas, galletas), originales)

    def test_tamano_maximo_del_contrato(self):
        self.assertEqual(
            Asignacion().findContentChildren([1] * 30_000, [1] * 30_000), 30_000
        )

    def test_contraste_exhaustivo(self):
        entradas = [
            valores
            for longitud in range(5)
            for valores in product((1, 2, 3), repeat=longitud)
        ]
        cantidad = 0
        for demandas in entradas:
            for galletas in entradas:
                esperado = asignacion_exhaustiva(demandas, galletas)
                obtenido = Asignacion().findContentChildren(list(demandas), list(galletas))
                self.assertEqual(obtenido, esperado, (demandas, galletas))
                cantidad += 1
        self.assertEqual(cantidad, 14_641)


class TestLemonadeChange(unittest.TestCase):
    def test_ejemplos_y_casos_limite(self):
        casos = [
            ([5, 5, 5, 10, 20], True),
            ([5, 5, 10, 10, 20], False),
            ([10], False),
            ([20], False),
            ([5, 20], False),
            ([5, 5, 5, 20], True),
            ([5, 5, 5, 5, 10, 20, 10], True),
            ([], True),
        ]
        for billetes, esperado in casos:
            with self.subTest(billetes=billetes):
                self.assertEqual(Cambio().lemonadeChange(billetes), esperado)

    def test_no_modifica_la_fila(self):
        billetes = [5, 5, 5, 10, 20]
        original = billetes.copy()
        Cambio().lemonadeChange(billetes)
        self.assertEqual(billetes, original)

    def test_denominacion_fuera_del_contrato(self):
        with self.assertRaises(ValueError):
            Cambio().lemonadeChange([5, 50])

    def test_tamano_maximo_del_contrato(self):
        self.assertTrue(Cambio().lemonadeChange([5] * 100_000))

    def test_contraste_exhaustivo(self):
        cantidad = 0
        for longitud in range(9):
            for billetes in product((5, 10, 20), repeat=longitud):
                self.assertEqual(
                    Cambio().lemonadeChange(list(billetes)),
                    cambio_exhaustivo(billetes),
                    billetes,
                )
                cantidad += 1
        self.assertEqual(cantidad, 9_841)


if __name__ == "__main__":
    unittest.main()
