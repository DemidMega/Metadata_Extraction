from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def get_absolutely_all_metadata(filename):
    try:
        img = Image.open(filename)
        # Getting basic EXIF data
        exif_data = img.getexif()

        print(f"--- FILE ANALYSIS: {filename} ---")

        # Main tags (what you have already seen + hidden ones)
        print("\n[BASIC DATA]:")
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            print(f"{tag_name}: {value}")

        # 2. Nested Directories (IFD) — shooting details are often hidden here
        for ifd_id in [0x8769, 0x8825, 0x0100]:  # Exif, GPS, Interop
            try:
                ifd_data = exif_data.get_ifd(ifd_id)
                dir_name = "GPS" if ifd_id == 0x8825 else "DETAILED_EXIF"
                print(f"\n[{dir_name}]:")

                for tag_id, value in ifd_data.items():
                    # We are trying to decipher the tag name using standard dictionaries
                    tag_name = TAGS.get(tag_id, GPSTAGS.get(tag_id, tag_id))
                    print(f"{tag_name}: {value}")
            except:
                continue

        # 3. Additional information about the format
        print("\n[ADDITIONALLY]:")
        print(f"Format: {img.format}")
        print(f"Mode: {img.mode}")
        print(f"Size: {img.size}")

    except Exception as e:
        print(f"ERROR: {e}")


# Launch, check the file name
get_absolutely_all_metadata('photo.jpg')