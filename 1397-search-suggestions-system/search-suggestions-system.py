
class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        products.sort()
        result = []
        for i in range(len(searchWord)):
            res = []
            for p in products:
                if p.startswith(searchWord[:i + 1]):
                    if len(res) < 3:
                        res.append(p)
                    else:
                        break
            result.append(res)
        return result
