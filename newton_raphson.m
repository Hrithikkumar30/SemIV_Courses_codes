% % function { } = newton_raphson( fun , diff, x0)
    
% % x = x0;
% % maxiter = 200;
% % for i = 1:maxiter
% %     x(i+1) = x(i) - fun(x(i))/diff(x(i))
% %     if abs (x(i+1) - x(i)) < tol 
% %         fprintf('the root has converged at x = %.10f\n' , x(i+1));
% %     end
% % end


% % Newton-Raphson Algorithm            
%  % Find the root of y=cos(x) from o to pi.

%  f = @(x) (cos(x));
%  fd = @(x) (-sin(x));
%  p0 = input('Enter initial approximaation: ');
%  n = input('Enter no. of iterations, n: ');
%  tol = input('Enter tolerance, tol:  ');

%  i = 1;
%  while i <= n
%     d=f(p0)/fd(p0);
%     p0 = p0 - d; 
%     if abs(d) < tol
%        fprintf('\nApproximate solution xn= %11.8f \n\n',p0);
%        break;
%     else
%        i = i+1;
%     end
%  end



























