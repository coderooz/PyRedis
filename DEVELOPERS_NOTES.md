# Developers Notes

This document provides technical details and guidance for developers working on PyRedis.

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [Code Structure](#code-structure)
3. [Key Classes](#key-classes)
4. [Data Flow](#data-flow)
5. [Persistence Mechanism](#persistence-mechanism)
6. [TTL Implementation](#ttl-implementation)
7. [CLI Implementation](#cli-implementation)
8. [Error Handling](#error-handling)
9. [Performance Considerations](#performance-considerations)
10. [Extension Points](#extension-points)
11. [Testing Strategy](#testing-strategy)
12. [Known Limitations](#known-limitations)
13. [Future Improvements](#future-improvements)
14. [Development Setup](#development-setup)
15. [Code Style Guide](#code-style-guide)

---

## Architecture Overview

PyRedis follows a **single-file architecture** with two main classes:

```
┌─────────────────────────────────────┐
│           PyRedis CLI               │
│  (User Interface Layer)             │
├─────────────────────────────────────┤
│           PyRedis Core              │
│  (Business Logic Layer)             │
├─────────────────────────────────────┤
│         Data Persistence            │
│  (JSON File Storage)                │
└─────────────────────────────────────┘
```

### Design Principles

1. **Simplicity**: Single file, minimal dependencies
2. **Educational**: Clear, readable code for learning
3. **Redis-inspired**: Mimics Redis commands and behavior
4. **Self-contained**: No external dependencies required

---

## Code Structure

The entire application is contained in `pyredis.py`:

```python
# pyredis.py

# Imports
import time
import json
import os
import sys

# Core Storage Class
class PyRedis:
    # Key-value store with TTL support
    pass

# CLI Interface Class
class PyRedisCLI:
    # Command-line interface
    pass

# Entry Point
if __name__ == "__main__":
    # CLI execution
    pass
```

---

## Key Classes

### PyRedis Class

**Purpose**: Core key-value store with TTL and persistence

**Attributes**:
- `store`: Dictionary for key-value pairs
- `expirations`: Dictionary for TTL timestamps
- `auto_save_enabled`: Boolean flag for auto-save
- `expiration_time`: Default TTL in seconds
- `verbose`: Boolean flag for print statements

**Methods**:
- `set(*key_values, ttl=None)`: Set key-value pairs
- `get(key)`: Get value by key
- `delete(key)`: Delete a key
- `save(filename)`: Save to JSON file
- `load(filename)`: Load from JSON file
- `enable_auto_save()`: Enable auto-save
- `disable_auto_save()`: Disable auto-save
- `_is_expired(key)`: Check if key is expired (internal)

### PyRedisCLI Class

**Purpose**: Command-line interface for user interaction

**Attributes**:
- `redis`: PyRedis instance
- `savefile_path`: Path to JSON file

**Methods**:
- `run()`: Main CLI loop
- Command parsing and execution

---

## Data Flow

### SET Operation
```
User Input → CLI Parser → PyRedis.set() → In-Memory Storage → Auto-Save (optional)
```

### GET Operation
```
User Input → CLI Parser → PyRedis.get() → Expiration Check → Return Value
```

### SAVE Operation
```
User Input → CLI Parser → PyRedis.save() → JSON Serialization → File Write
```

### LOAD Operation
```
User Input → CLI Parser → PyRedis.load() → File Read → JSON Deserialization → In-Memory Storage
```

---

## Persistence Mechanism

### JSON File Structure

```json
{
  "store": {
    "key1": "value1",
    "key2": "value2",
    "nested_key": "complex_value"
  },
  "expirations": {
    "key1": 1694160000.0,
    "key2": 1694160000.0
  }
}
```

### Save Process

1. Convert `store` and `expirations` dictionaries to JSON
2. Write to file (default: `pyredis_dump.json`)
3. Handle file write errors gracefully

### Load Process

1. Check if file exists
2. Read JSON file
3. Parse JSON to dictionaries
4. Update `store` and `expirations` attributes
5. Handle file not found gracefully

### Auto-Save Behavior

- Triggered on `set()` and `delete()` operations
- Can be enabled/disabled via `enable_auto_save()` and `disable_auto_save()`
- Default state: enabled

---

## TTL Implementation

### Time Calculation

```python
def set(self, *key_values, ttl=None):
    for kv in key_values:
        key, value = kv.split()
        self.store[key] = value
        if ttl is None:
            ttl = self.expiration_time
        self.expirations[key] = time.time() + ttl
```

### Expiration Check

```python
def _is_expired(self, key):
    if key not in self.expirations:
        return False
    return time.time() > self.expirations[key]
```

### Lazy Expiration

- Expiration is checked on `get()` operations
- Expired keys are deleted when accessed
- No background cleanup process

### Default TTL

- Default: 1 year (31536000 seconds)
- Configurable via `expiration_time` parameter
- Can be overridden per key with `ttl` parameter

---

## CLI Implementation

### Command Parsing

```python
def run(self):
    while True:
        input_str = input("pyredis> ").strip()
        parts = input_str.split(' ', 1)
        cmd = parts[0].upper()
        cmd_vals = parts[1] if len(parts) > 1 else ""
        
        # Command execution...
```

### Supported Commands

| Command | Syntax | Description |
|---------|--------|-------------|
| SET | `SET key value` | Set a key-value pair |
| SET | `SET key1 value1, key2 value2, ..., ttl` | Set multiple pairs with TTL |
| GET | `GET key` | Get value by key |
| DELETE | `DELETE key` | Delete a key |
| SAVE | `SAVE` | Save to file |
| LOAD | `LOAD` | Load from file |
| ENABLE_AUTOSAVE | `ENABLE_AUTOSAVE` | Enable auto-save |
| DISABLE_AUTOSAVE | `DISABLE_AUTOSAVE` | Disable auto-save |
| EXIT | `EXIT` | Exit CLI |

### Input Handling

- Uppercase command matching
- Space-separated arguments
- Comma-separated multiple values
- Optional TTL as last argument
- Empty input handling

---

## Error Handling

### Command Errors

```python
except ValueError:
    print(f"Error: Invalid format for key-value pair '{kv}'.")
```

### File Errors

```python
except FileNotFoundError:
    print(f"No existing data found in {filename}")
```

### General Errors

```python
except Exception as e:
    print(f"Error: {e}")
```

### Error Types

1. **ValueError**: Invalid key-value format
2. **FileNotFoundError**: Missing save file
3. **JSONDecodeError**: Corrupted save file
4. **Exception**: General errors

---

## Performance Considerations

### Memory Usage

- In-memory storage for all key-value pairs
- Expiration timestamps stored separately
- No memory optimization (educational purpose)

### Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| SET | O(1) |
| GET | O(1) |
| DELETE | O(1) |
| SAVE | O(n) |
| LOAD | O(n) |

### File I/O

- JSON serialization/deserialization on every save/load
- No batching or caching
- No compression

---

## Extension Points

### Adding New Commands

1. Add command handler in `PyRedisCLI.run()` method
2. Implement corresponding method in `PyRedis` class (if needed)
3. Update documentation

### Adding Data Types

1. Extend `PyRedis` class with new data structures
2. Add serialization support for new types
3. Update CLI commands

### Adding Network Support

1. Add socket server functionality
2. Implement protocol handling
3. Add authentication

### Adding Persistence Options

1. Add RDB (Redis Database) format support
2. Add AOF (Append-Only File) support
3. Add compression options

---

## Testing Strategy

### Manual Testing

1. **Basic Operations**
   - SET single key-value pair
   - GET existing key
   - DELETE existing key

2. **Edge Cases**
   - SET with invalid format
   - GET non-existing key
   - DELETE non-existing key

3. **Persistence**
   - SAVE to file
   - LOAD from file
   - SAVE and LOAD round-trip

4. **TTL**
   - SET with custom TTL
   - GET expired key
   - Check expiration behavior

5. **Auto-Save**
   - ENABLE_AUTOSAVE
   - DISABLE_AUTOSAVE
   - Test auto-save on operations

### Test Commands

```bash
# Run application
python pyredis.py

# Test SET
pyredis> SET name John
pyredis> SET age 25, city New York

# Test GET
pyredis> GET name
pyredis> GET age

# Test DELETE
pyredis> DELETE name
pyredis> GET name

# Test SAVE/LOAD
pyredis> SAVE
pyredis> LOAD

# Test TTL
pyredis> SET temp_key temp_value 10
pyredis> GET temp_key
# Wait 10 seconds
pyredis> GET temp_key

# Test auto-save
pyredis> DISABLE_AUTOSAVE
pyredis> SET test_key test_value
pyredis> EXIT
# Check if pyredis_dump.json was updated
```

---

## Known Limitations

### Single-File Architecture

- All code in one file
- No module separation
- Limited code organization

### Persistence Limitations

- JSON-only storage
- No encryption
- No compression
- No concurrent access

### Performance Limitations

- In-memory only
- No indexing
- No querying
- No clustering

### Security Limitations

- No authentication
- No authorization
- No input sanitization
- No encryption

---

## Future Improvements

### Short-term

1. Add more Redis-like commands (MGET, MSET, INCR, DECR)
2. Add data type support (lists, sets, hashes)
3. Add expiration events/notifications
4. Add input validation

### Medium-term

1. Add network server capability
2. Add client-server architecture
3. Add authentication
4. Add data encryption

### Long-term

1. Add persistence options (RDB, AOF)
2. Add clustering support
3. Add pub/sub functionality
4. Add scripting support

---

## Development Setup

### Prerequisites

- Python 3.x
- Git (for version control)

### Setup Steps

```bash
# Clone repository
git clone https://github.com/coderooz/PyRedis.git
cd PyRedis

# Create virtual environment (optional)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Run application
python pyredis.py
```

### Development Commands

```bash
# Run application
python pyredis.py

# Run with custom save file
python pyredis.py mydata.json

# Run with custom expiration time (seconds)
python pyredis.py mydata.json 86400

# Run Python linter
python -m py_compile pyredis.py

# Run type checker (optional)
mypy pyredis.py
```

---

## Code Style Guide

### PEP 8 Compliance

- 4 spaces indentation
- 79 character line limit
- Two blank lines before function/class definitions
- One blank line after method definitions

### Naming Conventions

- Classes: `PascalCase` (e.g., `PyRedis`, `PyRedisCLI`)
- Methods: `snake_case` (e.g., `set`, `get`, `delete`)
- Variables: `snake_case` (e.g., `key_value_pairs`, `expiration_time`)
- Constants: `UPPER_CASE` (e.g., `DEFAULT_EXPIRATION_TIME`)

### Docstrings

```python
def method_name(self, param1, param2):
    """
    Brief description of the method.
    
    :param param1: Description of param1
    :param param2: Description of param2
    :return: Description of return value
    """
    pass
```

### Comments

- Use comments to explain complex logic
- Avoid obvious comments
- Keep comments up-to-date

---

## Debugging Tips

### Common Issues

1. **KeyError**: Key doesn't exist in store
   - Check if key was set correctly
   - Check if key expired

2. **FileNotFoundError**: Save file not found
   - Check file path
   - Create file with SAVE command

3. **JSONDecodeError**: Corrupted save file
   - Delete or fix the JSON file
   - Start fresh

### Debug Mode

```python
# Add debug prints
print(f"DEBUG: store = {self.store}")
print(f"DEBUG: expirations = {self.expirations}")
```

### Logging

```python
# Add logging
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.debug(f"SET operation: key={key}, value={value}")
```

---

## Contributing Guidelines

### Code Contributions

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

### Documentation Contributions

1. Fix typos
2. Add examples
3. Improve explanations
4. Update outdated information

### Bug Reports

1. Describe the issue
2. Provide steps to reproduce
3. Include error messages
4. Suggest fixes (if any)

---

## Contact

- **Author**: Ranit Saha (@coderooz)
- **Email**: contact@coderooz.in
- **GitHub**: https://github.com/coderooz/PyRedis

---

*Last updated: 2026-09-08*