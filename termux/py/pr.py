for i in range(1, 10):
    row = []
    for j in range(1, i + 1):
        row.append(f"{j} × {i} = {i * j:2}")
    print("    ".join(row))
