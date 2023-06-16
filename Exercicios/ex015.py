# Aluguel de carros
km_rodado = float(input("Quantos Km rodados: "))
dias_aluguel = int(input("Quatos dias alugados: "))
total_km = km_rodado * 0.15
total_dias_alugado = dias_aluguel * 60
total_a_pagar = total_km + total_dias_alugado
print(
    f"""De acordo com as normas da empresa você pagara R$ {total_km:.2f} pelos quilometros rodados e R$ {total_dias_alugado:.2f} pelos dias alugados, isso da um total de R$ {total_a_pagar:.2f} .""")
