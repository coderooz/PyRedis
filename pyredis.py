import time
import json
import os
import sys


class PyRedis:
    """
    A simple Redis-like key-value store that supports TTL (time-to-live) and auto-save features.
    """

    def __init__(self, expiration_time=365 * 24 * 60 * 60, auto_save=True, verbose=True):
        """
        Initializes the PyRedis store.

        :param expiration_time: Default TTL (in seconds) for the keys.
        :param auto_save: Boolean flag to enable/disable auto-save. Default is True.
        :param verbose: Boolean flag to enable/disable print statements. Default is True.
        """
        self.store = {}
        self.expirations = {}
        self.auto_save_enabled = auto_save
        self.expiration_time = expiration_time
        self.verbose = verbose

    def set(self, *key_values, ttl=None):
        """
        Set single or multiple key-value pairs with an optional TTL.

        :param key_values: Key-value pairs to be set, e.g., ("firstname John", "lastname Doe").
        :param ttl: Time-to-live (in seconds) for the keys. Default is the instance's expiration_time.
        """
        for kv in key_values:
            try:
                key, value = kv.split(", ") if ", " in kv else kv.split()
                self.store[key] = value
                if ttl is None:
                    ttl = self.expiration_time
                self.expirations[key] = time.time() + ttl
                if self.verbose:
                    print(f"SET {key} = {value}")
            except ValueError:
                if self.verbose:
                    print(f"Error: Invalid format for key-value pair '{kv}'. Use 'key value' or 'key, value'.")

        if self.auto_save_enabled:
            self.save()

    def get(self, key):
        """
        Get the value of a key if it exists and has not expired.

        :param key: The key to retrieve.
        :return: The value associated with the key, or None if expired or does not exist.
        """
        if self._is_expired(key):
            self.delete(key)
            if self.verbose:
                print(f"GET {key}: key expired or does not exist")
            return None
        value = self.store.get(key)
        if self.verbose:
            print(f"GET {key} = {value}")
        return value

    def delete(self, key):
        """
        Deletes a key from the store.

        :param key: The key to delete.
        """
        if key in self.store:
            del self.store[key]
            if key in self.expirations:
                del self.expirations[key]
            if self.verbose:
                print(f"DELETE {key}")
        else:
            if self.verbose:
                print(f"DELETE {key}: key does not exist")

        if self.auto_save_enabled:
            self.save()

    def _is_expired(self, key):
        """
        Checks if a key has expired.

        :param key: The key to check.
        :return: True if expired, False otherwise.
        """
        if key not in self.expirations:
            return False
        return time.time() > self.expirations[key]

    def save(self, filename="pyredis_dump.json"):
        """
        Saves the current store and expiration data to a JSON file.

        :param filename: The file to save the data to.
        """
        with open(filename, "w") as f:
            data = {
                "store": self.store,
                "expirations": self.expirations
            }
            json.dump(data, f)
        if self.verbose:
            print(f"Data saved to {filename}")

    def load(self, filename="pyredis_dump.json"):
        """
        Loads store and expiration data from a JSON file.

        :param filename: The file to load data from.
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.store = data["store"]
                self.expirations = data["expirations"]
            if self.verbose:
                print(f"Data loaded from {filename}")
        except FileNotFoundError:
            if self.verbose:
                print(f"No existing data found in {filename}")

    def enable_auto_save(self):
        """
        Enables the auto-save feature.
        """
        self.auto_save_enabled = True
        if self.verbose:
            print("Auto-save enabled")

    def disable_auto_save(self):
        """
        Disables the auto-save feature.
        """
        self.auto_save_enabled = False
        if self.verbose:
            print("Auto-save disabled")


class PyRedisCLI:
    """
    Command-line interface for interacting with the PyRedis key-value store.
    """

    def __init__(self, savefile_path="pyredis_dump.json", expiration_time=365 * 24 * 60 * 60, verbose=True):
        """
        Initializes the CLI with optional save file path and expiration time.

        :param savefile_path: Path to the save file.
        :param expiration_time: Default TTL for keys.
        :param verbose: Boolean flag to enable/disable print statements in PyRedis.
        """
        self.redis = PyRedis(expiration_time, auto_save=True, verbose=verbose)
        self.savefile_path = savefile_path
        if os.path.exists(self.savefile_path):
            self.redis.load(self.savefile_path)
        else:
            if verbose:
                print(f"No save file found at {self.savefile_path}. Starting fresh.")

    def run(self):
        """
        Starts the PyRedis CLI loop.
        """
        print("Welcome to PyRedis CLI")
        while True:
            try:
                input_str = input("pyredis> ").strip()
                if not input_str:
                    continue

                # Split command and values
                parts = input_str.split(' ', 1)
                cmd = parts[0].upper()
                cmd_vals = parts[1] if len(parts) > 1 else ""

                if cmd == "SET":
                    cmd_vals = cmd_vals.strip()  # Clean any extra spaces
                    if len(cmd_vals.split(',')) >= 1:  # Minimum for one key-value pair
                        key_value_pairs = [kv.strip() for kv in cmd_vals.split(',')]
                        ttl = None
                        
                        if len(key_value_pairs) % 2 == 1:  # Check if TTL is included
                            ttl = int(key_value_pairs.pop())  # Remove TTL from key-value pairs
                        
                        self.redis.set(*key_value_pairs, ttl=ttl)
                    else:
                        print("Error: SET command requires at least two arguments (key and value).")
                elif cmd == "GET":
                    if cmd_vals:
                        self.redis.get(cmd_vals)
                    else:
                        print("Error: GET command requires a key.")
                elif cmd == "DELETE":
                    if cmd_vals:
                        self.redis.delete(cmd_vals)
                    else:
                        print("Error: DELETE command requires a key.")
                elif cmd == "SAVE":
                    self.redis.save(self.savefile_path)
                elif cmd == "LOAD":
                    self.redis.load(self.savefile_path)
                elif cmd == "ENABLE_AUTOSAVE":
                    self.redis.enable_auto_save()
                elif cmd == "DISABLE_AUTOSAVE":
                    self.redis.disable_auto_save()
                elif cmd == "EXIT":
                    print("Exiting PyRedis CLI")
                    break
                else:
                    print("Unknown command")
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    # Get command line arguments for savefile_path and expiration_time
    if len(sys.argv) > 1:
        savefile_path = sys.argv[1]
    else:
        savefile_path = "pyredis_dump.json"

    if len(sys.argv) > 2:
        expiration_time = int(sys.argv[2])
    else:
        expiration_time = 365 * 24 * 60 * 60  # Default to 1 year in seconds

    cli = PyRedisCLI(savefile_path=savefile_path, expiration_time=expiration_time)
    cli.run()
