% Plot complex root of polynomial function

clear;
clc;
fonction = [1 0 0 0 0 0 0 1 1];    % x^8 + x + 1

% calclate root
racines = roots(fonction);

% convert result to list
racine_complex = [racines];


% loop through roots
for i = 1:size(racine_complex)
   racine = racine_complex(i);
   partie_reelle = real(racine);
   partie_img = imag(racine);
   
   plot([partie_reelle], [partie_img], 'o');
   hold on;   
endfor
