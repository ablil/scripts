function [ somme ] = arithmetic_geometric( liste )

%{
verifier si une suite de nomber est une suite geometrique ou geometrique
et renvoyer la somme de ces elements.
Si la suite nest ni geometrique ni arithmetique, la somme nest pas cacule.

comment utiliser  :
    arithmetic_geometric([1,2,3,4,5,6,7,8])
%}
    arithmetique = 1;
    geometrique = 1 ;
    somme = 0 ;
    
    [~, taille] = size(liste); % le nombre d'elements
    pas = liste(2) - liste(1); % le pas d'une serie arithmetique
    raison = liste(2) / liste(1); % le raison d'une serie geometrique
    
    % verifier si la suite est arithmetique
    for i=1:taille-1  
        if liste(i + 1) - liste(i) ~= pas
            arithmetique = 0;
            break
        end
    end
    
    % verifier si la suite est geometrique
    for i=1:taille - 1
        if liste(i+1)/liste(i) ~= raison
            geometrique = 0;
            break
        end
    end
    
    % calculer la somme
    if arithmetique
        disp('la suite est arithmetique');
        somme = (liste(1) + liste(taille)*(taille))/2 ;
        disp('la somme est :');
        return
    end
    
    if geometrique
        disp('la suite est geometrique');
        somme = liste(1) * (1 - raison^(taille))/(1 - raison);
        disp('la somme est :');
        return 
    end
    
    disp('la suite nest pas goemtrique.');
    disp('la suite nest pas arithmetique');
end

