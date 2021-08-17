#Vectorized code for monte carlo dart simulation


throws = 100 #1000000
landed = 0 #landed in circle

#throws=100
x = runif(n=throws, min=-1, max=1)
y = runif(n=throws, min=-1, max=1)
soma_quadrados <- (x^2) + (y^2)
dardos_indexados <- which(soma_quadrados <= 1)
no_alvo <- length(dardos_indexados)

print(4 * (no_alvo/throws))

