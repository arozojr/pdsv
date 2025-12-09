# Projeto de Suavização Seletiva de Bordas em Imagens

## 📋 Descrição

Este projeto implementa uma técnica avançada de processamento de imagens que realiza a **suavização seletiva de bordas**. Diferente de um blur tradicional que afeta toda a imagem, este algoritmo identifica as bordas da imagem e aplica suavização apenas nessas regiões específicas, preservando os detalhes do restante da imagem.

## 🎯 Objetivo

O objetivo principal é criar uma técnica de pós-processamento que:
- Detecta bordas de forma precisa usando o algoritmo Canny
- Aplica suavização (blur) apenas nas regiões de borda
- Preserva os detalhes e a nitidez das áreas internas dos objetos
- Produz uma imagem final com bordas mais suaves e naturais

## 🔧 Tecnologias Utilizadas

- **Python 3.x**
- **OpenCV (cv2)**: Para processamento de imagens e detecção de bordas
- **NumPy**: Para operações matemáticas e manipulação de arrays
- **Matplotlib**: Para visualização e comparação dos resultados

## 📦 Dependências

Para executar o projeto, instale as dependências:

```bash
pip install opencv-python numpy matplotlib
```

Ou usando requirements.txt:

```bash
pip install -r requirements.txt
```

## 🚀 Como Executar

1. **Prepare sua imagem**: Coloque a imagem que deseja processar na raiz do projeto (ou modifique o caminho no código)

2. **Execute o script**:
```bash
python main.py
```

3. **Resultados**:
   - O script salvará a imagem processada como `resultado_suavizado.png`
   - Uma janela será exibida mostrando três imagens lado a lado:
     - Imagem Original
     - Arquivo de Contorno (bordas detectadas)
     - Imagem Saída (resultado final)

## 🔬 Metodologia

O algoritmo segue os seguintes passos:

### 1. Carregamento da Imagem
```python
img = cv2.imread("img2.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
- Carrega a imagem e converte para RGB e escala de cinza

### 2. Detecção de Bordas (Canny)
```python
edges = cv2.Canny(gray, 50, 80)
```
- Utiliza o algoritmo Canny com thresholds de 50 e 80
- Identifica as bordas principais da imagem

### 3. Dilatação das Bordas
```python
kernel = np.ones((3, 3), np.uint8)
edges_dil = cv2.dilate(edges, kernel, iterations=2)
```
- Dilata as bordas detectadas para criar uma região mais ampla
- Isso garante que o blur seja aplicado em uma área maior ao redor das bordas

### 4. Aplicação de Blur Global
```python
blur = cv2.GaussianBlur(img_rgb, (15, 15), 0)
```
- Aplica um filtro Gaussiano com kernel 15x15 na imagem completa
- Este blur será usado apenas nas regiões de borda

### 5. Criação de Máscara Binária
```python
mask = edges_dil / 255.0
mask_3 = np.repeat(mask[:, :, None], 3, axis=2)
```
- Cria uma máscara normalizada (0 a 1) a partir das bordas dilatadas
- Expande a máscara para 3 canais (RGB)

### 6. Blend Seletivo
```python
result = (mask_3 * blur + (1 - mask_3) * img_rgb).astype(np.uint8)
```
- Combina a imagem original com a versão borrada
- Nas bordas (onde mask = 1): usa a imagem borrada
- No restante (onde mask = 0): mantém a imagem original

## 📊 Resultados Obtidos

### Imagens Processadas

O projeto processou várias imagens de teste, incluindo:
- `img.png`
- `img2.png`
- `img4.png`

### Resultado Principal

A imagem `resultado_suavizado.png` demonstra o efeito da técnica:
- **Bordas suavizadas**: As bordas dos objetos ficam mais suaves e naturais
- **Detalhes preservados**: As áreas internas mantêm sua nitidez original
- **Transição natural**: O blend entre áreas borradas e nítidas é imperceptível

### Visualização Comparativa

O script gera uma visualização com três painéis:
1. **Imagem Original**: A imagem de entrada sem processamento
2. **Arquivo de Contorno**: Visualização das bordas detectadas (em escala de cinza)
3. **Imagem Saída**: Resultado final com bordas suavizadas

## 📁 Estrutura do Projeto

```
pdv/
├── main.py                      # Script principal
├── README.md                    # Este arquivo
├── img.png                      # Imagem de teste 1
├── img2.png                     # Imagem de teste 2
├── img4.png                     # Imagem de teste 4
├── resultado_suavizado.png      # Resultado do processamento
└── resultados/                  # Pasta com imagens de resultados
    ├── img.png
    ├── img2.png
    ├── img2Zoom.png
    └── img4.png
```

## ⚙️ Parâmetros Ajustáveis

Você pode modificar os seguintes parâmetros no código para obter resultados diferentes:

- **Thresholds do Canny** (linha 15):
  ```python
  edges = cv2.Canny(gray, 50, 80)  # Ajuste 50 e 80 conforme necessário
  ```

- **Dilatação** (linha 21):
  ```python
  iterations=2  # Aumente para dilatar mais as bordas
  ```

- **Tamanho do Blur** (linha 26):
  ```python
  blur = cv2.GaussianBlur(img_rgb, (15, 15), 0)  # Ajuste (15, 15) para mais/menos blur
  ```

## 🎨 Aplicações

Esta técnica pode ser útil para:
- **Fotografia**: Suavização de bordas duras em retratos
- **Processamento de imagens médicas**: Redução de artefatos em bordas
- **Arte digital**: Criação de efeitos visuais específicos
- **Pré-processamento**: Preparação de imagens para outras técnicas de visão computacional

## 📝 Observações

- O algoritmo funciona melhor com imagens que possuem bordas bem definidas
- Imagens muito complexas podem requerer ajuste dos parâmetros do Canny
- O tamanho do kernel de blur afeta diretamente a intensidade da suavização

## 👤 Autor

Projeto desenvolvido para processamento de imagens com suavização seletiva de bordas.

## 📄 Licença

Este projeto é fornecido como está, para fins educacionais e de pesquisa.

