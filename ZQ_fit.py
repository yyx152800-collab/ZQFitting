#课程作业
#Z-Q关系拟合
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

#设置字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

# 数据提取
df = pd.read_excel("/Users/xieyuxin/PycharmProjects/PythonProject2/Q.xlsx")
Z = df["Z"].values
Q = df["Q"].values

#Z-Q关系解析式以指数关系拟合，Z0，C，n是待拟合参数
def func(Z, Z0, C, n):
    return C * (Z - Z0) ** n

#初始值假设
p0 = [0.5, 10, 2.0]

#参数范围限制
bound = ([-np.inf, 0, 0], [np.min(Z) - 0.001, np.inf, np.inf])

#数据拟合
params, cov = curve_fit(func, Z, Q, bounds=bound, p0=p0, maxfev=20000)
Z0, C, n = params
Q_test = func(Z, Z0, C, n)
r2 = r2_score(Q, Q_test)

#公式展示
print(f"\n公式：Q = {C:.3f} × (Z - {Z0:.3f})^{n:.3f}")

#绘图
plt.figure(figsize=(10,5))
plt.scatter(Q, Z, c='r', label='实测数据')
Z_line = np.linspace(min(Z), max(Z), 200)
Q_line = C * (Z_line - Z0) ** n
plt.plot(Q_line, Z_line, 'b-', linewidth=2, label='拟合曲线')
plt.xlabel('Q (m³/s)')
plt.ylabel('Z (m)')
plt.title('Z- Q关系曲线')
plt.legend()
plt.grid(True)
plt.show()
