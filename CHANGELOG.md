# Changelog

All notable changes to this project will be documented in this file. This project adheres to [semantic versioning].

## [Unreleased]

### Fixed

- The `decode` function no longer returns incorrect coordinates when decoding negative values (see [commit `d8b63823`]).

### Added

- Further tests for the `polyline_round` function
- Tests for when encoding and decoding coordinates using a non-default precision

### Changed

- Store the default precision of floating-point numbers in a module-level constant named `DEFAULT_PRECISION`

## [0.1.0] — 2019-03-18

Initial release.


  [Unreleased]: https://github.com/JaGallup/encpoly/compare/v0.1.0...HEAD
  [0.1.0]: https://github.com/JaGallup/encpoly/releases/tag/v0.1.0

  [semantic versioning]: https://semver.org/
  [commit `d8b63823`]: https://github.com/JaGallup/encpoly/commit/d8b63823623303e089033468b20541bfa2a7d608
