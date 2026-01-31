# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Tools & infrastructure reflection page added to documentation website (`tools_infrastructure.qmd`) and linked in navbar.  
- Example output added to tutorial / vignette for clearer function usage.  
- Additional entries added to the `CHANGELOG.md` file to improve release tracking.  
- Docstrings added to unit tests, including:
  - `test_missing_summary`
  - `test_handle_missing`
  - other test functions for improved documentation clarity.

### Changed
- README badges updated to use **dynamic versioning**.  
- `publish.yml` modified to support dynamic semantic versioning for releases.  
- `pyproject.toml` updated for dynamic versioning and TestPyPI release workflow.  
- Documentation structure cleaned and improved (README, examples, batch fixes).  
- Build workflow updated to generate a **preview deployment** for the docs website.  
- Landing page of documentation website improved and fixed.  

### Fixed
- Fixed badge rendering in README.  
- Fixed documentation website landing page layout.  
- Removed unnecessary Quarto-generated files from the repository.  

### CI / Infrastructure
- Dev → main branch sync workflow completed.  
- Development branch merged into main following staging workflow.  
- GitHub Actions workflows updated to:
  - run `pytest` with coverage  
  - run `ruff` lint checks  
  - build Quartodoc reference  
  - render Quarto documentation  
  - deploy documentation previews  
  - publish package to TestPyPI via automated pipeline  



## [0.1.0] - (1979-01-01)

- First release
