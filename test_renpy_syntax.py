#!/usr/bin/env python3
"""
Basic syntax validation test for Ren'Py scripts.
This script checks for common issues in .rpy files without requiring full Ren'Py installation.
"""

import os
import re
import sys
from pathlib import Path


class RenpyValidator:
    """Validates Ren'Py script files for common syntax issues."""

    def __init__(self, game_dir):
        self.game_dir = Path(game_dir)
        self.errors = []
        self.warnings = []

    def validate_all(self):
        """Validate all .rpy files in the game directory."""
        rpy_files = list(self.game_dir.glob("**/*.rpy"))

        if not rpy_files:
            self.errors.append(f"No .rpy files found in {self.game_dir}")
            return False

        print(f"Found {len(rpy_files)} .rpy files to validate\n")

        for rpy_file in rpy_files:
            print(f"Validating: {rpy_file.relative_to(self.game_dir)}")
            self.validate_file(rpy_file)

        return len(self.errors) == 0

    def validate_file(self, filepath):
        """Validate a single .rpy file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')

            # Check for common issues
            self.check_dialogue_brackets(filepath, lines)
            self.check_indentation(filepath, lines)
            self.check_label_definitions(filepath, lines)
            self.check_menu_syntax(filepath, lines)
            self.check_character_definitions(filepath, lines)

        except Exception as e:
            self.errors.append(f"{filepath}: Error reading file - {e}")

    def check_dialogue_brackets(self, filepath, lines):
        """
        Check for unescaped brackets in dialogue lines.
        Ren'Py treats [...] as interpolation, which can cause syntax errors.
        """
        in_dialogue = False
        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # Skip comments
            if stripped.startswith('#'):
                continue

            # Check for dialogue lines (character speaking)
            # Pattern: character "dialogue" or just "dialogue"
            if re.match(r'^[a-z]\s+"', stripped) or stripped.startswith('"'):
                # Check for unescaped brackets in dialogue
                if '[' in stripped and ']' in stripped:
                    # Check if it's actually in the quoted part
                    quote_match = re.search(r'"([^"]*)"', stripped)
                    if quote_match:
                        dialogue_text = quote_match.group(1)
                        if '[' in dialogue_text and not '[[' in dialogue_text:
                            self.warnings.append(
                                f"{filepath}:{i}: Potential Ren'Py interpolation in dialogue: {stripped[:60]}..."
                            )

    def check_indentation(self, filepath, lines):
        """Check for inconsistent indentation."""
        prev_indent = 0
        for i, line in enumerate(lines, 1):
            if not line.strip() or line.strip().startswith('#'):
                continue

            # Count leading spaces
            indent = len(line) - len(line.lstrip(' '))

            # Ren'Py typically uses 4-space indentation
            if indent % 4 != 0 and line.lstrip():
                self.warnings.append(
                    f"{filepath}:{i}: Non-standard indentation (not multiple of 4 spaces)"
                )

    def check_label_definitions(self, filepath, lines):
        """Check label definitions for common issues."""
        labels = set()

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # Check for label definition (navigation label, not UI property)
            # UI labels in screens don't have colons, so we need to differentiate
            if stripped.startswith('label ') and stripped.endswith(':'):
                label_match = re.match(r'label\s+(\w+)\s*:', stripped)
                if label_match:
                    label_name = label_match.group(1)
                    if label_name in labels:
                        self.errors.append(
                            f"{filepath}:{i}: Duplicate label definition: {label_name}"
                        )
                    labels.add(label_name)

    def check_menu_syntax(self, filepath, lines):
        """Check menu blocks for proper syntax."""
        in_menu = False

        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            if stripped == 'menu:':
                in_menu = True
            elif in_menu and stripped and not stripped.startswith('"') and not stripped.startswith('#'):
                # Menu should be followed by quoted options or jump statements
                if not any(keyword in stripped for keyword in ['jump', 'return', 'pass', 'python']):
                    if stripped.endswith(':') and not stripped.startswith('"'):
                        pass  # This is a menu option
                    elif not stripped.startswith('label'):
                        # Reset menu state if we hit a new block
                        in_menu = False

    def check_character_definitions(self, filepath, lines):
        """Check character definitions."""
        for i, line in enumerate(lines, 1):
            stripped = line.strip()

            # Check for character definition
            if stripped.startswith('define ') and 'Character(' in stripped:
                # Basic check for matching quotes
                if stripped.count('"') % 2 != 0 and stripped.count("'") % 2 != 0:
                    self.errors.append(
                        f"{filepath}:{i}: Mismatched quotes in character definition"
                    )

    def print_results(self):
        """Print validation results."""
        print("\n" + "="*70)
        print("VALIDATION RESULTS")
        print("="*70 + "\n")

        if self.errors:
            print(f"❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  {error}")
            print()

        if self.warnings:
            print(f"⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  {warning}")
            print()

        if not self.errors and not self.warnings:
            print("✅ All checks passed! No issues found.")
            print()

        print(f"Summary: {len(self.errors)} errors, {len(self.warnings)} warnings")
        print("="*70)


def main():
    """Main entry point."""
    # Determine game directory
    script_dir = Path(__file__).parent
    game_dir = script_dir / "bludiblud" / "game"

    if not game_dir.exists():
        print(f"Error: Game directory not found: {game_dir}")
        return 1

    print("="*70)
    print("Ren'Py Syntax Validator")
    print("="*70)
    print(f"Game directory: {game_dir}\n")

    validator = RenpyValidator(game_dir)
    success = validator.validate_all()
    validator.print_results()

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
