
# Problem Set 5: Image Processing & Steganography

This project focuses on image processing techniques, specifically **Steganography** (hiding and recovering secret images within the Least Significant Bits of another image) and applying custom pixel filters.

---

## 📁 Project Structure & Generated Outputs

The following output images are generated after running the implementation:

1. **`image3.png`** (Filtered Image): 
   * The result of applying the pixel filter (originally referred to as `image_15.png`).
2. **image1.png** (Recovered Grayscale Image): 
   * The secret black-and-white/grayscale image extracted from `hidden1.bmp` using LSB decoding and rescaled to full $[0, 255]$ contrast.
3. **`image2.png`** (Recovered Color Image): 
   * The secret RGB color image extracted from the 3 LSBs of `hidden2.bmp` and rescaled to full contrast.

---

## 🛠️ Key Implementations

### 1. LSB Extraction (`extract_end_bits`)
Extracts the $n$ least significant bits (LSB) from a pixel value (either a single grayscale integer or an RGB tuple) using modulo arithmetic:
$$\text{LSB} = \text{pixel} \pmod{2^n}$$

### 2. Contrast Rescaling (`rescale`)
Stretches the low-contrast extracted LSB values (which range from $0$ to $2^n - 1$) to the full 8-bit range ($0$ to $255$) using a precise scaling multiplier:
$$\text{Multiplier} = \frac{255}{2^n - 1}$$

### 3. Image Recovery (`reveal_bw_image` & `reveal_color_image`)
Processes each pixel of the stego-images, extracts the hidden bits, rescales the values, and reconstructs the hidden images as PIL Image objects.

---

## 🚀 How to Run

1. Make sure you have the required dependencies installed (specifically **Pillow** for image processing):
```bash
   pip install Pillow

```

2. Run the test suite to verify the code logic:
```bash
python test_ps5_student.py

```


3. Run the main script to generate the output images (`image1.png`, `image2.png`, `image3.png`):
```bash
python ps5.py

```



---

## ✍️ Watermarking & Submission

To finalize the submission:

1. Use the helper function `draw_kerb` to apply your unique Kerberos watermark to `image1.png`, `image2.png`, and `image3.png`.
2. Combine the watermarked images into a single PDF.
3. **Note:** Remember to comment out any `draw_kerb` function calls in `ps5.py` before submitting to the autograder to prevent testing failures.
