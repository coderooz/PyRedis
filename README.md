# PyRedis

A simple, in-memory key-value store inspired by Redis, designed for educational purposes. PyRedis supports basic key-value operations, expiration times (TTL), and automatic saving/loading of data from a JSON file.

## Features

- Set key-value pairs with optional TTL (time-to-live)
- Get values by key, with automatic expiration handling
- Delete keys
- Auto-save and load data from a JSON file
- Command-line interface for easy interaction

## Requirements

- Python 3.x

## Installation

To get started with PyRedis, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/coderooz/PyRedis.git
cd PyRedis
```

You can also download the repository as a ZIP file and extract it.

## Usage

### Running the CLI

To run the PyRedis command-line interface, execute:

```bash
python pyredis.py
```

### Commands

The following commands are available in the CLI:

- **SET**: Set a key-value pair. Optionally, specify a TTL (in seconds).
  ```bash
  SET key value
  SET key1 value1, key2 value2, ..., ttl
  ```

- **GET**: Retrieve the value of a key.
  ```bash
  GET key
  ```

- **DELETE**: Remove a key from the store.
  ```bash
  DELETE key
  ```

- **SAVE**: Save the current data to a JSON file.
  ```bash
  SAVE
  ```

- **LOAD**: Load data from a JSON file.
  ```bash
  LOAD
  ```

- **ENABLE_AUTOSAVE**: Enable automatic saving of data.
  ```bash
  ENABLE_AUTOSAVE
  ```

- **DISABLE_AUTOSAVE**: Disable automatic saving of data.
  ```bash
  DISABLE_AUTOSAVE
  ```

- **EXIT**: Exit the CLI.
  ```bash
  EXIT
  ```

### Example

Here's an example of using the PyRedis CLI:

```bash
pyredis> SET country USA
SET country = USA
pyredis> GET country
GET country = USA
pyredis> DELETE country
DELETE country
pyredis> GET country
GET country = None
```

## Configuration

You can customize the following parameters in the `PyRedisCLI` class:

- **savefile_path**: Path to the JSON file for saving/loading data (default is `pyredis_dump.json`).
- **expiration_time**: Default TTL for keys in seconds (default is 1 year).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to improve the project.

## Acknowledgements

This project is inspired by Redis and is meant for educational purposes to understand key-value storage mechanisms.
