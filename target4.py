sp = 67836.42
rj = 36678.66
mg = 29229.88
es = 27165.48
another = 19849.53
total = sp + rj + mg + es + another

print(f"""
São Paulo contribuiu com: {((sp/total) * 100):.2f}%
Rio de Janeiro contribuiu com: {((rj/total) * 100):.2f}%
Minas Gerais contribuiu com: {((mg/total) * 100):.2f}%
Espirito Santo contribuiu com: {((es/total) * 100):.2f}%
E outros estados contribuiram com: {((another/total) * 100):.2f}%
""")
