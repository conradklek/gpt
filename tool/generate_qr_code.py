"""
Generates a QR code image from the given data and saves it to the specified file path.
"""
import qrcode


def generate_qr_code(data, file_path):
    """
    Generates a QR code image from the given data and saves it to the specified file path.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(file_path)
    return f'QR code saved to {file_path}'


available_functions = {
    "generate_qr_code": generate_qr_code
}

tools = [
    {
        "type": "function",
        "function": {
            "name": "generate_qr_code",
            "description": "Generates a QR code image from the given data.",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "string",
                        "description": "The data to encode in the QR code."
                    },
                    "file_path": {
                        "type": "string",
                        "description": "The file path where the QR code image will be saved."
                    }
                },
                "required": ["data", "file_path"]
            }
        }
    }
]

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        print(generate_qr_code(sys.argv[1], sys.argv[2]))
    else:
        print("Please provide data and file path as arguments.")
