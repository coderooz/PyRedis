# PyRedis — Project Rules

## Project Identity

- **Name:** PyRedis
- **Language:** Python 3.x
- **Type:** CLI Application / Educational Key-Value Store
- **Owner:** Ranit Saha (@coderooz)
- **Repository:** https://github.com/coderooz/PyRedis

## Repository Structure

```
pyredis/
├── pyredis.py               # Main application file
├── pyredis_dump.json        # Data persistence file (gitignored)
├── README.md                # Project documentation
├── .gitignore               # Git ignore rules
├── .opencode/               # OpenCode configuration
│   └── reference/           # Project reference index
└── .venv/                   # Python virtual environment (gitignored)
```

## Development Workflow

1. Read `README.md` before making changes
2. Check `.opencode/reference/PROJECT_REFERENCE_INDEX.md` for current project state
3. Follow Python coding conventions (PEP 8)
4. Write docstrings for all public methods
5. Test changes manually via CLI
6. Commit with conventional commits: `type(scope): message`
7. Update docs when code changes
8. Generate session reports after major work

## Code Quality

- **Style:** PEP 8 (Python Enhancement Proposal 8)
- **Docstrings:** Required for all public methods
- **Type Hints:** Optional but recommended
- **Testing:** Manual testing via CLI
- **Dependencies:** Standard library only (no external dependencies)

## Project Structure Rules

### Single-File Architecture
- All code must remain in `pyredis.py`
- No external dependencies allowed
- Maintain backward compatibility

### Data Persistence
- JSON file format for persistence
- Default filename: `pyredis_dump.json`
- Auto-save feature available
- Manual SAVE/LOAD commands supported

### CLI Interface
- Uppercase commands
- Space-separated arguments
- Comma-separated multiple values
- Optional TTL as last argument in SET command

## Documentation Standards

### README.md
- Keep updated with current features
- Include usage examples
- Document all CLI commands
- Provide installation instructions

### Code Documentation
- Docstrings for all public methods
- Parameter descriptions
- Return value descriptions
- Usage examples in docstrings

## Commit Conventions

Follow conventional commits:
```
type(scope): message
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples
```
feat(core): add MGET command for multiple key retrieval
fix(ttl): correct expiration time calculation
docs(readme): update installation instructions
style(code): format according to PEP 8
refactor(cli): simplify command parsing logic
```

## Testing Guidelines

### Manual Testing
1. Run the CLI: `python pyredis.py`
2. Test SET command with various formats
3. Test GET command with existing and non-existing keys
4. Test DELETE command
5. Test SAVE and LOAD commands
6. Test TTL expiration
7. Test auto-save feature
8. Test error handling

### Test Cases
- SET single key-value pair
- SET multiple key-value pairs
- SET with custom TTL
- GET existing key
- GET non-existing key
- GET expired key
- DELETE existing key
- DELETE non-existing key
- SAVE to file
- LOAD from file
- SAVE and LOAD round-trip
- Auto-save on SET
- Auto-save on DELETE
- ENABLE_AUTOSAVE and DISABLE_AUTOSAVE
- Invalid command handling
- Invalid key-value format handling

## Security Considerations

- No authentication required (educational purpose)
- No encryption (plain JSON storage)
- No network access (local only)
- No user input sanitization beyond basic error handling

## Performance Considerations

- In-memory storage for fast access
- JSON file I/O for persistence
- No indexing or querying capabilities
- No concurrent access support
- Single-user design

## Future Enhancements (Potential)

- Add more Redis-like commands (MGET, MSET, INCR, etc.)
- Add data type support (lists, sets, hashes)
- Add pub/sub functionality
- Add expiration events
- Add persistence options (RDB, AOF)
- Add network server capability
- Add authentication
- Add data encryption

## Governance Compliance

This project follows global governance rules from `~/.config/opencode/GOVERNANCE.md`:

### Pre-Task Checklist
1. Read GOVERNANCE.md
2. Read PROJECT_WORKFLOW.md
3. Load Project Reference Index (PRI)
4. Check project AGENTS.md (this file)
5. Plan compliance

### Post-Task Checklist
1. No root-level files created
2. All reports in correct locations
3. All reports follow naming convention
4. All reports indexed
5. Workspace cleaned up
6. Documentation sets not modified

## Version Control

- **Branch:** main
- **Commit Style:** Conventional commits
- **PR Requirements:** Code review for significant changes
- **Release Strategy:** Manual tagging for releases

## Development Environment

### Requirements
- Python 3.x
- No external dependencies required

### Setup
```bash
# Clone repository
git clone https://github.com/coderooz/PyRedis.git
cd PyRedis

# Create virtual environment (optional but recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Run application
python pyredis.py
```

### IDE Configuration
- Use any Python-compatible IDE
- Follow PEP 8 style guidelines
- Enable type checking (optional)
- Configure auto-formatting (optional)