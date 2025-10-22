def swap_bytes(data):
    # Split the data into chunks of 4 bytes each
    chunks = [data[i:i+4] for i in range(0, len(data), 4)]
    
    # Swap the byte order of each chunk
    swapped_chunks = [chunk[::-1] for chunk in chunks]
    
    # Concatenate the swapped chunks back together
    swapped_data = b''.join(swapped_chunks)
    
    return swapped_data

def main():
    input_file = input("Enter the path to the JPEG file: ")

    # Read the contents of the input file
    with open(input_file, 'rb') as f:
        jpeg_data = f.read()

    # Perform the byte order transformation
    modified_jpeg_data = swap_bytes(jpeg_data)

    # Write the modified data to a new file
    output_file = input("Enter the path for the modified JPEG file: ")
    with open(output_file, 'wb') as f:
        f.write(modified_jpeg_data)

    print("Transformation complete. Modified JPEG file saved as", output_file)

if __name__ == "__main__":
    main()
