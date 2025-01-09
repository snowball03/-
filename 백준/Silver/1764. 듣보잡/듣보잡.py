n, m = map(int, input().split())
listen = set(input().strip() for _ in range(n)) 
see = set(input().strip() for _ in range(m)) 

result = sorted(listen & see)

print(len(result)) 
print("\n".join(result)) 

