#Looped code for monte carlo dart simulation

throws = 100 #1000000
landed = 0 #landed in circle

for (i in seq(1,throws)){
    x = runif(1, min=-1, max=1)
    y = runif(1, min=-1, max=1)

    if ((x^2)+(y^2) <= 1) {
        landed = landed + 1
    }
}

print(4 * (landed/throws))

for (i in seq(1, throws)) {
        plot(x[1:i], y[1:i], xlim=c(-1,1), ylim=c(-1,1))
    points(x[i], y[i], col="red")
        Sys.sleep(0.5)
}



