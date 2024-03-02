class Factors:
    def __init__(self):
        self.memoization_table = set()
        self.factor_list = []

    def dfs(self, prime_factors, current_factor):
        if not prime_factors:
            return

        for i, factor in enumerate(prime_factors):
            
            new_factor = current_factor * factor
            if new_factor not in self.memoization_table:
                self.memoization_table.add(new_factor)
                self.factor_list.append(new_factor)

                self.dfs(prime_factors[:i] + prime_factors[i+1:], new_factor)

    def generate_factors(self, prime_factors):
        self.memoization_table = set()
        self.factor_list = [1]

        self.dfs(prime_factors, 1)

        self.factor_list.sort()

        return self.factor_list




obj = Factors()
prime_factors = [2,2,3,5,5]

print(obj.generate_factors(prime_factors))
#prime_factors = [2,2,2,3]
