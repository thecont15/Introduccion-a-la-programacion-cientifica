class Solution(object):
    def lemonadeChange(self, bills):
        Cincos = 0
        Diez = 0

        for bill in bills:
            if bill == 5:
                Cincos += 1
            elif bill == 10:
                if Cincos > 0:
                    Cincos -= 1
                    Diez += 1
                else:
                    return False
            else:  # bill == 20
                if Diez > 0 and Cincos > 0:
                    Diez -= 1
                    Cincos -= 1
                elif Cincos >= 3:
                    Cincos -= 3
                else:
                    return False

        return True
