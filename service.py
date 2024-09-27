import time
import requests
from datetime import datetime
import getmac

# Function to send RFID tag data to the API
def send_rfid_data(tag_id):
    print(f"RFID Tag Scanned: {tag_id}")

    # Simulate visual feedback (e.g., LED)
    # led.on()  # Uncomment if using a real LED
    time.sleep(1)  # Keep the LED on for a moment
    # led.off()  # Uncomment if using a real LED

    # Prepare the data to send to the API
    data = {
        'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'card_no': tag_id,
        'device_sn': getmac.get_mac_address(),  # Replace with actual device serial number
        'device_name': 'test',  # Replace with actual device name
        'event_point_name': "Attendance_record"  # Replace with actual event point name
    }

    # Headers for the API request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Send the POST request to the API
    try:
        response = requests.post('https://megasolutions.microlent.com/localtest/test.php', data=data, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(f"Successfully sent RFID Tag: {tag_id} to the API")
        print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send RFID Tag: {tag_id} to the API. Error: {e}")


# Main loop to simulate RFID scanning
def main():
    while True:
        # Simulating RFID tag reading (replace with actual RFID reading logic)
        tag_id = input("Scan RFID card (Enter RFID number): ")

        if tag_id:
            send_rfid_data(tag_id)
        else:
            print("No RFID number entered. Please scan again.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
