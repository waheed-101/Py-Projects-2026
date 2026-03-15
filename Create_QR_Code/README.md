# 🔲 QR Code Generator

A simple Python script that generates a QR code from any URL, text, or data and saves it in three formats: **PNG**, **SVG**, and **XBM** — plus a live preview directly in the terminal.

---

## 📸 Preview

```
 Generating QR code for: www.youtube.com/@abdulwaheed-101

 PNG saved:→ C:\Users\thewa\qrcode.png
 SVG saved:→ C:\Users\thewa\qrcode.svg
 XBM saved:→ C:\Users\thewa\qrcode.xbm

 Terminal Preview:

█████████████████████████████
████ ▄▄▄▄▄ █▀▄▀▀▄█ ▄▄▄▄▄ ████
████ █   █ ██▀▄▀▄█ █   █ ████
████ █▄▄▄█ █▀▀▄▀▄█ █▄▄▄█ ████
████▄▄▄▄▄▄▄█▄█▄█▄█▄▄▄▄▄▄▄████
█████████████████████████████

 QR Details:
   Data            : www.youtube.com/@abdulwaheed-101
   Version         : 5
   Error correction: H
   Mode            : binary
   Scale           : 10px per module
```

---

## 📦 Requirements

- Python 3.x
- [PyQRCode](https://pypi.org/project/PyQRCode/)
- [pypng](https://pypi.org/project/pypng/) ← only needed for PNG output

---

## ⚙️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/abdulwaheed-101/qr-code-generator.git
cd qr-code-generator
```

**2. Install dependencies:**
```bash
pip install PyQRCode
pip install pypng
```

---

## 🚀 Usage

**1. Open `qrcode_generator.py` and update the `DATA` variable:**
```python
DATA = "www.youtube.com/@abdulwaheed-101"   # ← change this to anything
```

**2. Run the script:**
```bash
python qrcode_generator.py
```

**3. Find your QR code files in the same folder:**
```
qrcode.png
qrcode.svg
qrcode.xbm
```

---

## 🎨 Customization

You can change these settings at the top of the file:

| Variable | Default | Description |
|---|---|---|
| `DATA` | YouTube URL | Text or URL to encode |
| `FILENAME` | `"qrcode"` | Output filename (no extension) |
| `SCALE` | `10` | Pixel size per module |
| `ERROR` | `"H"` | Error correction: L, M, Q, H |
| `FG_COLOR` | `[0, 0, 0]` | Foreground color (RGB) |
| `BG_COLOR` | `[255, 255, 255]` | Background color (RGB) |

---

## 📁 Output Formats

| Format | File | Notes |
|---|---|---|
| PNG | `qrcode.png` | Raster image, requires `pypng` |
| SVG | `qrcode.svg` | Vector image, always sharp |
| XBM | `qrcode.xbm` | Plain text bitmap format |

---

## 💡 Examples — What you can encode

```python
DATA = "https://www.google.com"         # Website URL
DATA = "Hello, World!"                  # Plain text
DATA = "tel:+923001234567"              # Phone number
DATA = "mailto:you@example.com"         # Email
DATA = "WIFI:T:WPA;S:MyNet;P:1234;;"    # WiFi credentials
```

---

## 👤 Author

**Abdul Waheed**
- YouTube: [www.youtube.com/@abdulwaheed-101](https://www.youtube.com/@abdulwaheed-101)

---

## 📄 License

This project is open source and free to use.
