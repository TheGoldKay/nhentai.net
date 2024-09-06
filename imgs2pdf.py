import os
from img2pdf import convert

def save_pdf(did):
    image_dir = os.path.join(os.getcwd(), f'download/{did}')
    image_paths = []
    for filename in os.listdir(image_dir):
        if filename.endswith('.json'):
            continue
        image_path = os.path.join(image_dir, filename)
        image_paths.append(image_path)

    # Sort the image paths to ensure correct order
    image_paths.sort()
    pdf_content = convert(image_paths)
    # get the code name
    name = image_dir.split('/')[-1].strip()
    # Save the PDF file
    with open(os.path.join(image_dir, f'{name}.pdf'), 'wb') as file:
        file.write(pdf_content)

    print(f'{did} -> PDF file created successfully!')