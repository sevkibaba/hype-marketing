import os
import json
import logging
import argparse
from google import genai
from pydantic import BaseModel, Field

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Target languages based on top App Store populations / revenue aside from English
LANGUAGES = {
    "Spanish (Mexico)": "es-MX",       # Huge LATAM / Spain population
    "Chinese (Simplified)": "zh-Hans", # Massive population, massive iOS market
    "Japanese": "ja",                  # Top 3 App Store Revenue market
    "Portuguese (Brazil)": "pt-BR",    # Massive and highly engaged mobile market
    "Korean": "ko",                    # High ARPU market
    "French": "fr-FR"                  # Major European / African market
}

ENGLISH_METADATA = {
    "title": "Word Hype: English Vocabulary",
    "subtitle": "Learn offline, IELTS & TOEFL",
    "keywords": "learn,english,ESL,IELTS,TOEFL,dictionary,flashcard,anki,offline,study,context,quizlet,builder,words"
}

OUTPUT_DIR = "localized_metadata"

class AppStoreMetadata(BaseModel):
    title: str = Field(description="Max 30 chars. App title.")
    subtitle: str = Field(description="Max 30 chars. App subtitle.")
    keywords: str = Field(description="Max 100 chars. Comma-separated keywords without spaces.")

def generate_metadata_for_language(client, language_name, locale_code):
    prompt = f"""
    You are an expert App Store Optimization (ASO) marketer.
    Translate, localize, and optimize the following English App Store metadata into {language_name} ({locale_code}).
    
    CRITICAL CONSTRAINTS (iOS App Store Limits):
    - App Title: MUST be maximum 30 characters.
    - Subtitle: MUST be maximum 30 characters.
    - Keyword String: MUST be exactly 100 characters maximum, comma-separated with NO spaces after commas.
    
    Original English Metadata:
    Title: {ENGLISH_METADATA['title']}
    Subtitle: {ENGLISH_METADATA['subtitle']}
    Keywords: {ENGLISH_METADATA['keywords']}
    
    Focus on targeting the "Active Language Learner" persona seeking to improve their English skills (e.g., IELTS, TOEFL, vocabulary building).
    Ensure the localized terms have high search volume in {language_name}.
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={
                'response_mime_type': 'application/json',
                'response_schema': AppStoreMetadata,
                'temperature': 0.2, # Low temperature for factual translation
            },
        )
        return response.text
    except Exception as e:
        logging.error(f"Error generating content for {language_name}: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate ASO metadata for multiple languages.")
    parser.add_argument("--api-key", required=True, help="Gemini API Key")
    args = parser.parse_args()

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    try:
        client = genai.Client(api_key=args.api_key)
    except Exception as e:
        logging.error(f"Failed to initialize Gemini client: {e}")
        return

    for lang_name, locale_code in LANGUAGES.items():
        logging.info(f"Generating ASO metadata for {lang_name} ({locale_code})...")
        metadata_json_str = generate_metadata_for_language(client, lang_name, locale_code)
        
        if metadata_json_str:
            try:
                metadata = json.loads(metadata_json_str)
                
                # Double-verify lengths
                if len(metadata['title']) > 30:
                     logging.warning(f"Title for {locale_code} over 30 chars limit!")
                if len(metadata['subtitle']) > 30:
                     logging.warning(f"Subtitle for {locale_code} over 30 chars limit!")
                if len(metadata['keywords']) > 100:
                     logging.warning(f"Keywords for {locale_code} over 100 chars limit!")
                
                # Save to file
                filepath = os.path.join(OUTPUT_DIR, f"{locale_code}_metadata.json")
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, ensure_ascii=False, indent=4)
                    
                logging.info(f"Saved: {filepath}\n")
            except json.JSONDecodeError:
                 logging.error(f"Failed to parse JSON for {lang_name}: {metadata_json_str}\n")

if __name__ == "__main__":
    main()
