# App Store Optimization (ASO) Metadata Localization Script

The `generate_aso_metadata.py` script automates the generation of App Store titles, subtitles, and keywords into multiple languages tailored specifically for the "Active Language Learner" persona using Google's Gemini LLM.

## Prerequisites

Before running the script, ensure you have the required Python dependencies installed.

```bash
pip install pydantic "google-genai>=0.2.0"
```

You will also need a valid Google Gemini API Key. You can obtain one from the [Google AI Studio](https://aistudio.google.com/).

## Usage

To run the script, use the following command from the root of the project:

```bash
python scripts/generate_aso_metadata.py --api-key "YOUR_GEMINI_API_KEY"
```

### Arguments

*   `--api-key`: **(Required)** Your Google Gemini API Key.

## How It Works

1.  The script takes a base English metadata set (Title, Subtitle, Keywords) configured inside the script (`ENGLISH_METADATA`).
2.  It iterates over a predefined list of high-value App Store languages (`LANGUAGES`), such as Spanish, Simplified Chinese, Japanese, Portuguese, Korean, and French.
3.  For each language, it prompts the Gemini language model to translate and optimize the metadata, strictly adhering to App Store ASO limits:
    *   **Title**: Max 30 characters
    *   **Subtitle**: Max 30 characters
    *   **Keywords**: Max 100 characters (comma-separated, no spaces)
4.  The generated output is validated, and any limits that exceed App Store constraints are flagged in the console.
5.  Validated JSON files are saved in the `localized_metadata/` directory at the project root for each target language.

## Modifying the Script

If you update the English metadata for "Word Hype", you must update the `ENGLISH_METADATA` dictionary directly at the top of the `scripts/generate_aso_metadata.py` script.

To add new languages to target, add them to the `LANGUAGES` dictionary within the script utilizing the standard iOS locale identifiers (e.g., `"German": "de-DE"`).
