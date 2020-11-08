# FotoPixeladaExcel

Como criar uma foto pixelada no Excel


A ideia deste tutorial é pegar uma imagem qualquer e pintar as células do Excel de forma correspondente.

![](https://ferramentasexcelvba.files.wordpress.com/2020/11/fotoexcel.jpg)

Uma imagem é apenas um retângulo dividido em quadriculados (o pixel), e cada pixel é pintado de uma cor.

Imagine que cada célula é pintada de uma combinação de Vermelho, Verde e Azul, as cores primárias.

![](https://ferramentasexcelvba.files.wordpress.com/2020/11/rgb.jpg)

Cada célula terá um tom de Red, Green e Blue, e essa tonalidade varia de 0 a 255.

Infelizmente, o VBA não tem uma boa biblioteca de manipulação de imagens. Recomendo instalar o OpenCV (open computer vision), no Python.

https://pypi.org/project/opencv-python/

A rotina tem dois passos:

1 – ler a imagem e salvar a matriz de dados (Python)

2 – ler a matriz de dados e colorir o Excel

Passo 1) Rodar o arquivo “OpenCVReadFile.py”, no Python.

Indicar a localização do arquivo de imagem a desenhar

Mudar o local do arquivo CSV de destino.

Essa rotina lê a imagem e salva a matriz de dados em CSV.

![](https://ferramentasexcelvba.files.wordpress.com/2020/11/codigo01.jpg)

Passo 2)  Rodar a macro “Pixeliza” do Excel em anexo. É necessário mudar o endereço do arquivo CSV.

![](https://ferramentasexcelvba.files.wordpress.com/2020/11/codigo02.jpg)

E pronto, temos uma reprodução da imagem na planilha, que pode ser editada normalmente, como qualquer arquivo Excel.

Atenção. Rodando essa macro, descobri que o Excel tem um limite de 4000 células com formatação diferente.

E, pior, chega facilmente nesse limite.

Portanto, o esquema citado só funciona com imagens de resolução muito baixa.

Vide arquivos no Github: https://github.com/asgunzi/FotoPixeladaExcel

Tem o Excel com a macro e o código Python.



Ideias técnicas com uma pitada de filosofia

https://ideiasesquecidas.com/
