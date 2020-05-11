import numpy
import matplotlib as mpl
import matplotlib.pyplot as plt
% matplotlib inline

mpl.rc('font', family='Verdana', size= 16)

w = numpy.linalg.solve(M6, v6) # запишем найденные коэффициенты в переменную
def f(x):
    return w[0]*x**2 + w[1]*x + w[2] # уравнение параболы


fig, ax = plt.subplots(figsize=(10,5))

x = numpy.linspace(-2,2,200)
ax.axis([-2., 2., 0., 2.])
ax.grid()
ax.plot(x, f(x), label = 'Парабола')
ax.plot(x, x, label = 'Биссектриса 1й\nкоординатной четверти')
ax.set_xlabel(u'x',{'fontname':'Arial', 'size': 24})
ax.set_ylabel(u'f(x)',{'fontname':'Arial', 'size': 24})
plt.plot([-1, 1], [1, 1], 'ro', label = 'Точки для\nпостроения графика')
ax.annotate('Точка\nкасания', xy=(1., 1.), xytext=(1.5, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

ax.legend(bbox_to_anchor=(1.6, 1.))

plt.show()
