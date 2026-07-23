#!/usr/bin/env python3
"""Generate a stable QR code PNG for the site URL.

"Stable" here means deterministic: the same URL and the same settings
below always produce the identical QR pattern. If you ever regenerate,
keep VERSION, ERROR_CORRECTION, and BORDER unchanged so the image
matches any copies you've already printed or shared.

Usage:
    pip install "qrcode[pil]"
    python scripts/generate_qr.py                 # -> images/site_qr.png
    python scripts/generate_qr.py -o out.png       # custom output path
    python scripts/generate_qr.py --box-size 20    # larger image
"""

import argparse

import qrcode
from qrcode.constants import ERROR_CORRECT_M

URL = "https://mspitzerbrooks.github.io/"

# Fixed parameters -> stable, reproducible output. Don't change these
# once you've distributed the code.
VERSION = 3            # 29x29 modules; comfortably fits the URL
ERROR_CORRECTION = ERROR_CORRECT_M  # ~15% recovery
BORDER = 4             # quiet zone (modules); 4 is the spec minimum


def make_qr(url: str, box_size: int) -> "qrcode.image.pil.PilImage":
    qr = qrcode.QRCode(
        version=VERSION,
        error_correction=ERROR_CORRECTION,
        box_size=box_size,
        border=BORDER,
    )
    qr.add_data(url)
    qr.make(fit=False)  # fit=False -> VERSION is honored, keeping output stable
    return qr.make_image(fill_color="black", back_color="white")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a stable QR code PNG.")
    parser.add_argument("-o", "--output", default="images/site_qr.png",
                        help="output PNG path (default: images/site_qr.png)")
    parser.add_argument("--box-size", type=int, default=10,
                        help="pixels per module (default: 10)")
    parser.add_argument("--url", default=URL, help=f"URL to encode (default: {URL})")
    args = parser.parse_args()

    img = make_qr(args.url, args.box_size)
    img.save(args.output)
    print(f"Wrote {args.output} for {args.url}")


if __name__ == "__main__":
    main()
