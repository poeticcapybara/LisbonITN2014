function D = pairwise_matlab(X)
%Calculate difference between elements of array

[M,N] = size(X);
D = zeros(M,M);
for i=1:M
    for j=1:M
        d = 0.0;
        for k=1:N
            tmp = X(i,k)-X(j,k);
            d = d+tmp*tmp;
        end
        D(i,j) = sqrt(d);
    end
end
end
