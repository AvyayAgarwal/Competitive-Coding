# 811. Subdomain Visit Count - Easy
# Tags - Hash Table

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        map = collections.defaultdict(int)
        for cp in cpdomains:
            ct, dom = cp.split()
            ct = int(ct)
            splits = dom.count(".")
            for i in range(splits + 1):
                map[dom.split(".", i)[i]] += ct
        res = [(str(v) + " " + str(k)) for k,v in map.items()]
        return res