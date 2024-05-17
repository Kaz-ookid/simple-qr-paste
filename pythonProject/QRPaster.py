if __name__ == '__main__':
    import os
    from PIL import Image

    # Script by @maxime_tbr (Telegram) | 2022
    # Its purpose is to paste QR codes on a ticket background.
    # This is a scrap script so feel me to ask me for any help :)
    # Need to install Pillow : pip install Pillow

    # USE:
    # Prepare a folder with the following elements inside :
    # - a subfolder named OUTPUT
    # - the background file you want to paste QRs on
    # - all the QRs to print.
    # Please do not add any other file inside this main folder other than specified above!

    # You should try with a single QR to find the right adjustments for your QRs size and positions.
    # Play with paste_x and paste_y to find the right coordinates.
    # Coordinates are calculated in pixels, but you'll have a better time trying to adjust position rather than calculating it.
    # Don't forget to change the filenames and paths below.

    # The size of the QR in pixels
    sq_fit_size = 300

    # TO FILL
    blank_ticket_file_name = 'ticket.png'
    input_folder_abs_path = 'C:/absolut/path/to/the/INPUT/folder/'
    # --------------------------------------------

    blank_ticket_file = input_folder_abs_path + blank_ticket_file_name
    ticketIm = Image.open(blank_ticket_file)
    ticketWidth, ticketHeight = ticketIm.size
    i = 0
    for qr_filename in os.listdir(input_folder_abs_path):
        # /!\ All png and jpg files other than the background are considered as QR codes /!\
        if not (qr_filename.endswith('.png') or qr_filename.endswith('.jpg')) or qr_filename == blank_ticket_file_name:
            continue
        im = Image.open(input_folder_abs_path + qr_filename)
        width, height = im.size
        # print("Adding QR code to %s" % qr_filename)   DEBUG
        temp_im = ticketIm
        paste_x = ticketWidth - ((ticketWidth / 2 - width) / 2 + width)
        paste_y = ticketHeight - ((ticketHeight - height) / 2 + height) + 50
        temp_im.paste(im, (paste_x, paste_y))
        temp_im.save(os.path.join(input_folder_abs_path + "\OUTPUT", "qr_" + str(i) + ".png"))
        i += 1
