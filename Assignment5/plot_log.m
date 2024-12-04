## File to plot error values using log-log scale.
function plot_log(del_x, error, Title, Ylabel)
  ##Finding best fit line.
  y = Linear_Regression(del_x , error);
  ##Making all values positive.
  if (y(100)<=0)
    for i=1:100
      error(i) = error(i) - y(100) + 10^(-6);
      y(i) = y(i) - y(100) + 10^(-6);
    endfor
  endif
  ##Making the plots.
  loglog(del_x, error, ".b");
  loglog(del_x,y, "m")
  ##Making the legend.
  legend({"Scatter plot", "Linear Regression"}, "location", "southeast")
  grid on
  ##Titling the figure.
  title(Title)
  ##Labelling the axes.
  xlabel("∆x -->")
  ylabel(Ylabel)
  set(gca, "fontsize", 10)
endfunction
