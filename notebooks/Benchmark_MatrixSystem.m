
r = 0.05;
sigma = 0.2;
T = 1;
K = 100;
S0 = 120;

nt = 100;
ns = 1500;

t = linspace(0,T,nt);
s = linspace(0,3*K,ns)';
dt = t(2)-t(1);
ds = s(2)-s(1);

e1 = ones(ns,1);
data = [e1 -2*e1 e1];
diags = [-1 0 1];

%second derivative
ss2 = spdiags(s.^2,0,ns,ns);
sd = 0.5*sigma.^2*ss2*spdiags(data,diags,ns,ns)/(ds.^2);
data = [-e1 e1];
diags = [-1 1];

%first derivative
fd = r*spdiags(s,0,ns,ns)*spdiags(data,diags,ns,ns)/(2*ds);

%reaction term
reac = -r*speye(ns);
A = sd+fd+reac;
AA = speye(ns-2)-dt*A(2:end-1,2:end-1);

bc = zeros(ns-2,nt);
bc(end,:) = dt*A(end-1,end)*(s(end)-K*exp(-r*t));

tic;
v1 = max(s(2:end-1)-K,0);
plot(s(2:end-1),v1)
for i=1:nt-1
    v1 = AA\(v1+bc(:,i+1));
end
toc;
% around 60ms
plot(s(2:end-1),v1)


[lAA,uAA] = lu(AA);
figure()
tic;
v2 = max(s(2:end-1)-K,0);
for i=1:nt-1
    v2 = uAA\(lAA\(v2+bc(:,i+1)));
end
toc;
plot(s(2:end-1),v2-v1)