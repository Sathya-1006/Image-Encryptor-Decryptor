# Image Encryption and Decryption Tool

This project is a **Tkinter-based GUI application** for encrypting and decrypting images using custom keys. Built with Python and OpenCV, it allows users to load an image, apply encryption, and later decrypt it with the matching key. The project provides an interactive and user-friendly experience for image security.

## Features

- **Load and Display Images:** Users can load an image into the application to view the original before encryption.
- **Image Encryption with Key:** Encrypts images by applying a randomly generated key, transforming the image and securing its contents.
- **Decryption with Matching Key:** Ensures only users with the correct key can successfully decrypt and restore the original image.
- **Image Reset and Save Options:** Users can reset the image to its original state or save the encrypted image.
- **Responsive UI with Tkinter:** Uses Tkinter buttons, labels, and message dialogs for a streamlined user experience.
- **Real-Time Image Display:** Shows the original, encrypted, and decrypted images side by side, providing immediate feedback.

## How It Works

1. **Load an Image:** Use the "Choose" button to select an image file, which is resized for uniform display.
2. **Encryption:** Click the "Encrypt" button, and the program prompts for a unique encryption key, then encrypts the image. The encrypted version appears on the right.
3. **Decryption:** Click the "Decrypt" button, enter the correct decryption key, and the image will be decrypted if the keys match.
4. **Reset and Save Options:** Reset the image to its original state or save the encrypted image for future use.
5. **Exit Program:** Click "EXIT" to close the application safely.

## Libraries and Tools Used

- **Tkinter**: For the graphical user interface (GUI).
- **OpenCV**: For image processing operations.
- **PIL (Pillow)**: For handling image display and conversion within Tkinter.
- **NumPy**: For mathematical operations required during encryption and decryption.

## Screenshots

- **Original and Encrypted Image Side by Side**
- **Encryption Key Prompt**
- **Decryption Key Prompt**

## Installation and Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/image-encryption-decryption.git
    ```

2. **Install Required Libraries**:
    ```bash
    pip install opencv-python pillow numpy
    ```

3. **Run the Application**:
    ```bash
    python main.py
    ```

## Usage Instructions

1. **Choose Image**: Click "Choose" to select an image file.
2. **Encrypt Image**: Enter an encryption key when prompted to secure the image.
3. **Decrypt Image**: Use the correct key to reveal the original image.
4. **Save Image**: Click "Save" to save the encrypted image file.
5. **Reset Image**: Reset to the original view.
6. **Exit**: Click "EXIT" to close the app.

## Future Enhancements

- **Different Encryption Algorithms**: Experiment with other encryption techniques for enhanced security.
- **Advanced Image Processing**: Add color support and additional transformations.
- **Additional UI Enhancements**: Improve layout and design for better usability.


---

Give it a try, and secure your images with ease!
