import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

def extract_palette(image_path, num_colors=5):
    try:
        img = Image.open(image_path)
        img.thumbnail((200, 200)) 
        
        image_array = np.array(img)
        pixel_data = image_array.reshape(-1, 3) 
        
        kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init='auto', max_iter=300)
        kmeans.fit(pixel_data)
        
        colors = kmeans.cluster_centers_
        palette = [tuple(map(int, color)) for color in colors]
        
        return palette
        
    except FileNotFoundError:
        return None
    except Exception:
        return None

image_file_path = "path/to/your/image.jpg" 
dominant_colors = extract_palette(image_file_path, num_colors=6)

if dominant_colors:
    for i, color in enumerate(dominant_colors):
        r, g, b = color
        swatch = f"\033[48;2;{r};{g};{b}m    \033[0m"
        print(f"Color {i+1}: {swatch} RGB {color}")
