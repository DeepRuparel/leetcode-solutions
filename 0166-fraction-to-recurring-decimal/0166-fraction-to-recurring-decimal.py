class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = ""
        if numerator*denominator < 0:
            sign = "-"
        
        q, remainder = divmod(abs(numerator), abs(denominator))
        
        if remainder == 0:
            return sign+str(q)
        l = [sign+str(q)+"."]
        seen = {}
        
        while remainder > 0 and remainder not in seen:
            seen[remainder] = len(l)
            quotient, remainder = divmod(remainder * 10, abs(denominator))
            l.append(str(quotient))
        if remainder in seen:
            j = seen[remainder]
            l.insert(j, "(")
            l.append(")")
        return "".join(l)
        