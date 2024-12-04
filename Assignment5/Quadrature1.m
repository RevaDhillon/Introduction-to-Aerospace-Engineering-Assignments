## Quadrature 1

##Creating figures.
f1=figure(); hold on;
f1log=figure(); hold on;
f2=figure(); hold on;
f2log=figure(); hold on;
f3=figure(); hold on;
f3log=figure(); hold on;
f4=figure();hold on;
f4log=figure(); hold on;
figIle = figure(); hold on;
figIre = figure(); hold on;
figTime = figure(); hold on;

##Creating vectors.
delta_x = [];
n = [];
err_LE = [];
ILE = [];
TLE=[];
err_RE = [];
IRE = [];
TRE=[];
err_MP = [];
TMP=[];
err_TZ = [];
TTZ=[];

##Storing values of delta_x and n.
for i=1:100
  delta_x = [delta_x, [pi/(2*i)]];
  n = [n, [i]];
endfor

##Storing corresponding errors, times and riemann sum values.
##Calls to functions in different files.
for i= 1:100
  [errorLE, Ile, Tle] = LeftEnd(delta_x(i), n(i));
  err_LE = [err_LE, [errorLE]];
  ILE = [ILE, [Ile]];
  TLE = [TLE, [Tle]];
  [errorRE, Ire, Tre] = RightEnd(delta_x(i), n(i));
  err_RE = [err_RE, [errorRE]];
  IRE = [IRE, [Ire]];
  TRE = [TRE, [Tre]];
  [errorMP, Tmp] = Midpoint(delta_x(i), n(i));
  err_MP = [err_MP, [errorMP]];
  TMP = [TMP, [Tmp]];
  [errorTZ, Ttz] = Trap(delta_x(i), n(i));
  err_TZ = [err_TZ, [errorTZ]];
  TTZ = [TTZ, [Ttz]];
endfor

figure(f1);
##Making the plot.
plot_linear(delta_x ,err_LE, "Left Endpoint Method", "|Error| -->");
##Saving the plot.
print(f1, "-r500", "LE_Linear.png")

figure(f1log)
##Making the plot.
plot_log(delta_x ,err_LE, "Left Endpoint Method (log-log scale)","|Error| -->")
##Saving the plot.
print(f1log, "-r500", "LE_Log.png")

figure(f2);
##Making the plot.
plot_linear(delta_x ,err_RE, "Right Endpoint Method", "|Error| -->");
##Saving the plot.
print(f2, "-r500", "RE_Linear.png")

figure(f2log)
##Making the plot.
plot_log(delta_x ,err_RE, "Right Endpoint Method (log-log scale)","|Error| -->")
##Saving the plot.
print(f2log, "-r500", "RE_Log.png")

figure(f3);
##Making the plot.
plot_linear(delta_x ,err_MP, "Midpoint Method", "|Error| -->");
##Saving the plot.
print(f3, "-r500", "MP_Linear.png")


#For the MP and TZ methods I have negative values and zero for the best-fit line.
#To fix this I am going to take the most negative value + 10^-6 as correction term.
#So all values will be shifted on loglog scale.
#We know from logic that if we increase n[i], our |error| becomes closer to zero.
#So the largest negative value will be the one corresponding to n[100].

figure(f3log);
##Making the plot.
plot_log(delta_x ,err_MP, "Midpoint Method (log-log scale)","|Error| -->")
##Saving the plot.
print(f3log, "-r500", "MP_Log.png")

figure(f4);
##Making the plot.
plot_linear(delta_x ,err_TZ, "Trapezoidal Method", "|Error| -->");
##Saving the plot.
print(f4, "-r500", "TZ_Linear.png")

figure(f4log);
##Making the plot.
plot_log(delta_x ,err_TZ, "Trapezoidal Method (log-log scale)","|Error| -->")
##Saving the plot.
print(f4log, "-r500", "TZ_Log.png")

figure(figIle);
##Making the plot.
plot_linear_I(delta_x ,ILE, "I_{LE} as f(∆x)","I_{LE} -->")
##Saving the plot.
print(figIle, "-r500", "Ile.png")

figure(figIre);
##Making the plot.
plot_linear_I(delta_x ,IRE, "I_{RE} as f(∆x)","I_{RE} -->")
##Saving the plot.
print(figIre, "-r500", "Ire.png")

##Plotting computational cost of each method on log-log scale.
figure(figTime);
loglog(delta_x, TLE, ".-b");
loglog(delta_x, TRE, ".-g");
loglog(delta_x, TMP, ".-r");
loglog(delta_x, TTZ, ".-m");
##Making the legend.
legend({"Left Endpoint", "Right Endpoint", "Midpoint", "Trapezoidal"}, "location", "northeast")
grid on
##Titling the figure.
title("Computational Cost")
##Labelling the axes.
xlabel("∆x -->")
ylabel("Time(s) -->")
set(gca, "fontsize", 10)
##Saving the plot.
print(figTime, "-r500", "Time.png")


