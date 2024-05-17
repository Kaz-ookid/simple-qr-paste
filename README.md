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

### Script

python <if __name__ == '__main__': < import os < from PIL import Image < < # Script by @maxime_tbr (Telegram) | 2022 < # Its purpose is to paste QR codes on a ticket background. < # This is a scrap script so feel me to ask me for any help :) < # Need to install Pillow : pip install Pillow < < # USE: < # Prepare a folder with the following elements inside : < # - an output folder < # - an input folder that will contain : < # * the background file you want to paste QRs on < # * all the QRs to print. < # Please do not add any other file inside this input folder other than specified above! < < # You should try with a single QR to find the right adjustments for your QRs size and positions. < # Play with paste_x and paste_y to find the right coordinates. < # Coordinates are calculated in pixels, but you'll have a better time trying to adjust position rather than calculating it. < # Don't forget to change the filenames and paths below. < < # The size of the QR in pixels < sq_fit_size = 300 < < # TO FILL < blank_ticket_file_name = 'ticket.png' < input_folder_abs_path = 'C:/absolut/path/to/the/INPUT/folder/' < output_folder_abs_path = 'C:/absolut/path/to/the/OUTPUT/folder/' < # -------------------------------------------- < < blank_ticket_file = input_folder_abs_path + blank_ticket_file_name < ticketIm = Image.open(blank_ticket_file) < ticketWidth, ticketHeight = ticketIm.size < i = 0 < for qr_filename in os.listdir(input_folder_abs_path): < # /!\ All png and jpg files other than the background are considered as QR codes /!\ < if not (qr_filename.endswith('.png') or qr_filename.endswith('.jpg')) or qr_filename == blank_ticket_file_name: < continue < im = Image.open(input_folder_abs_path + qr_filename) < width, height = im.size < # print("Adding QR code to %s" % qr_filename) DEBUG < temp_im = ticketIm < paste_x = ticketWidth - ((ticketWidth / 2 - width) / 2 + width) < paste_y = ticketHeight - ((ticketHeight - height) / 2 + height) + 50 < temp_im.paste(im, (paste_x, paste_y)) < temp_im.save(os.path.join(output_folder_abs_path, "qr_" + str(i) + ".png")) < i += 1 <

### Credits

Script by Maxime Teuber (@Kaz), 2022.
