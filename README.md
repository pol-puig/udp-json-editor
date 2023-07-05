## Code Structure

* **main.py:** Thread management. It configures 2 threads and starts them. Program finishes when both threads end their execution

* **json_operators:** contains all required classes and methods for proper json handling.

* **udp_client:** Reads user's desired JSON file and sends it to a listening server.

* **udp_server:** Handles JSON data received from a UDP connection depending on user choices.

* **console_interface.py:** Shows in console the required steps for the user to use the program. It also handles his inputs.


## Limitations

* Id uniqueness in the JSON file is not checked and not using integers as their value make the system crash.

* The program works properly only if the JSON file follows a similar structure as the example JSON file.

* Fields can only be replaced by strings. It is still possible to represent a list as a string, for example.

## How to run

Just run main.py and follow console instructions. The program has been tested on Python 3.11 and Windows 10 OS. It is
not guaranteed to work on other configurations.