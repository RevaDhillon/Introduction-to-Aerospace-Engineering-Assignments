## File to store the function for linear regression.
##Returns the values of y for the best fit line.
function y = Linear_Regression(del_x, error)
  ##Row vectors.
  v1 = del_x;
  v2 = error;
  ##Adding a column of all ones.
  mv1 = [v1', [ones(length(v1),1)]];
  ##Finding [m; c].
  X = inv((mv1')*mv1)*(mv1')*v2';
  ##Storing the values of y on the line.
  y = mv1*(X);
 endfunction

