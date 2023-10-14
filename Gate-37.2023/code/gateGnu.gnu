set terminal pngcairo enhanced color size 600,400
set output 'cdf_plot.png'
plot 'cdf_data.txt' using 1:2 with lines title 'CDF(Y)'