from InquirerPy import inquirer
from InquirerPy.base.control import Choice
import os
import json

languages = {
    "Afrikaans": "afr",
    "Amharic": "amh",
    "Arabic": "ara",
    "Assamese": "asm",
    "Azerbaijani": "aze",
    "Azerbaijani (Cyrillic)": "aze_cyrl",
    "Belarusian": "bel",
    "Bengali": "ben",
    "Tibetan": "bod",
    "Bosnian": "bos",
    "Breton": "bre",
    "Bulgarian": "bul",
    "Catalan": "cat",
    "Cebuano": "ceb",
    "Czech": "ces",
    "Chinese Simplified": "chi_sim",
    "Chinese Simplified Vertical": "chi_sim_vert",
    "Chinese Traditional": "chi_tra",
    "Chinese Traditional Vertical": "chi_tra_vert",
    "Cherokee": "chr",
    "Corsican": "cos",
    "Welsh": "cym",
    "Danish": "dan",
    "Danish Fraktur": "dan_frak",
    "German": "deu",
    "German Fraktur": "deu_frak",
    "German Latin-F": "deu_latf",
    "Divehi": "div",
    "Dzongkha": "dzo",
    "Greek": "ell",
    "English": "eng",
    "Middle English": "enm",
    "Esperanto": "epo",
    "Equestrian": "equ",
    "Estonian": "est",
    "Basque": "eus",
    "Faroese": "fao",
    "Persian": "fas",
    "Filipino": "fil",
    "Finnish": "fin",
    "French": "fra",
    "Middle French": "frm",
    "Frisian": "fry",
    "Scottish Gaelic": "gla",
    "Irish": "gle",
    "Galician": "glg",
    "Ancient Greek": "grc",
    "Gujarati": "guj",
    "Haitian": "hat",
    "Hebrew": "heb",
    "Hindi": "hin",
    "Croatian": "hrv",
    "Hungarian": "hun",
    "Armenian": "hye",
    "Inuktitut": "iku",
    "Indonesian": "ind",
    "Icelandic": "isl",
    "Italian": "ita",
    "Old Italian": "ita_old",
    "Javanese": "jav",
    "Japanese": "jpn",
    "Japanese Vertical": "jpn_vert",
    "Kannada": "kan",
    "Georgian": "kat",
    "Old Georgian": "kat_old",
    "Kazakh": "kaz",
    "Khmer": "khm",
    "Kyrgyz": "kir",
    "Kurmanji Kurdish": "kmr",
    "Korean": "kor",
    "Korean Vertical": "kor_vert",
    "Lao": "lao",
    "Latin": "lat",
    "Latvian": "lav",
    "Lithuanian": "lit",
    "Luxembourgish": "ltz",
    "Malayalam": "mal",
    "Marathi": "mar",
    "Macedonian": "mkd",
    "Maltese": "mlt",
    "Mongolian": "mon",
    "Maori": "mri",
    "Malay": "msa",
    "Burmese": "mya",
    "Nepali": "nep",
    "Dutch": "nld",
    "Norwegian": "nor",
    "Occitan": "oci",
    "Odia": "ori",
    "Orientation and Script Detection": "osd",
    "Punjabi": "pan",
    "Polish": "pol",
    "Portuguese": "por",
    "Pashto": "pus",
    "Quechua": "que",
    "Romanian": "ron",
    "Russian": "rus",
    "Sanskrit": "san",
    "Sinhala": "sin",
    "Slovak": "slk",
    "Slovak Fraktur": "slk_frak",
    "Slovenian": "slv",
    "Sindhi": "snd",
    "Spanish": "spa",
    "Albanian": "sqi",
    "Serbian": "srp",
    "Serbian Latin": "srp_latn",
    "Sundanese": "sun",
    "Swahili": "swa",
    "Swedish": "swe",
    "Syriac": "syr",
    "Tamil": "tam",
    "Tatar": "tat",
    "Telugu": "tel",
    "Tajik": "tgk",
    "Tagalog": "tgl",
    "Thai": "tha",
    "Tigrinya": "tir",
    "Tonga": "ton",
    "Turkish": "tur",
    "Uighur": "uig",
    "Ukrainian": "ukr",
    "Urdu": "urd",
    "Uzbek": "uzb",
    "Uzbek Cyrillic": "uzb_cyrl",
    "Vietnamese": "vie",
    "Yiddish": "yid",
    "Yoruba": "yor"
}

