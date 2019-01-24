
# coding: utf-8

# # プログラム

# In[1]:


class Newton(object):
    def __init__(self, f, d1f,B):
        self.f = f
        self.d1f = d1f
        self.B = B
    def _update(self, bar_x):
        f = self.f
        d1f = self.d1f
        B = self.B
        return bar_x - d1f(bar_x)*B
   
    def solve(self,init_x, n_iter, tol):
        bar_x = init_x
        for i in range(n_iter):
            x = self._update(bar_x)
            error = abs(x - bar_x)
            print("|Δx| = {0:.4f}, x = {1:.4f}".format(error, x))
            print("y = {0:.4f}".format(self.f(x)))
            bar_x = x
            if error < tol:
                break
        return x


# In[2]:


f = lambda x: x**2 - 2*x
d1f = lambda x: 2*x - 2

newton = Newton(f=f, d1f=d1f, B=0.1)
res = newton.solve(init_x=10, n_iter=100, tol=0.01)
print("x = {0:.1f}, y= {1:.1f}".format(res,f(res)))

