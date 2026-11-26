"""455. Assign Cookies: asignación greedy sin modificar las entradas."""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        demandas = sorted(g)
        galletas = sorted(s)
        satisfechos = 0

        for tamano in galletas:
            if satisfechos == len(demandas):
                break

            # La menor galleta suficiente conserva las grandes para otras demandas.
            if tamano >= demandas[satisfechos]:
                satisfechos += 1

        return satisfechos
