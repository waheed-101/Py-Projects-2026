# 🔍 QR Code Decoder

A simple Python script that reads a QR code from any image file (PNG, JPG) and decodes the data inside it — using OpenCV.

---

## 📸 Preview

```
 Decoding QR code from: qrcode.png

   Type : QRCODE
   Data : www.youtube.com/@abdulwaheed-101
```

---

## 📦 Requirements

- Python 3.x
- [OpenCV](https://pypi.org/project/opencv-python/)

---

## ⚙️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/waheed-101/Py-Projects-2026.git
cd Py-Projects-2026/Decode_QR_Code
```

**2. Install dependencies:**
```bash
pip install opencv-python
```

---

## 🚀 Usage

**1. Place your QR code image in the same folder as `Decode_QR_Code.py`**

**2. Open `Decode_QR_Code.py` and update the `IMAGE_FILE` variable:**
```python
IMAGE_FILE = "qrcode.png"   # ← change this to your image filename
```

**3. Run the script:**
```bash
python Decode_QR_Code.py
```

---

## 🎨 Customization

You can change this setting at the top of the file:

| Variable | Default | Description |
|---|---|---|
| `IMAGE_FILE` | `"qrcode.png"` | Path to your QR code image |

---

## 💡 Supported Image Formats

| Format | Works |
|---|---|
| PNG | ✅ |
| JPG / JPEG | ✅ |
| BMP | ✅ |
| TIFF | ✅ |

---

## 🔗 Related Project

This project is the companion to **QR Code Generator** — which creates the QR codes that this script decodes!

👉 [Create_QR_Code](../Create_QR_Code/)

---

## 👤 Author

**Abdul Waheed**
- YouTube: [www.youtube.com/@abdulwaheed-101](https://www.youtube.com/@abdulwaheed-101)

---

## 📄 License

This project is open source and free to use.
