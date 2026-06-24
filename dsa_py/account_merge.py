class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v

        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u

        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v

            self.size[ulp_v] += self.size[ulp_u]
            
        else:
            self.parent[ulp_v] = ulp_u

            self.size[ulp_u] += self.size[ulp_v]

class solution:
    def accountsMerge(self, details):
        n = len(details)

        ds = DisjointSet(n)
        mapMailNode = {}

        for i in range(n):
            for j in range(1, len(details[i])):
                mail = details[i][j]
                if mail not in mapMailNode:
                    mapMailNode[mail] = i

                else:
                    ds.unionByRank(i, mapMailNode[mail])

        mergeMail = [[] for _ in range(n)]
        for mail, idx in mapMailNode.items():
            node = ds.findUPar(idx)

            mergeMail[node].append(mail)

            ans = [] 

            for i in range(n):
                if not mergeMail[i]:
                    continue

                mergeMail[i].sort()
                temp = [details[i][0]]

                for mail in mergeMail[i]:
                    temp.append(mail)

                ans.append(temp)

                ans.sort()
                return ans
            
    def main():
        accounts = [
            ["john", "j1@com", "j2@com", "j3@com"],
                         
   ]
        obj = solution()
        ans = obj.accountsMerge(accounts)
        for acc in ans:
            print(acc[0] + ":", end="")
            for mail in acc[1:]:
                print(mail, end=" ")
            
            print()

