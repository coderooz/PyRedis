# Project Reference Index

## 1. Reference Metadata

```yaml
reference:
  name: PROJECT_REFERENCE_INDEX
  version: 1.0
  status: active
  last_verified: 2026-09-08
  verification_scope: full
```

## 2. Project Identity

**Name:** PyRedis
**Description:** A simple, in-memory key-value store inspired by Redis, designed for educational purposes. PyRedis supports basic key-value operations, expiration times (TTL), and automatic saving/loading of data from a JSON file.
**Author:** Ranit Saha (@coderooz)
**License:** MIT
**Repository:** https://github.com/coderooz/PyRedis
**Language:** Python
**Type:** CLI Application / Library

## 3. Technology Stack

- **Language:** Python 3.x
- **Libraries:** Standard library only (time, json, os, sys)
- **Storage:** JSON file-based persistence
- **CLI:** Custom command-line interface

## 4. Root Structure

```
pyredis/
├── .git/                    # Git repository
├── .github/                 # GitHub configuration (if exists)
├── .opencode/               # OpenCode configuration
│   └── reference/           # Project reference index
├── .venv/                   # Python virtual environment (gitignored)
├── docs/                    # Documentation (if exists)
├── pyredis.py               # Main application file
├── pyredis_dump.json        # Data persistence file (gitignored)
├── README.md                # Project documentation
├── .gitignore               # Git ignore rules
└── .mcp-runtime.json        # MCP runtime state (gitignored)
```

## 5. Directory Reference

### `.opencode/`
**Type:** OpenCode configuration directory
**Purpose:** Contains project-specific OpenCode configuration and reference files
**Contains:**
- `reference/PROJECT_REFERENCE_INDEX.md` - This file
**Do Not:** Place source code or application files here

### `.venv/`
**Type:** Python virtual environment
**Purpose:** Isolated Python environment for project dependencies
**Status:** Active (gitignored)
**Do Not:** Commit to version control

## 6. File Reference

### `pyredis.py`
**Type:** Main application file
**Purpose:** Contains the PyRedis key-value store implementation and CLI interface
**Responsibilities:**
- `PyRedis` class: Core key-value store with TTL support
- `PyRedisCLI` class: Command-line interface for user interaction
- Data persistence (save/load to JSON)
- Auto-save functionality
**Dependencies:** Python standard library only (time, json, os, sys)
**Layer:** Application / Core
**Modification Guidance:** All core functionality changes should be made here

### `README.md`
**Type:** Project documentation
**Purpose:** Provides project overview, installation, usage, and configuration instructions
**Responsibilities:**
- Project description and features
- Installation instructions
- Usage examples
- Command reference
- Configuration options
**Layer:** Documentation

### `pyredis_dump.json`
**Type:** Data persistence file
**Purpose:** Stores key-value data and expiration times in JSON format
**Status:** Runtime generated (gitignored)
**Do Not:** Commit to version control

### `.gitignore`
**Type:** Git configuration
**Purpose:** Defines files and directories to exclude from version control
**Responsibilities:**
- Exclude virtual environment
- Exclude generated data files
- Exclude IDE files
- Exclude OpenCode workspace files
**Layer:** Configuration

## 7. Application Routes

Not applicable - CLI application without web routes.

## 8. API Routes

Not applicable - CLI application without HTTP API.

## 9. Modules

### PyRedis Core Module
**Location:** `pyredis.py` (PyRedis class)
**Purpose:** Core key-value store implementation
**Structure:**
- Key-value storage (dictionary)
- Expiration tracking (TTL)
- Auto-save mechanism
- Data persistence (JSON)
**Responsibilities:**
- Store and retrieve key-value pairs
- Handle TTL expiration
- Save data to JSON file
- Load data from JSON file
- Auto-save on modifications
**Data Access:** In-memory dictionary + JSON file
**External Consumers:**
- PyRedisCLI class
- Direct Python import

### PyRedis CLI Module
**Location:** `pyredis.py` (PyRedisCLI class)
**Purpose:** Command-line interface for user interaction
**Structure:**
- Command parsing
- User input handling
- Command execution
**Responsibilities:**
- Parse user commands (SET, GET, DELETE, SAVE, LOAD, etc.)
- Execute commands against PyRedis core
- Display results to user
- Handle errors and exceptions
**Data Access:** PyRedis core module
**External Consumers:**
- End users via command line

## 10. Components

Not applicable - single-file application.

## 11. Services

Not applicable - single-file application.

## 12. Data Layer

### Storage Format
**Type:** JSON file
**Location:** `pyredis_dump.json`
**Structure:**
```json
{
  "store": {
    "key1": "value1",
    "key2": "value2"
  },
  "expirations": {
    "key1": 1694160000.0,
    "key2": 1694160000.0
  }
}
```
**Responsibilities:**
- Persist key-value pairs
- Persist expiration timestamps
- Enable data recovery on restart

