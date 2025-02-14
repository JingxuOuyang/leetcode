
class ProductOfNumbers:

    def __init__(self):
        self.products = []        

    def add(self, num: int) -> None:
        if num == 0:
            self.products.clear()
            return
        if len(self.products) == 0:
            self.products.append(num)
        else:
            self.products.append(num * self.products[-1])

    def getProduct(self, k: int) -> int:
        if len(self.products) < k:
            return 0
        if len(self.products) == k:
            return self.products[-1]
        return self.products[-1] // self.products[-k-1]
    
if __name__ == '__main__':
    s = ProductOfNumbers()