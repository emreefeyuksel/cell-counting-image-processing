# 🧬 Cell Counting Using Image Processing

### COMP 4360 – Assignment 1

**Author:** Emre Efe Yüksel  
🔗 **LinkedIn:** [emre-efe-yüksel](https://www.linkedin.com/in/emre-efe-y%C3%BCksel/)  
🔗 **GitHub:** [emreefeyuksel](https://github.com/emreefeyuksel)

This project compares three different computer vision techniques for counting cells in microscopy images. The goal is to evaluate the strengths and weaknesses of each method and determine which performs best for images containing circular biological structures.

---

## 📌 1. Overview

Three distinct approaches were tested, each using a different principle of image processing:

| Method                                       | Approach Type   | Strength                                                       |
| -------------------------------------------- | --------------- | -------------------------------------------------------------- |
| **Hough Circle Transform**                   | Geometry-based  | Highest accuracy; excellent for circular and overlapping cells |
| **Canny Edge Detection + Contours**          | Edge-based      | Shape flexibility; robust to irregular cell outlines           |
| **Otsu Thresholding + Connected Components** | Intensity-based | Automatic thresholding; simple segmentation                    |

---

## 🧪 2. Methods

### **🔵 Method 1 — Hough Circle Transform**

* Gaussian Blur (9×9, σ=2)
* Circular detection via `cv2.HoughCircles`
* **Key parameters:**
  * dp = 1
  * minDist = 15
  * param1 = 50
  * param2 = 20
  * radius range = 10–30 px

**Why it works best:**  
The image contains roughly circular shapes. Hough's geometric voting mechanism reconstructs circles even in heavy overlap regions.

---

### **⚪ Method 2 — Canny Edge Detection + Contours**

* Gaussian Blur (5×5)
* Canny thresholds: 25–100
* Contour area filtering between 30–4500 px²

**Strengths:**
* No shape assumption → handles irregular cell boundaries

**Weakness:**
* Touching cells often merge into a single contour, reducing accuracy

---

### **⚫ Method 3 — Otsu Thresholding + Connected Components**

* Gaussian Blur (5×5)
* Otsu global threshold
* Morphology:
  * Erosion ×2
  * Dilation ×1

**Strengths:**
* Fully automatic threshold selection

**Weakness:**
* Erosion can remove smaller cells
* Global thresholding assumes uniform lighting

---

## 📊 3. Results

### **Quantitative Summary**

| Method                      | Detected Cells |
| --------------------------- | -------------- |
| **Hough Circle Transform**  | **283**        |
| Canny + Contours            | 223            |
| Otsu + Connected Components | 245            |

**Winner:**  
➡️ **Hough Circle Transform** (~94–100% of estimated ground truth)

---

## 🖼️ 4. Visual Outputs

The repository includes pipeline visualizations:

* `method1_hough_circle.png`
* `method2_canny_contours.png`
* `method3_blobs.png`
* `methods_comparison.png`

Contours and detections are marked in green for clarity.

---

## 🧩 5. Code

The full source code is available in `main.py`.  
Required packages:

```bash
pip install opencv-python numpy matplotlib
```

The script:

* Loads the input image
* Applies all three segmentation/counting approaches
* Saves comparison figures
* Prints final cell counts to the console

---

## 📝 6. Discussion & Conclusion

The experiments show that **geometry-driven approaches** like the Hough Circle Transform outperform general edge-based and intensity-based approaches for circular cell structures.

* **Method 1** handles overlapping cells extremely well
* **Method 2** is more flexible but merges touching cells
* **Method 3** benefits from automatic thresholding but loses detail due to erosion

### **Recommendation:**

For microscopy images dominated by circular shapes, **Hough Circle Transform** provides the most reliable and accurate results among the tested methods.

This assignment strengthened understanding of image preprocessing, segmentation techniques, and parameter tuning in image processing pipelines.

---

## 📂 Project Structure

```
📁 project-root
│── README.md
│── main.py
│── cells.png
│── method1_hough_circle.png
│── method2_canny_contours.png
│── method3_blobs.png
└── methods_comparison.png
```

---

## 📄 License

This project is created for educational purposes as part of COMP 4360 coursework.

---

**Questions or feedback?** Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/emre-efe-y%C3%BCksel/) or open an issue on GitHub!
