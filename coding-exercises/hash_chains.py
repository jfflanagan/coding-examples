# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        for i in range(bucket_count):
            self.elems.append([])

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(reversed(self.elems[query.ind]))
        else:
            hash_value = self._hash_func(query.s)
            if query.type == 'find':
                found = False
                if self.elems[hash_value]:
                    for elem in self.elems[hash_value]:
                        if elem == query.s:
                            found = True
                            break           
                self.write_search_result(found)
            elif query.type == 'add':
                in_list = False
                if self.elems[hash_value]:
                    for elem in self.elems[hash_value]:
                        if elem == query.s:
                            in_list = True
                            break
                if not in_list:
                    self.elems[hash_value].append(query.s)
            else:       
                if self.elems[hash_value]:
                    new_chain = []
                    for elem in self.elems[hash_value]:
                        if elem != query.s:
                            new_chain.append(elem)
                    self.elems[hash_value] = new_chain

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
