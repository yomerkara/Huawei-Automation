import re


def ask_user_questions():
    # Questions to ask the user
    questions = {
        "saha_kodu": "Saha kodu ne? (Örnek: UIS5110)",
        "tech": "Hangi Teknolojiyi kuruyorsun? (900 veya 2100)",
        "ran": "Hangi RAN'dasın? (4, 5 veya 6)",
        "endWith": "500 mü 510 mu?",
        "transmission_resource_pool_index": "Transmission Resource Pool Index'in nedir?",
        "sector_number": "Sahada kaç sektör var?",
        "have_chipsett": "Chipset verildi mi? (E/H)",
        "new_huawei_rnc_id": "New Huawei RNC ID'si nedir?",
        "cabinet_type": "5900 kabin mi 3900 kabin mi?",
        "files_loaded": "Gerekli dosyaları sourceFiles klasörüne yükledin mi? (E/H)"
    }

    # Dictionary to store user answers
    user_answers = {}
    
    def validate_saha_kodu(saha_kodu):
        return bool(re.match(r'^[A-Za-z]{3}\d{4}$', saha_kodu))
    
    def validate_technology(teknoloji):
        return teknoloji in ["900", "2100"]

    def validate_ran(ran):
        return ran in ["4", "5", "6"]

    def validate_chipsett(have_chipsett):
        return have_chipsett in ["E", "H"]
    
    def validate_files_loaded(files_loaded):
        return files_loaded in ["E", "H"]
    
    for key, question in questions.items():
        while True:
            answer = input(f"{question} ")

            # Validate saha_kodu
            if key == "saha_kodu":
                if validate_saha_kodu(answer):
                    user_answers[key] = answer
                    break
                else:
                    print("Geçersiz saha kodu. 3 harf ve 4 sayıdan oluşmalı. (Örn: UAB1234)")

            # Validate teknoloji
            elif key == "tech":
                if validate_technology(answer):
                    user_answers[key] = answer
                    break
                else:
                    print("Geçersiz teknoloji. Yalnızca 900 veya 2100 kabul ediliyor.")

            # Validate ran
            elif key == "ran":
                if validate_ran(answer):
                    user_answers[key] = answer
                    break
                else:
                    print("Geçersiz RAN. Yalnızca 4, 5, veya 6 kabul ediliyor.")
                    
            elif key == "have_chipsett":
                if validate_chipsett(answer):
                    user_answers[key] = answer
                    break
                else:
                    print("Geçersiz cevap. Yalnızca E veya H.")
                    
            elif key == "files_loaded":
                if validate_files_loaded(answer):
                    user_answers[key] = answer
                    break
                else:
                    print("Geçersiz cevap. Yalnızca E veya H.")        

            # For all other inputs, accept the answer
            else:
                user_answers[key] = answer
                break

    return user_answers

    