#Self-written QR decomposition
1;

#Function to generate a random matrix A(invertible) and a random vector b.
function [A, b] = MatrixGen(n)
  v = randn(n,1);
  I = eye(n);
  A = I - v*v';
  b = randn(n,1);
 endfunction

 #To store the matrix size values.
 #This is indicated along the the x-axis.
 xaxis = [];
 for i=1:100
   xaxis = [xaxis, i];
 endfor

 #Creating vectors to store L_infinity error and computational times.
 L = [];
 T_QR = [];
 T_x = [];
 T_backslash= [];
 T_QRBuiltin = [];
 T_inv = [];

#QR code run for each matrix size.
for i=1:100
  #Matrices generated.
  [A, b] = MatrixGen(i);
  #Defining vector x to hold the solution.
  x = zeros(i,1);
  #Starting time count.
  tic();
  #Gram - schmidt orthogonalization process.
  u=[A(1:i, 1)];
  for j=2:i
    t=0;
    for k=1:j-1
      t = t + ((u(1:i, k)'*A(1:i, j))/(u(1:i, k)'*u(1:i, k)))*u(1:i, k);
    endfor
    u = [u, A(1:i, j) - t];
  endfor
  #Obtaining unit vectors from the orthogonal vectors u.
  #q stores the unit vectors.
  q = [];
  for j=1:i
    q = [q, u(1:i, j)/sqrt(u(1:i, j)'*u(1:i, j))];
  endfor
  #Finding the upper triangular matrix corresponding to q.
  r=zeros(i);
  for j=1:i
    for k=j:i
      r(j,k) = q(1:i, j)'*A(1:i, k);
    endfor
  endfor
  #Time taken for QR computation stored.
  T_QR = [T_QR, toc()];
  #Starting time count.
  tic();
  #Rearrange the original equation for c = q'b.
  c = q'*b;
  #Loop to compute x.
  for p=1:i
    sum = 0;
    for k = i-p+2:i
      sum = sum + x(k, 1)*r(i+1-p,k);
    endfor
    x(i+1-p, 1) = (c(i+1-p,1)-sum)/r(i+1-p, i+1-p);
  endfor
  #Time taken for x computation stored.
  T_x = [T_x, toc()];

  #Store time taken by A\b operation.
  tic();
  x_Backslash = A\b;
  T_backslash = [T_backslash, toc()];

  #Store time taken by in-built QR code.
  tic();
  [Q, R] = qr(A);
  T_QRBuiltin = [T_QRBuiltin, toc()];

  #Store time taken by inv(A)*b operation.
  tic();
  inv(A)*b;
  T_inv = [T_inv, toc()];

  #Find L_infinity error.
  L = [L, norm((x - x_Backslash), inf)];
endfor

#Compute total time taken by self written QR code.
T_total = T_QR+T_x;
#Convert times to log scales.
T_QRl = log10(T_QR);
T_xl = log10(T_x);
T_totall = log10(T_total);

#Creating figures.
f1=figure(); hold on
f2=figure(); hold on
f3=figure(); hold on

figure(f1);
#Making a plot.
plot(xaxis, T_QRl, "-og",xaxis, T_xl, "-sb",xaxis, T_totall, "-*m")
#Titling the figure.
title ("Computational time against Matrix size", "fontsize", 16);
#Making the legend.
legend({"Q, R computation", "x calculations", "Total Time"},"location", "southeast", "numcolumns", 2)
grid on
#Labelling the axes.
xlabel("Matrix size n -->");
ylabel ("Computational time(Log scale) -->");
set(gca, "fontsize", 7)
#Saving the plot.
print(f1, "-r600", "TimeQR_Matsize.png")

figure(f2);
#Making a plot.
plot(xaxis, log10(L))
#Titling the figure.
title ("L∞ error in x between the QR-code and A\\b", "fontsize", 16);
grid on
#Labelling the axes.
xlabel("Matrix size n -->");
ylabel ("L∞ error in x (Log scale)-->");
set(gca, "fontsize", 7)
#Saving the plot.
print(f2, "-r600", "Linf_Matsize.png")

figure(f3);
#Making a plot.
plot(xaxis, log10(T_QR), "-og",xaxis, log10(T_QRBuiltin), "-sb",xaxis, log10(T_backslash), "-*m",xaxis, log10(T_inv), "-or" )
#Titling the figure.
title ("Computational time against Matrix size", "fontsize", 16);
#Making the legend.
legend({"QR code(self)", "QR code(in-built)", "A\\b", "inv(A)*b"},"location", "southeast", "numcolumns", 2)
grid on
#Labelling the axes.
xlabel("Matrix size n -->");
ylabel ("Computational time(Log scale) -->");
yticks([-6, -5, -4, -3, -2, -1, 0])
set(gca, "fontsize", 7)
#Saving the plot.
print(f3, "-r600", "TimeCompare_Matsize.png")
