%Linear Regression

#Creating figures.
f1=figure(); hold on;
f2=figure(); hold on;
f3=figure(); hold on;

#Matrix to store the data values in the file.
A1=load('-ascii', "data1.txt")
#Vectors to store the columns of A1.
v11=A1(1:50, 1)
v12=A1(1:50, 2)
#Adding a column of all ones.
mv11=[v11, [ones(50,1)]]
#Finding [m; c].
X=inv((mv11')*mv11)*(mv11')*v12
#Storing the values of y on the line.
y1=mv11*(X)
#Calculations for better parabolic model.
a4=v11(40,1)*v11(40,1)/v12(40,1)
#Storing the values of y on the parabola.
para_y= v11.*v11.*1/a4

figure(f1);
#Making plots.
scatter(v11, v12, 16, "filled")
plot(v11,y1, "m")
plot(v11, para_y , "g")
#Making the legend.
legend({"Scatter plot","Linear Regression", "Better Model"}, "location", "northwest")
grid on
#Titling the figure.
title("Linear Regression: Dataset 1")
#Labelling the axes.
xlabel("x -->")
ylabel("y -->")
set(gca, "fontsize", 10)
#Saving the plot.
print(f1, "-r300", "LG_Data1.png")

#Matrix to store the data values in the file.
A2=load('-ascii', "data2.txt")
#Vectors to store the columns of A2.
v21=A2(1:100, 1)
v22=A2(1:100, 2)
#Adding a column of all ones.
mv21=[v21, [ones(100,1)]]
#Finding [m; c].
X=inv((mv21')*mv21)*(mv21')*v22
#Storing the values of y on the line.
y2=mv21*(X)

figure(f2);
#Making plots.
scatter(v21, v22, 10, "filled")
plot(v21,y2, "m")
grid on
#Titling the figure.
title("Linear Regression: Dataset 2")
#Making the legend.
legend({"Scatter plot","Linear Regression"}, "location", "northwest")
#Labelling the axes.
xlabel("x -->")
ylabel("y -->")
set(gca, "fontsize", 10)
#Saving the plot.
print(f2, "-r300", "LG_Data2.png")

#Matrix to store the data values in the file.
A3=load('-ascii', "data3.txt")
#Vectors to store the columns of A3.
v31=A3(1:200, 1)
v32=A3(1:200, 2)
#Adding a column of all ones.
mv31=[v31, [ones(200,1)]]
#Finding [m; c].
X=inv((mv31')*mv31)*(mv31')*v32
#Storing the values of y on the line.
y3=mv31*(X)

figure(f3);
#Making plots.
scatter(v31, v32, 5)
plot(v31,y3, "m")
#Making the legend.
legend({"Scatter plot","Linear Regression"}, "location", "northwest")
grid on
#Titling the figure.
title("Linear Regression: Dataset 3")
#Labelling the axes.
xlabel("x -->")
ylabel("y -->")
set(gca, "fontsize", 10)
#Saving the plot.
print(f3, "-r300", "LG_Data3.png")

