#!/usr/bin/R --vanilla

setwd("~/Documentos/coding/projetos/rscripts/bib-packrat")
packrat::on("~/Documentos/coding/projetos/rscripts/bib-packrat")
#set.seed(165)
#runif(10)

n <- 10000
f <- function(x) x^2
plot(runif(n), runif(n), col='blue', pch=20)
curve(f, 0, 1, n=100, col='white', add=TRUE)


ps <- matrix(runif(2*n), ncol=2)
g <- function(x,y) y <= x^2
z <- g(ps[,1], ps[,2])
#plot(ps[z, 1], ps[z, 2], col='blue', pch=20)
plot(ps[!z, 1], ps[!z, 2], col='blue', pch=20)
points(ps[z, 1], ps[z, 2], col="green", pch=20)
#points(ps[!z, 1], ps[!z, 2], col="green", pch=20)
curve(f, 0,1, n=100, col='red', add=TRUE)

## Aproximação de erro

# Gera uma sequência entre 1 e 7, pulando casas decimais de 2 em 2
ks <- seq(1, 7, by=.2)

g <- function(k) {
    n <- 10^k #eleva 10 a K, parametro da funcao
    f <- function(x, y) y <= x^2
    z <- f(runif(n), runif(n))
    length(z[z]) / n
}

a <- sapply(ks, g)



# Dardos

n <- 1000000

for i in seq(n) {
    x = runif()
}i




#Baseado em geometria: A probabilidade de jogar dentro do círculo é proporcional à área do círculo. Se dividirmos a área do círculo pela área do quadrado, temos nossa resposta. r=1, l=2, (pi*r^2)/(l^2) | pi/4


#n= numero de pontos, dardos jogados
n = 1000000 #quanto mais amostras, mais próximo da realidade
circ = 0
#circ= acumulador, chamado de "running total" ou soma parcial. Vai acumular todas as vezes que o dardo estiver de fato dentro do círculo, somando um toda vez que isso for verdade. Dessa forma, no final, temos apenas que fazer a razão entre o número de dardos dentro da circunferência, ou seja, CIRC, sobre o número total de dados jogados, N. C/N = Fração de dados que eu joguei aleatoriamente dentro do alvo, essa é a nossa "área em baixo da curva".

for i in (i...n) {
    x = rand(-1, 1)
    y = rand(-1, 1)


    if ((x^2 + y^2) <= 1) {
        circ += 1
    }
}
