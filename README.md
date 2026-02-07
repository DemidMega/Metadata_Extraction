markdown
# Image Metadata (EXIF) Extractor

A simple and efficient Python tool to extract hidden metadata from image files. This script allows you to view technical details, device information, and GPS coordinates stored inside your photos.

## 📋 Features
- **GPS Tracking:** Extract latitude and longitude (link to Google Maps).
- **Device Info:** Identify camera make, model, and software version.
- **Shot Details:** View ISO, exposure time, aperture, and focal length.
- **Timestamps:** Get the exact date and time the photo was taken.

## 🛠 Installation
Make sure you have Python 3.x installed. Then, install the required Pillow library:

```
pip install Pillow
```

🚀 How to Use
Clone this repository or download the script.
Place the target image in the same directory as the script.
Run the following command:

```
python MetaData.py
```

⚠️ Important Note
Most social media platforms (Telegram, WhatsApp, VK) strip EXIF metadata to protect user privacy. To extract data, ensure you are using original files (e.g., photos sent as "Documents" or transferred via USB).

📄 License
This project is open-source and free to use.
