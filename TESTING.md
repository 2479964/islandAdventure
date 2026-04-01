# Testing Guide for Island Adventure

This document describes how to test the Ren'Py visual novel game.

## Quick Test

To quickly validate the Ren'Py scripts for syntax errors:

```bash
python3 test_renpy_syntax.py
```

This will check all `.rpy` files in the `bludiblud/game` directory for:
- Unescaped brackets in dialogue (which can cause Ren'Py interpolation errors)
- Inconsistent indentation
- Duplicate label definitions
- Basic menu syntax issues
- Character definition syntax

## Test Results

The validator will output:
- ✅ **Success**: All checks passed, no issues found
- ❌ **Errors**: Critical syntax issues that will prevent the game from running
- ⚠️ **Warnings**: Potential issues that may cause problems

## Full Game Testing

For comprehensive testing, you need to run the game in Ren'Py:

1. **Install Ren'Py SDK** from https://www.renpy.org/
2. **Launch Ren'Py** and open this project
3. **Click "Launch Project"** to run the game
4. **Test all story branches** (there are 30 different endings across 5 main paths)

## Testing Checklist

### Automated Tests (via test_renpy_syntax.py)
- [x] All .rpy files have valid syntax
- [x] No unescaped brackets in dialogue
- [x] No duplicate label definitions
- [x] Character definitions are properly formatted

### Manual Testing (requires Ren'Py)
When manually testing, verify:

1. **Start screen loads correctly**
2. **All character sprites display properly**
3. **Background images load**
4. **Initial menu appears with 5 choices**
5. **Each path leads to correct sub-paths**:
   - Path A (Jet): 6 endings (A1-A6)
   - Path B (Island): 6 endings (B1-B6)
   - Path C (Tel Aviv): 6 endings (C1-C6)
   - Path D (Data Center): 6 endings (D1-D6)
   - Path E (White House VR): 6 endings (E1-E6)

## Known Issues

### Resolved Issues
- **Bracketed text in dialogue**: Fixed in PR #4. Dialogue no longer contains raw `[...]` brackets that could trigger Ren'Py interpolation errors.

## CI/CD

Currently, this project does not have automated CI/CD. To add it:

1. Create `.github/workflows/test.yml`
2. Run `test_renpy_syntax.py` on every PR
3. Optionally add Ren'Py compilation checks

## Contributing

When making changes to `.rpy` files:

1. Run `python3 test_renpy_syntax.py` before committing
2. If adding dialogue, avoid using `[...]` brackets unless you specifically want Ren'Py interpolation
3. Use `[[...]]` if you need to show literal brackets in text
4. Maintain consistent 4-space indentation
5. Test your branch manually in Ren'Py before submitting PR

## Troubleshooting

### "No .rpy files found"
- Ensure you're running the test from the repository root
- Check that `bludiblud/game/` directory exists

### "Potential Ren'Py interpolation warning"
- Check the reported line for `[text]` in dialogue
- Replace with `[[text]]` if you want literal brackets
- Remove brackets if they're not needed

### Game won't launch in Ren'Py
- Check for syntax errors using the validator
- Look at Ren'Py's error console for specific issues
- Check `errors.txt` and `traceback.txt` in the game directory
