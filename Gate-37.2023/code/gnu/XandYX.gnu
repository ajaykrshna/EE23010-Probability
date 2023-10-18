set terminal pngcairo enhanced color size 600,400
set output '../../figs/XandYX.png'
plot '../data/x_data.txt' using 1:2 with lines title 'CDF(X)'