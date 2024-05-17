## Ticket Generation Script

This script is designed to generate festival tickets with a given background and unique QR codes for each ticket. It uses the Pillow library for image processing.

### Requirements

- Python 3.x
- Pillow library (Install using pip install Pillow)

### Usage

1. Prepare the folder structure:
 - Create an input folder containing:
 - A background file (e.g., ticket.png)
 - All the QR codes to print (PNG or JPG files)
 - Create an output folder where the generated tickets will be saved.

2. Edit the script:
 - Set the blank_ticket_file_name to the name of your background file.
 - Set input_folder_abs_path to the absolute path of your input folder.
 - Set output_folder_abs_path to the absolute path of your output folder.

3. Adjust QR code size and position:
 - The size of the QR code is defined by sq_fit_size (default is 300 pixels).
 - Adjust paste_x and paste_y to find the right coordinates for pasting the QR code on the ticket background. These coordinates are calculated in pixels.

4. Run the script:
 - Execute the script using python script_name.py.
 - The generated tickets will be saved in the output folder with filenames qr_0.png, qr_1.png, etc.

### Example

If you have the following files in your input folder:
- ticket.png (background file)
- qr1.png (QR code file)
- qr2.png (QR code file)

After running the script, you will get:
- qr_0.png in the output folder (ticket with qr1.png)
- qr_1.png in the output folder (ticket with qr2.png)

### Credits

Script by Maxime Teuber (@Kaz), 2022.
