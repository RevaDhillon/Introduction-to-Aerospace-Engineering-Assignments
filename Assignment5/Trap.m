## File to store the function for the trapezoidal method.
##Returns the error and time taken.
function [error, Ttz] = Trap(del_x, n)
 ##Starts the timer.
 tic();
 sum = 0;
 for i=0:(n-1)
   ##Stores the sum.
  sum = sum + (del_x/2)*(sin(i*del_x) + sin((i+1)*del_x));
 endfor
 ##Stores the error.
 error = abs(1 - sum);
 ##Stores the time taken.
 Ttz = toc();
endfunction

