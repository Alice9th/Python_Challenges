def __init__(self, m, n):
             self.m = m
             self.n = n
             self.mat = [] * (m + 1)
                for i in range(m + 1):
                    a = [0] * (n + 1)
                    self.mat.append(a)