def select_popular_languages():
    popular_languages = [
        "English", "Spanish", "French", "German",
        "Chinese Simplified", "Japanese", "Korean",
        "Arabic", "Hindi", "Russian"
    ]
    
    selected = inquirer.checkbox(
        message=f"Select Popular Languages ({len(popular_languages)} available):",
        choices=popular_languages,
        instruction="(type to search, space to select/deselect, enter to confirm)"
    ).execute()
    
    if not selected:
        print("No languages selected. Defaulting to English.")
        selected = ["English"]
    
    return selected


def method1_categorized_selection():
    categories = {
        "European Languages": ["English", "Spanish", "French", "German", "Italian", "Portuguese", "Dutch", "Swedish", "Norwegian", "Danish", "Polish", "Czech", "Hungarian", "Romanian", "Bulgarian", "Greek", "Croatian", "Serbian", "Albanian", "Latvian", "Lithuanian", "Estonian", "Finnish", "Icelandic", "Irish", "Welsh", "Basque", "Catalan", "Galician"],
        "Asian Languages": ["Chinese Simplified", "Chinese Traditional", "Japanese", "Korean", "Hindi", "Bengali", "Telugu", "Tamil", "Gujarati", "Marathi", "Kannada", "Malayalam", "Odia", "Punjabi", "Assamese", "Nepali", "Sinhala", "Thai", "Vietnamese", "Indonesian", "Malay", "Filipino", "Burmese", "Khmer", "Lao", "Mongolian", "Tibetan", "Dzongkha"],
        "Middle Eastern & African": ["Arabic", "Hebrew", "Persian", "Turkish", "Amharic", "Tigrinya", "Swahili", "Yoruba", "Haitian", "Afrikaans"],
        "Cyrillic Scripts": ["Russian", "Ukrainian", "Bulgarian", "Macedonian", "Serbian", "Belarusian", "Kazakh", "Kyrgyz", "Uzbek Cyrillic", "Azerbaijani (Cyrillic)"],
        "Historical & Specialized": ["Latin", "Ancient Greek", "Middle English", "Middle French", "Old Italian", "Old Georgian", "Sanskrit", "Orientation and Script Detection"]
    }
    
    category_choice = inquirer.select(
        message="How would you like to browse languages?",
        choices=[
            Choice("all", "Search/Browse All Languages"),
            Choice("popular", "Popular Languages"),
            Choice("european", "European Languages"),
            Choice("asian", "Asian Languages"),
            Choice("middle_eastern", "Middle Eastern & African Languages"),
            Choice("cyrillic", "Cyrillic Script Languages"),
            Choice("historical", "Historical & Specialized Languages")
        ]
    ).execute()
    
    if category_choice == "all":
        available_languages = sorted(languages.keys())
    else:
        category_map = {
            "popular": "Popular Languages",
            "european": "European Languages", 
            "asian": "Asian Languages",
            "middle_eastern": "Middle Eastern & African",
            "cyrillic": "Cyrillic Scripts",
            "historical": "Historical & Specialized"
        }
        available_languages = [lang for lang in categories[category_map[category_choice]] if lang in languages]
    
    selected = inquirer.checkbox(
        message=f"Select languages ({len(available_languages)} available):",
        choices=available_languages,
        instruction="(type to search, space to select/deselect, enter to confirm)"
    ).execute()
    
    return selected

def method2_enhanced_search():
    choices = []
    for name, code in sorted(languages.items()):
        choices.append(Choice(name, f"{name} ({code})"))
    
    selected = inquirer.checkbox(
        message=f"Select languages ({len(languages)} total):",
        choices=choices,
        instruction="(type to search by name, space to select/deselect, enter to confirm)",
        transformer=lambda result: f"{len(result)} selected"
    ).execute()
    
    return selected

