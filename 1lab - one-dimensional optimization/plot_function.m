x = -20 : 0.00001 : 20;
y = sin(x) - log(x .* x) - 1;
plot(x,y)