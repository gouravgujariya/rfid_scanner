import csv
import os  # Import os to check file existence
import time
from gpiozero import LED

# Set up the LED (or buzzer) for visual feedback
led = LED(19)


# Function to read RFID tags and store them in dataset.csv
def read_rfid_tag(tag_id):
    print(f"RFID Tag Scanned: {tag_id}")
    led.on()  # Turn on the LED
    time.sleep(1)  # Keep the LED on for a moment
    led.off()  # Turn off the LED

    # Check if dataset.csv exists, create it if not
    file_exists = os.path.isfile('dataset.csv')

    # Append the scanned RFID tag to the dataset.csv file
    with open('dataset.csv', mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['RFid'])  # Write header if the file is newly created
        writer.writerow([tag_id])  # Write the RFID tag as a new row
    print(f"Stored RFID Tag: {tag_id} in dataset.csv")


# Main loop to simulate RFID scanning
def main():
    while True:
        # Simulating RFID tag reading (replace with actual RFID reading logic)
        tag_id = input("Scan RFID card (Enter RFID number): ")

        if tag_id:
            read_rfid_tag(tag_id)
        else:
            print("No RFID number entered. Please scan again.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
