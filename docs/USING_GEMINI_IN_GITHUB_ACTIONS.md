# Using GEMINI_API_KEY in GitHub Actions

## Quick Start

You've already set up `GEMINI_API_KEY` as a repository secret - great! Here's how to use it:

### Option 1: Create a GitHub Actions Workflow (Recommended)

Create a new workflow file to run the evolution system with Gemini:

**.github/workflows/evolution-cycle-gemini.yml**

```yaml
name: Evolution Cycle with Gemini AI

on:
  workflow_dispatch:
    inputs:
      n_suggestions:
        description: 'Number of refinement suggestions to generate'
        required: false
        default: '5'
      use_gemini:
        description: 'Use Gemini AI (true/false)'
        required: false
        default: 'true'

permissions:
  contents: read

jobs:
  evolution-cycle:
    name: Run Evolution Cycle
    runs-on: ubuntu-latest
    timeout-minutes: 30
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          # Pin versions for supply chain security
          pip install mpmath==1.3.0 numpy==2.0.0 scipy==1.13.1
          pip install google-genai==0.3.0
      
      - name: Run Evolution Cycle with Gemini
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: |
          python3 demo_evolution_cycle.py
          
          # Also test Gemini advisor directly
          python3 evolution_system/gemini_advisor.py
      
      - name: Upload results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: evolution-cycle-results
          path: outputs/evolution_system/*.json
          retention-days: 30
```

Then run it from:
- **GitHub UI:** Actions tab → "Evolution Cycle with Gemini AI" → Run workflow
- **GitHub CLI:** `gh workflow run evolution-cycle-gemini.yml`

### Option 2: Test Locally with Secret Access

If you want to test locally, you need to:

1. **Get your actual API key value** from Google AI Studio
2. **Set it locally:**
   ```bash
   export GEMINI_API_KEY='your-actual-api-key-value'
   ```
3. **Run the script:**
   ```bash
   python3 evolution_system/gemini_advisor.py
   ```

**Note:** GitHub secrets are NOT accessible in local development or Copilot sessions. They only work in GitHub Actions workflows.

### Option 3: Integrate Gemini into Existing Workflows

Add to any existing workflow:

```yaml
- name: Run with Gemini
  env:
    GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
  run: |
    python3 your_script.py
```

## Quick Test

To verify your secret is working, create this simple workflow:

**.github/workflows/test-gemini.yml**

```yaml
name: Test Gemini Connection

on:
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install and test
        env:
          GEMINI_API_KEY: ${{ secrets.GEMINI_API_KEY }}
        run: |
          # Pin versions for supply chain security
          pip install google-genai==0.3.0 mpmath==1.3.0 numpy==2.0.0 scipy==1.13.1
          
          # Quick test
          python3 << 'EOF'
          import os
          from evolution_system.gemini_advisor import GeminiAIAdvisor
          
          advisor = GeminiAIAdvisor()
          if advisor.client:
              print("✅ Gemini connected successfully!")
          else:
              print("❌ Gemini not available")
          EOF
```

Run this to verify the secret works!

## Important Notes

1. **GitHub Secrets** only work in GitHub Actions workflows
2. **Local development** requires setting the environment variable manually
3. **Copilot sessions** cannot access GitHub secrets (security feature)
4. The secret value is hidden in workflow logs for security

## What You've Already Got

✅ Secret `GEMINI_API_KEY` is set up in your repository  
✅ Code is ready to use it (`evolution_system/gemini_advisor.py`)  
✅ Fallback mode works without the key

## Next Steps

1. Create `.github/workflows/evolution-cycle-gemini.yml` (see template above)
2. Go to Actions tab
3. Run "Evolution Cycle with Gemini AI" workflow
4. Check the logs to see Gemini in action!

The secret will automatically be available as `${{ secrets.GEMINI_API_KEY }}` in any workflow you create.
