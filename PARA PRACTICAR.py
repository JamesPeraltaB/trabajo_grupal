d = [
     ["stench               ", "sturdy"],
     ["drizzle              ", "damp"],
     ["speed-boost          ", "limber"],
     ["battle-armor         ", "sand-veil"],
     ["static               ", "volt-absorb"],
     ["water-absorb         ", "oblivious"],
     ["intimidate           ", "trace"]      
]
     
print ("{:<8} {:<30}".format('Habilidades','de Pokemon a Elegir'))

for v in d:
    col1, col2 = v
    print ("{:<8} {:<30}".format( col1, col2))