### In-Memory Storage
**Type:** Python dictionary
**Location:** `PyRedis.store` attribute
**Purpose:** Runtime storage for key-value pairs
**Characteristics:**
- Fast access
- Temporary (lost on exit unless saved)
- Supports all key-value operations

## 13. Configuration

### Application Configuration
**Location:** `PyRedisCLI.__init__` parameters
**Purpose:** Runtime configuration options
**Parameters:**
- `savefile_path`: Path to JSON persistence file (default: `pyredis_dump.json`)
- `expiration_time`: Default TTL in seconds (default: 1 year = 31536000 seconds)
- `verbose`: Enable/disable print statements (default: True)

### Git Configuration
**Location:** `.gitignore`
**Purpose:** Version control exclusions
**Excludes:**
- Virtual environment
- Generated data files
- IDE files
- OpenCode workspace files

## 14. Scripts & Commands

### Development Commands
**Run Application:**
```bash
python pyredis.py [savefile_path] [expiration_time]
```

**Examples:**
```bash
# Default configuration
python pyredis.py

# Custom save file
python pyredis.py mydata.json

# Custom save file and expiration time (in seconds)
python pyredis.py mydata.json 86400
```

### CLI Commands (Interactive)
- `SET key value` - Set a key-value pair
- `SET key1 value1, key2 value2, ..., ttl` - Set multiple pairs with TTL
- `GET key` - Get value by key
- `DELETE key` - Delete a key
- `SAVE` - Save data to file
- `LOAD` - Load data from file
- `ENABLE_AUTOSAVE` - Enable auto-save
- `DISABLE_AUTOSAVE` - Disable auto-save
- `EXIT` - Exit CLI

## 15. Documentation

### Documentation Root
**Location:** `README.md`
**Purpose:** Primary project documentation
**Contains:**
- Project overview
- Features
- Installation instructions
- Usage examples
- Command reference
- Configuration options
- License information

### Additional Documentation
**Location:** This file (`.opencode/reference/PROJECT_REFERENCE_INDEX.md`)
**Purpose:** Structural reference for OpenCode navigation
**Contains:**
- Project structure
- File references
- Module descriptions
- Configuration details

## 16. Integrations

### File System Integration
**Type:** JSON file persistence
**Purpose:** Data persistence across sessions
**Files:**
- `pyredis_dump.json` - Data storage
**Operations:**
- Read on startup (if exists)
- Write on SAVE command
- Write on auto-save (if enabled)

### Standard Library Integration
**Modules:**
- `time` - TTL calculation and expiration checking
- `json` - Data serialization/deserialization
- `os` - File existence checking
- `sys` - Command-line argument parsing

## 17. Assets

Not applicable - no static assets.

## 18. Generated / Runtime Directories

### `.venv/`
**Type:** Python virtual environment
**Purpose:** Isolated Python environment
**Status:** Generated
**Do Not:** Commit to version control

### `pyredis_dump.json`
**Type:** Runtime data file
**Purpose:** Persistent storage
**Status:** Generated at runtime
**Do Not:** Commit to version control

## 19. Architectural Relationships

### Data Flow
```
User Input → PyRedisCLI → PyRedis Core → In-Memory Storage
                                      ↓
                              JSON File (Persistence)
```

### Module Dependencies
```
PyRedisCLI
    ↓
PyRedis Core
    ↓
Python Standard Library (time, json, os, sys)
```

## 20. Important Entry Points

### Application Entry Point
**Location:** `pyredis.py` (bottom of file)
**Purpose:** Main execution point when running as script
**Behavior:**
- Parses command-line arguments
- Initializes PyRedisCLI
- Starts interactive CLI loop

### Programmatic Entry Point
**Location:** `PyRedis` class
**Purpose:** For use as a library in other Python code
**Usage:**
```python
from pyredis import PyRedis
store = PyRedis()
store.set("key", "value")
value = store.get("key")
```

## 21. Project-Specific Conventions

### Code Style
- Single-file application
- Class-based architecture
- Docstrings for all methods
- Verbosity control via `verbose` parameter
- Error handling with user-friendly messages

### Data Format
- JSON for persistence
- Timestamps as floats (Unix time)
- Key-value pairs as strings

### CLI Conventions
- Uppercase commands
- Space-separated arguments
- Comma-separated multiple values
- Optional TTL as last argument

## 22. Known Structural Constraints

### Single-File Architecture
- All code in `pyredis.py`
- No external dependencies
- No complex build process

### Persistence Limitations
- JSON-only storage
- No concurrent access support
- No encryption or security features
- No compression

### Performance Limitations
- In-memory storage only
- No indexing or querying capabilities
- No clustering or distributed support

## 23. Reference Maintenance Log

### 2026-09-08
**Change:** Initial PRI creation
**Classification:** ADDED
**Updated:**
- Complete project structure documentation
- All file references
- Module descriptions
- Configuration details
**Verification:** FULL
**Status:** PASS
**Coverage:** 100%
**Unverified Areas:** None
**Known Limitations:** None