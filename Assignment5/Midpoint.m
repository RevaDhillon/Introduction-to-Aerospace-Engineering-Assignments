## File to store the function for the midpoint method.
##Returns the error and time taken.
function [error, Tmp] = Midpoint(del_x, n)
 ##Starts the timer.
 tic();
 sum = 0;
 for i=0:(n-1)
   ##Stores the sum.
  sum = sum + del_x*sin(i*del_x + del_x/2);
 endfor
 ##Stores the error.
 error = abs(1 - sum);
 ##Stores the time taken.
 Tmp = toc();
endfunction

