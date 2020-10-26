# 1472. Design Browser History - Medium
# Tags - Design

class BrowserHistory:

    def __init__(self, homepage: str):
        self.pos = 0
        self.length = 0
        self.arr = [homepage]

    def visit(self, url: str) -> None:
        self.pos += 1
        if self.pos == len(self.arr):
            self.arr.append(url)
        else:
            self.arr[self.pos] = url
        self.length = self.pos

    def back(self, steps: int) -> str:
        self.pos = max(0, self.pos - steps)
        return self.arr[self.pos]

    def forward(self, steps: int) -> str:
        self.pos = min(self.length, self.pos + steps)
        return self.arr[self.pos]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)