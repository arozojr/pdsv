import cv2
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------
# 1) Carrega imagem
# -----------------------------------------
img = cv2.imread("img8.png")   # coloque sua imagem aqui
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -----------------------------------------
# 2) Detecta bordas
# -----------------------------------------
edges = cv2.Canny(gray, 80, 120)

# -----------------------------------------
# 3) Dilata as bordas
# -----------------------------------------
kernel = np.ones((3, 3), np.uint8)
edges_dil = cv2.dilate(edges, kernel, iterations=2)

# -----------------------------------------
# 4) Aplica blur global
# -----------------------------------------
blur = cv2.GaussianBlur(img_rgb, (9, 9), 0)

# -----------------------------------------
# 5) Cria máscara binária (0 ou 1)
# -----------------------------------------
mask = edges_dil / 255.0
mask_3 = np.repeat(mask[:, :, None], 3, axis=2)

# -----------------------------------------
# 6) Blend: blur apenas na borda
# -----------------------------------------
result = (mask_3 * blur + (1 - mask_3) * img_rgb).astype(np.uint8)

# -----------------------------------------
# 7) (Opcional) Salva resultado
# -----------------------------------------
cv2.imwrite("resultado_suavizado.png",
            cv2.cvtColor(result, cv2.COLOR_RGB2BGR))

# -----------------------------------------
# 8) Painel 3x3: passo a passo do procedimento
# -----------------------------------------
fig, axes = plt.subplots(3, 3, figsize=(10, 10))

# 1) Imagem original
axes[0, 0].imshow(img_rgb)
axes[0, 0].set_title("1) Imagem original", fontsize=9)
axes[0, 0].axis("off")

# 2) Escala de cinza
axes[0, 1].imshow(gray, cmap="gray")
axes[0, 1].set_title("2) Escala de cinza", fontsize=9)
axes[0, 1].axis("off")

# 3) Bordas (Canny)
axes[0, 2].imshow(edges, cmap="gray")
axes[0, 2].set_title("3) Bordas (Canny)", fontsize=9)
axes[0, 2].axis("off")

# 4) Bordas dilatadas
axes[1, 0].imshow(edges_dil, cmap="gray")
axes[1, 0].set_title("4) Bordas dilatadas", fontsize=9)
axes[1, 0].axis("off")

# 5) Máscara (0 e 1)
axes[1, 1].imshow(mask, cmap="gray")
axes[1, 1].set_title("5) Máscara da borda", fontsize=9)
axes[1, 1].axis("off")

# 6) Blur global
axes[1, 2].imshow(blur)
axes[1, 2].set_title("6) Blur global", fontsize=9)
axes[1, 2].axis("off")

# 7) Resultado final
axes[2, 0].imshow(result)
axes[2, 0].set_title("7) Resultado final", fontsize=9)
axes[2, 0].axis("off")

# 8) Zoom borda original
h, w, _ = img_rgb.shape
x1, y1, box = w//1 - 100, h//1 - 200, 180   # ajuste se quiser outra região
zoom_orig = img_rgb[y1:y1+box, x1:x1+box]
axes[2, 1].imshow(zoom_orig)
axes[2, 1].set_title("8) Zoom borda (original)", fontsize=9)
axes[2, 1].axis("off")

# 9) Zoom borda suavizada
zoom_res = result[y1:y1+box, x1:x1+box]
axes[2, 2].imshow(zoom_res)
axes[2, 2].set_title("9) Zoom borda (suavizada)", fontsize=9)
axes[2, 2].axis("off")

plt.tight_layout()
plt.subplots_adjust(top=0.8)
plt.show()