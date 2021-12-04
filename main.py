import random
import string
from datetime import datetime
# Other option for generating keys
# import shortuuid

# Characters to be used for key generation (letters from a-z, numbers from 0-9)
alphabet = string.ascii_lowercase + string.digits
# Length of key to generate
key_length = 8

def main():
    # Function to create a random string of letters and numbers using the alphabet and length provided above
    def generate_key():
        return ''.join(random.choices(alphabet, k=8))

    # Grab current date/time, format it, and save to variable
    date_and_time = datetime.now().strftime('%m-%d-%Y %H:%M:%S')
    # Open gift_keys.txt file using a context manager
    with open('gift_keys.txt', 'a') as f:
        # Write formatted current date and time
        f.write('-----------------------\n')
        f.write(f'| {date_and_time} |\n')
        f.write('-----------------------\n')
        # Generate and write 10 keys on separate lines
        for _ in range(10):
            gift_key = generate_key()
            f.write(f'{gift_key}\n')

    while True:
        print('Keys generated.')
        input('Press any key or close window to exit.')
        break
    
if __name__ == '__main__':
    main()