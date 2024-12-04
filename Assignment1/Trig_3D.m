%To plot a multivariable sine function.

%Creates an evenly spaced sequence from -1 to 1 stored in tx and ty.(Row vector)
tx = ty = linspace(-1,1);

%Meshgrid used to produce input for the 3-D function that will be plotted.
[xx, yy]=meshgrid(tx, ty);

%Sequence tz obtained using corresponding values of xx and yy.
% 'dot' implies element by element operation.
tz=sin(10*(xx.^2+yy.^2))/10;

hf = figure()
%Plotting a 3-D wireframe mesh with selected properties.
mesh(tx, ty, tz, "linewidth", 1.5 , "facecolor", "k")
%x-axis, y-axis and z-axis labelled.
xlabel('x -->')
ylabel('y -->')
zlabel('f(x, y) -->')
%Selecting the shading of patches.
shading flat;
%Saving the figure.
saveas(hf, "Trig3D.png")


