''' QR Code Generator '''
# Generates a QR code from any URL, text, or data and saves it in three formats: PNG, SVG, and XBM.
# Also displays a live preview directly in the terminal.


import pyqrcode
import os

DATA       = "www.youtube.com/@abdulwaheed-101"   # Data to encode
FILENAME   = "qrcode"                             # Output filename (no extension)
SCALE      = 10                                   # Pixel size per module
ERROR      = "H"                                  # L, M, Q, H (H = best quality)
FG_COLOR   = [0, 0, 0]                            # Foreground/dark color (RGB)
BG_COLOR   = [255, 255, 255]                      # Background/light color (RGB)


def generate_qr(data, filename, scale, error, fg_color, bg_color):
    print(f"\n Generating QR code for: {data}\n")

    # Create the QR code Object
    qr = pyqrcode.create(data, error=error) 

    # Saving as PNG
    try:
        import png
        png_file = filename + ".png"
        qr.png(png_file, scale=scale, module_color=fg_color, background=bg_color)
        print(f" PNG saved:→ {os.path.abspath(png_file)}")
    except ImportError:
        print(" PNG skipped (run: pip install pypng)")

    # Saving as SVG
    svg_file = filename + ".svg"
    qr.svg(svg_file, scale=scale, background="white", module_color="#000000")
    print(f" SVG saved:→ {os.path.abspath(svg_file)}")

    # Saving as XBM
    xbm_file = filename + ".xbm"
    with open(xbm_file, 'w') as f:
        f.write(qr.xbm(scale=scale))
    print(f" XBM saved:→ {os.path.abspath(xbm_file)}")

    # Terminal Preview
    print("\n Terminal Preview:\n")
    print(qr.terminal(quiet_zone=1))

    print(f"\n QR Details:")
    print(f"   Data            : {data}")
    print(f"   Version         : {qr.version}")
    print(f"   Error correction: {qr.error.upper()}")
    print(f"   Mode            : {qr.mode}")
    print(f"   Scale           : {scale}px per module")
    print()

if __name__ == "__main__":
    generate_qr(
        data=DATA,
        filename=FILENAME,
        scale=SCALE,
        error=ERROR,
        fg_color=FG_COLOR,
        bg_color=BG_COLOR
    )