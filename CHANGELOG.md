# Changelog

All notable changes to PyRedis will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Project Reference Index (PRI) for structural documentation
- AGENTS.md with project-specific rules and conventions
- .gitignore file for proper version control
- Developers Notes documentation for future developers

### Changed
- Updated README.md with current project state
- Improved documentation structure

### Fixed
- N/A

## [1.0.0] - 2026-09-08

### Added
- Initial release of PyRedis
- Core `PyRedis` class with key-value storage
- TTL (Time-to-Live) support for key expiration
- Auto-save functionality
- Command-line interface (CLI) with interactive commands
- JSON file persistence for data storage
- Support for SET, GET, DELETE, SAVE, LOAD commands
- ENABLE_AUTOSAVE and DISABLE_AUTOSAVE commands
- Multiple key-value pair SET command with comma separation
- Optional TTL parameter for SET command
- Verbose mode for detailed output
- Error handling for invalid commands and formats

### Features
- **SET command**: Set single or multiple key-value pairs
- **GET command**: Retrieve values by key with expiration checking
- **DELETE command**: Remove keys from the store
- **SAVE command**: Manually save data to JSON file
- **LOAD command**: Manually load data from JSON file
- **ENABLE_AUTOSAVE**: Enable automatic saving on modifications
- **DISABLE_AUTOSAVE**: Disable automatic saving
- **EXIT command**: Exit the CLI
- **TTL support**: Keys expire after specified time
- **Auto-save**: Automatic persistence on data changes
- **Command-line arguments**: Custom save file and expiration time

### Technical Details
- Single-file architecture (`pyredis.py`)
- Python 3.x compatibility
- Standard library only (no external dependencies)
- JSON-based data persistence
- In-memory storage with file backup
- Class-based architecture (PyRedis, PyRedisCLI)

### Documentation
- Comprehensive README with usage examples
- Installation instructions
- Command reference
- Configuration options
- Contributing guidelines

## [0.9.0] - 2026-09-07

### Added
- Beta version with core functionality
- Basic SET/GET/DELETE operations
- TTL support
- JSON persistence

### Changed
- Refined CLI interface
- Improved error handling

## [0.8.0] - 2026-09-06

### Added
- Initial prototype
- Basic key-value storage
- Simple CLI interface

---

## Version History Summary

| Version | Date | Status | Description |
|---------|------|--------|-------------|
| 1.0.0 | 2026-09-08 | Stable | Production-ready release with full feature set |
| 0.9.0 | 2026-09-07 | Beta | Beta version with core functionality |
| 0.8.0 | 2026-09-06 | Alpha | Initial prototype |

---

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/coderooz/PyRedis/tags).

## Authors

- **Ranit Saha** - *Initial work* - [coderooz](https://github.com/coderooz)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Inspired by Redis
- Built for educational purposes
- Thanks to the open-source community