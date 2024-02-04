import pulp as plp

prob = plp.LpProblem(name="Drink Company", sense=plp.LpMaximize)

x1 = plp.LpVariable(name="Lemonade", lowBound=0, cat="Integer")
x2 = plp.LpVariable(name="Fruit juice", lowBound=0, cat="Integer")

prob += x1 + x2, "Total_production"

prob += 2 * x1 + x2 <= 100, "water"
prob += x1 <= 50, "sugar"
prob += x1 <= 30, "lemon juice"
prob += 2 * x2 <= 40, "fruit puree"

prob.solve()

print("Status:", plp.LpStatus[prob.status])
print("Total Production (Lemonade):", int(x1.varValue))
print("Total Production (Fruit Juice):", int(x2.varValue))
