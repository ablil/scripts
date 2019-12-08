function [l, u] = decompositionLU(A)
%{
 decomposer la matrice A en un produit
de deux matrice, L triangulaire inf avec des uns dans la diagonale
 U triangulaire superieur
il ya une fonction deje cree dans matlab lu(A), mais elle ne
 donne pas une matrice l avec des uns dans la diagonale
%}
    if det(A) == 0
        error('la matrice nest pas inversible');
    end

    % avoir la dimension de la matrice A
   [a, n] = size(A);
   if (a ~= n)
       error('la matrice doit etre carre');
   end
   
   % creer la matrice u avec des zeros
   u = zeros(n);
   
   % creer la matrice L avec les uns dans la diagonale
   l = zeros(n);
   tmp = 1;
   while tmp <= n
       l(tmp,tmp) = 1;
       tmp = tmp + 1;
   end
   
   
   %calculer le premier ligne et colonne
   for j=1:n
       u(1,j) =  (A(1,j));
   end
   for i=1:n
       l(i,1) =  (A(i,1)/u(1,1));
   end
   
   ligne = 2;
   colonne = 2;
   
   % decomposer le matrice
   while (ligne <= n) && (colonne <= n)
       % trouver la ligne de U
       for j=2:n
           somme = 0;
           for k=1:ligne-1
               somme = somme +  (l(ligne, k)*u(k, j));
           end
           u(ligne, j) =  ((A(ligne, j) -  (somme))/l(ligne,ligne));
       end
       ligne = ligne + 1;
       
       % trouver la colonne de L
       for i=2:n
           somme = 0;
           for k=1:colonne-1
               somme = somme +  (l(i,k)*u(k, colonne));
           end
           l(i, colonne) =  ((A(i,colonne) -  (somme))/u(colonne, colonne));
       end
       colonne = colonne +1;
   end
   u = sym(u);
   l = sym(l);
   return
end