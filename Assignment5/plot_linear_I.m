## File to plot riemann sum values using linear axis.
function plot_linear_I(del_x, I, Title, Ylabel)
  ##Making the plot.
  plot(del_x,I, ".-r")
  grid on
  ##Titling the figure.
  title(Title)
  ##Labelling the axes.
  xlabel("∆x -->")
  ylabel(Ylabel)
  set(gca, "fontsize", 10)
endfunction
