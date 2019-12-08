function [output_A output_b] = diagonalisationParGauss(A, b)
%{
resoudre un system d'equation A.x = b
renvoyer les deux matrices A et B apres diagonalisation par Gauss.
%}
	% verifier la coherence du systeme
	[line col] = size(A);
	if line ~= col
		error('la matrice donne doit etre carre');
    else 
        outputs = zeros(line);
    end
    n = line;
    [line col] = size(b);
    if (line ~= n) || (col ~= 1)
        error('les dimension de A et B ne sont pas coherent');
    end
    
    % creer les varibles de sortie
    output_A = zeros(n,n);
    output_b = ones(n,1);
    
    % the script
    for k=1:n-1
        pivot = A(k,k);
        if pivot ~= 0
            for i=k+1:n
                output_b(i,1) = b(i,1) - (A(i,k)/pivot)*b(k,1);
                for j=k+1:n
                    output_A(i,j) = A(i,j) - (A(i,k)/pivot)*A(k,j);
                end
            end
        else
            error('un erreur s est produit: un pivot est nul');
        end
    end
    disp(output_A)
    disp(output_b)
    return
end