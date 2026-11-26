"""860. Lemonade Change: cambio exacto conservando los billetes pequeños."""

from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billetes_cinco = 0
        billetes_diez = 0

        for billete in bills:
            if billete == 5:
                billetes_cinco += 1
            elif billete == 10:
                if billetes_cinco == 0:
                    return False
                billetes_cinco -= 1
                billetes_diez += 1
            elif billete == 20:
                # Un billete de cinco también permite atender pagos de diez.
                if billetes_diez > 0 and billetes_cinco > 0:
                    billetes_diez -= 1
                    billetes_cinco -= 1
                elif billetes_cinco >= 3:
                    billetes_cinco -= 3
                else:
                    return False
            else:
                raise ValueError("Las denominaciones permitidas son 5, 10 y 20.")

        return True