def method3_multi_step():
    print("=== Language Selection Wizard ===\n")
    
    use_case = inquirer.select(
        message="What's your primary use case?",
        choices=[
            Choice("document", "Document/Text OCR"),
            Choice("multilingual", "Multilingual documents"),
            Choice("specific", "I know exactly which languages I need"),
            Choice("browse", "Let me browse all options")
        ]
    ).execute()
    
    if use_case == "document":
        common_langs = ["English", "Spanish", "French", "German", "Chinese Simplified", "Japanese", "Korean", "Arabic", "Portuguese", "Italian", "Russian", "Hindi"]
        print(f"\nSuggested languages for document OCR:")
        
    elif use_case == "multilingual":
        preset = inquirer.select(
            message="Choose a preset or custom:",
            choices=[
                Choice("european", "European Languages (EN, FR, DE, ES, IT, PT)"),
                Choice("asian", "Major Asian Languages (EN, ZH, JA, KO, HI)"),
                Choice("global", "Global Mix (EN, ES, FR, DE, ZH, AR, RU, PT, JA, HI)"),
                Choice("custom", "Custom selection")
            ]
        ).execute()
        
        presets = {
            "european": ["English", "French", "German", "Spanish", "Italian", "Portuguese"],
            "asian": ["English", "Chinese Simplified", "Japanese", "Korean", "Hindi"],
            "global": ["English", "Spanish", "French", "German", "Chinese Simplified", "Arabic", "Russian", "Portuguese", "Japanese", "Hindi"]
        }
        
        if preset != "custom":
            return presets[preset]
            
    selected = inquirer.checkbox(
        message="Select your languages:",
        choices=sorted(languages.keys()),
        instruction="(type to search, space to select, enter to confirm)",
        transformer=lambda result: f"{len(result)} languages selected"
    ).execute()
    
    return selected

def method4_quick_common():
    common_languages = [
        "English", "Spanish", "French", "German", "Chinese Simplified", 
        "Japanese", "Korean", "Arabic", "Hindi", "Russian", "Portuguese", 
        "Italian", "Dutch", "Polish", "Turkish"
    ]
    
    quick_select = inquirer.checkbox(
        message="Quick select common languages (optional):",
        choices=common_languages,
        instruction="(space to select, enter to continue)"
    ).execute()
    
    if quick_select:
        add_more = inquirer.confirm(
            message=f"You selected {len(quick_select)} languages. Add more?",
            default=False
        ).execute()
        
        if not add_more:
            return quick_select
    
    remaining_languages = [lang for lang in sorted(languages.keys()) if lang not in quick_select]
    additional = inquirer.checkbox(
        message="Select additional languages:",
        choices=remaining_languages,
        instruction="(type to search, space to select, enter to confirm)"
    ).execute()
    
    return quick_select + additional

def main():
    print("Choose a selection method:")
    method = inquirer.select(
        message="Which method would you prefer?",
        choices=[
            Choice(1, "Method 1: Popular languages"),
            Choice(2, "Method 2: Enhanced Search with Codes"),
            Choice(3, "Method 3: Multi-step Wizard"),
            Choice(4, "Method 4: Quick Common + Search"),
            Choice(1, "Method 5: Categorized Selection")
        ]
    ).execute()
    
    if method == 1:
        selected = select_popular_languages()
        
    elif method == 2:
        selected = method2_enhanced_search()
    elif method == 3:
        selected = method3_multi_step()
    elif method==4:
        selected = method4_quick_common()
    else:
        selected = method1_categorized_selection()
        
   
    while True:
        SCREENSHOT_DIR = inquirer.text(
            message="Which directory do you want to watch over?"
        ).execute()

        if os.path.isdir(SCREENSHOT_DIR):
            print(f"Watching directory: {SCREENSHOT_DIR}")
            break
        else:
            print("Invalid directory. Please try again.")
    
    if selected:
        print(f"\nSelected languages: {', '.join(selected)}")
        file = os.path.join(os.getcwd(), "config.json")

        codes = [languages[lang] for lang in selected]
        if not codes:
            codes = ["eng"]

        codes_str = "+".join(codes)

        config = {
            "SCREENSHOT_DIR": SCREENSHOT_DIR,
            "lang": codes_str
        }

        with open(file, "w") as f:
            json.dump(config, f, indent=4)

        print(f"Codes: {[languages[lang] for lang in selected]}")
    else:
        print("No languages selected.")

if __name__ == "__main__":
    main()