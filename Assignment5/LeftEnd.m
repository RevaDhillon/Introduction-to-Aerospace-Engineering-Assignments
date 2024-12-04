## File to store the function for the left endpoint method.
##Returns the error, riemann sum value and time taken.
function [error, Ile, Tle]= LeftEnd(del_x, n)
 ##Starts the timer.
 tic();
 sum = 0;
 for i=0:(n-1)
   ##Stores the sum.
  sum = sum + del_x*sin(i*del_x);
 endfor
 Ile = sum;
 ##Stores the error.
 error = abs(1 - sum);
 ##Stores the time taken.
 Tle = toc();
endfunction

