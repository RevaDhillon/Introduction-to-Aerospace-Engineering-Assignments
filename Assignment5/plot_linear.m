## File to plot error values using linear axis.
function plot_linear(del_x, error, Title, Ylabel)
  ##Making a scatter plot.
  scatter(del_x, error, 12, "filled")
  ##Finding best fit line.
  y = Linear_Regression(del_x , error);
  ##Making a plot.
  plot(del_x,y, "m")
  ##Making the legend.,
  legend({"Scatter plot", "Linear Regression"}, "location", "northwest")
  grid on
  ##Titling the figure.
  title(Title)
  ##Labelling the axes.
  xlabel("∆x -->")
  ylabel(Ylabel)
  set(gca, "fontsize", 10)
endfunction

