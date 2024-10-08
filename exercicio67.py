times = []
tabela = []

for i in range(4):
    time = input(f"Digite o nome do {i + 1}º time: ")
    times.append(time)
    tabela.append([0, 0, 0, 0, 0, 0, 0])

for i in range(len(times)):
    print(f"\n----- Partidas do {times[i]} -----")
    for j in range(len(times)):
        if i != j:
            print(f"\n{times[i]} x {times[j]}")
            gols_time_i = int(input(f"Gols do {times[i]}: "))
            gols_time_j = int(input(f"Gols do {times[j]}: "))
            if gols_time_i > gols_time_j:
                tabela[i][1] += 1  
                tabela[j][3] += 1  
                tabela[i][0] += 3  
            elif gols_time_i < gols_time_j:
                tabela[j][1] += 1  
                tabela[i][3] += 1  
                tabela[j][0] += 3  
            else:
                tabela[i][2] += 1  
                tabela[j][2] += 1  
                tabela[i][0] += 1  
                tabela[j][0] += 1  
            tabela[i][4] += gols_time_i  
            tabela[i][5] += gols_time_j  
            tabela[j][4] += gols_time_j  
            tabela[j][5] += gols_time_i  

print("\n----- Tabela do Campeonato -----")
print("Time | P | V | E | D | GP | GC | SG")
for i in range(len(times)):
    tabela[i][6] = tabela[i][4] - tabela[i][5]  
    print(f"{times[i]} | {tabela[i][0]} | {tabela[i][1]} | {tabela[i][2]} | {tabela[i][3]} | {tabela[i][4]} | {tabela[i][5]} | {tabela[i][6]}")