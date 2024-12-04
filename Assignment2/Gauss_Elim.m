#Gaussian Elimination
1;#Runs sometimes, says n not defined other times.

#Function to create a matrix and a vector of order n.
function [A, b] = Gen_Matrices (n)
  A=randn(n)
  b=randn(n,1)
endfunction

#Function to return the solution vector xM1 of a system of linear equations.
function [xM1] = Gauss_Elim (A, b, n)
  #Creating the solution vector.
    xM1=zeros(n,1)
    #Creating the augmented matrix.
    A=[A, [b]]
    #Coverting A to an upper triangular matrix.
    A = triu(A)
    #Nested for loops.
    for i=1:n
      sum=0
      for k=n-i+2:n
        sum+=xM1(k,1)*A(n+1-i,k)
      endfor
      #Obtaining the components of the solution vector.
      xM1(n+1-i,1)=(b(n+1-i,1)-sum)/A(n+1-i, n+1-i)
    endfor
endfunction

#Vector to provide size of matrix n.
matrix_size=1:11:100
#Vector to store the time taken by method 1.
M1=[]
#Vector to store the time taken by method 2.
M2=[]
#Vector to store the time taken by method 3.
M3=[]
#Vector to store the L infinity norm between methods 1 and 2.
L12=[]
#Vector to store the L infinity norm between methods 1 and 3.
L13=[]
#Loop for matrix size n.
for i=matrix_size
  [A, b] = Gen_Matrices(i)
  #Calculating time corresponding to n.
  tic(); xM1 = Gauss_Elim(A, b, i); M1=[M1, [toc()]]
  tic(); xM2 = inv(A)*b; M2=[M2, [toc()]]
  tic(); xM3 = A\b; M3=[M3, [toc()]]
  #Calculating L infinity norm corresponding to n.
  L12=[L12, [norm(xM1-xM2, inf)]]
  L13=[L13, [norm(xM1-xM3, inf)]]
endfor

#Creating figures.
f1=figure(); hold on
f2=figure(); hold on

figure(f1);
#Making a plot.
plot(matrix_size, M1, "-og",M2, "-sb", M3, "-*m")
#Titling the figure.
title ("Wall clock time against Matrix size", "fontsize", 16);
#Making the legend.
legend({"Method 1", "Method 2", "Method 3"}, "location", "northwest")
grid on
#Labelling the axes.
xlabel("Matrix size n -->");
ylabel ("Wall clock time -->");
set(gca, "fontsize", 10)
#Saving the plot.
print(f1, "-r300", "Time_Matsize.png")

figure(f2);
#Making a plot.
plot(matrix_size, L12,"-og", L13,"-*b")
#Titling the figure.
title("L infinity norm of error against Matrix size",  "fontsize", 14);
#Making the legend.
legend({"Method 1 and 2", "Method 1 and 3"}, "location", "north")
grid on
#Labelling the axes.
xlabel ("Matrix size n -->");
ylabel ("L infinity norm -->");
set(gca, "fontsize", 10)
#Saving the plot.
print(f2, "-r300", "Linf_Matsize.png")

%triu code:  for i=1:n
   %               for j=i+1:n
    %              A(j,:)=A(j,:)-A(j,i)*A(i,:)/A(i,i)
     %             endfor
      %         endfor

