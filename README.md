# src-skytrak_qr.py
# SKYTRAK / STPLUS Wi-Fi QR Generator (Python / Windows)

Python utility created to help QC technicians save time and avoid manual errors during device quality checks.

During QC, technicians connect SKYTRAK units to a PC through Wi-Fi and must record device identifiers into an Excel sheet. Manual copy/paste and typing can be slow and error-prone.

This tool:
- Reads Wi-Fi interface details using `netsh wlan show interfaces`
- Detects SKYTRAK / STPLUS devices
- Extracts the device identifier
- Generates a QR code to make capture and logging faster

## Why this exists (QC workflow)
- Faster quality checks
- Less manual typing
- Reduces mistakes when recording identifiers into Excel sheets

## Requirements
- Windows 10/11
- Python 3.8+

## Install
```bash
pip install pyqrcode pypng Pillow
python src/skytrak_qr.py
