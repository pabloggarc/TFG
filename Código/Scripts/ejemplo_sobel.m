imagen = imread('llama.jpg');

sobel_x = [-1 0 1; -2 0 2; -1 0 1];
sobel_y = [-1 -2 -1; 0 0 0; 1 2 1];

derivada_x = convn(double(rgb2gray(imagen)), sobel_x, 'valid');
derivada_y = convn(double(rgb2gray(imagen)), sobel_y, 'valid');
norma_gradiente = sqrt(derivada_x.^2 + derivada_y.^2); 
norma_gradiente = mat2gray(norma_gradiente); 

montage({imagen, 
        uint8(derivada_x), 
        uint8(derivada_y), 
        norma_gradiente
    }); 