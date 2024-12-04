## File to store the function for the right endpoint method.
##Returns the error, riemann sum value and time taken.
function [error, Ire, Tre] = RightEnd(del_x, n)
 ##Starts the timer.
 tic();
 sum = 0;
 for i=1:n
   ##Stores the sum.
  sum = sum + del_x*sin(i*del_x);
 endfor
 Ire = sum;
 ##Stores the error.
 error = abs(1 - sum);
 ##Stores the time taken.
 Tre = toc();
endfunction

